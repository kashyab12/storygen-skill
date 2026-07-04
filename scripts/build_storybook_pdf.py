from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
PDF_IMAGE_DIR = ROOT / "tmp" / "pdfs" / "pdf-assets"

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONTS = {
    "Georgia": FONT_DIR / "Georgia.ttf",
    "Georgia-Italic": FONT_DIR / "Georgia Italic.ttf",
    "Georgia-Bold": FONT_DIR / "Georgia Bold.ttf",
    "Georgia-BoldItalic": FONT_DIR / "Georgia Bold Italic.ttf",
}

STORIES = [
    {
        "path": ROOT / "samples" / "sesame-seed" / "story.md",
        "output": ROOT / "samples" / "sesame-seed" / "storybook.pdf",
        "title": "Pip of Bramblewick Farm",
        "images": [
            ("Pip of Bramblewick Farm", ROOT / "output" / "images" / "pip-seed-shed.png"),
            ("The flagstones ended at a puddle.", ROOT / "output" / "images" / "pip-leaf-boat.png"),
            ("Morning came white at the edges", ROOT / "output" / "images" / "pip-hen-gate.png"),
            ("They raced the water down to the Big Field's edge.", ROOT / "output" / "images" / "pip-dam-gap.png"),
            ("Pip grew. Oh, how Pip grew", ROOT / "output" / "images" / "pip-spring-field.png"),
        ],
    },
    {
        "path": ROOT / "samples" / "archimedes" / "story.md",
        "output": ROOT / "samples" / "archimedes" / "storybook.pdf",
        "title": "The Circles of Syracuse",
        "images": [
            ("The Circles of Syracuse", ROOT / "output" / "images" / "archimedes-courtyard.png"),
            ("Alexandria, then. The second ring.", ROOT / "output" / "images" / "archimedes-alexandria.png"),
            ("The fourth circle. The lever.", ROOT / "output" / "images" / "archimedes-syracusia.png"),
            ("The siege. Two years of it", ROOT / "output" / "images" / "archimedes-siege-wall.png"),
            ("Dexios had turned at the garden gate", ROOT / "output" / "images" / "archimedes-dexios-escape.png"),
        ],
    },
]


def register_fonts() -> str:
    missing = [str(path) for path in FONTS.values() if not path.exists()]
    if missing:
        return "Times-Roman"
    for name, path in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "Georgia",
        normal="Georgia",
        bold="Georgia-Bold",
        italic="Georgia-Italic",
        boldItalic="Georgia-BoldItalic",
    )
    return "Georgia"


def markdown_inline_to_reportlab(text: str) -> str:
    escaped = html.escape(text, quote=False)

    def italic(match: re.Match[str]) -> str:
        return f"<i>{match.group(1)}</i>"

    return re.sub(r"\*(.+?)\*", italic, escaped)


def read_markdown_blocks(path: Path) -> list[tuple[str, str]]:
    raw = path.read_text(encoding="utf-8").strip()
    blocks: list[tuple[str, str]] = []
    for block in re.split(r"\n\s*\n", raw):
        normalized = " ".join(line.strip() for line in block.splitlines())
        if normalized.startswith("# "):
            blocks.append(("title", normalized[2:]))
        else:
            blocks.append(("paragraph", normalized))
    return blocks


def story_image(max_width: float, path: Path) -> Image:
    PDF_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    embedded_path = PDF_IMAGE_DIR / f"{path.stem}.jpg"
    with PILImage.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((1800, 1800), PILImage.Resampling.LANCZOS)
        im.save(embedded_path, quality=88, optimize=True)
        width, height = im.size
    display_width = max_width
    display_height = display_width * height / width
    max_height = 4.25 * inch
    if display_height > max_height:
        scale = max_height / display_height
        display_width *= scale
        display_height *= scale
    image = Image(str(embedded_path), width=display_width, height=display_height)
    image.hAlign = "CENTER"
    return image


def build_story(story: dict[str, object], font_name: str) -> None:
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "StoryTitle",
        parent=styles["Title"],
        fontName=f"{font_name}-Bold" if font_name == "Georgia" else "Times-Bold",
        fontSize=25,
        leading=31,
        alignment=TA_CENTER,
        spaceAfter=0.28 * inch,
    )
    body_style = ParagraphStyle(
        "StoryBody",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=11.2,
        leading=16.4,
        firstLineIndent=0.2 * inch,
        spaceAfter=8,
    )

    output = story["output"]
    assert isinstance(output, Path)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output),
        pagesize=letter,
        leftMargin=0.78 * inch,
        rightMargin=0.78 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.72 * inch,
        title=str(story["title"]),
        author="",
    )

    flowables = []
    max_width = doc.width
    image_queue = list(story["images"])
    used_images: set[Path] = set()

    def append_matching_images(text: str) -> None:
        while image_queue and image_queue[0][0] in text:
            _, image_path = image_queue.pop(0)
            flowables.append(story_image(max_width, image_path))
            flowables.append(Spacer(1, 0.2 * inch))
            used_images.add(image_path)

    story_path = story["path"]
    assert isinstance(story_path, Path)
    for kind, text in read_markdown_blocks(story_path):
        if kind == "title":
            flowables.append(Paragraph(markdown_inline_to_reportlab(text), title_style))
            append_matching_images(text)
        else:
            append_matching_images(text)
            flowables.append(Paragraph(markdown_inline_to_reportlab(text), body_style))
    if image_queue:
        missing = ", ".join(marker for marker, _ in image_queue)
        raise RuntimeError(f"Image markers were not found in {story_path}: {missing}")
    expected = {path for _, path in story["images"]}
    if used_images != expected:
        raise RuntimeError(f"Some images were not inserted for {story_path}")

    doc.build(flowables)


def build() -> None:
    if PDF_IMAGE_DIR.exists():
        shutil.rmtree(PDF_IMAGE_DIR)
    font_name = register_fonts()
    for story in STORIES:
        build_story(story, font_name)
    if PDF_IMAGE_DIR.exists():
        shutil.rmtree(PDF_IMAGE_DIR)


if __name__ == "__main__":
    build()
