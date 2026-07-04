#!/usr/bin/env bash
# storygen installer — installs the skill + Braintrust subagents for
# Cursor, Claude Code, and/or Codex, at user or project scope.
#
# Usage:
#   ./install.sh                  # install for all detected tools, user scope
#   ./install.sh cursor           # just Cursor
#   ./install.sh claude codex     # Claude Code + Codex
#   ./install.sh --project all    # project scope (./.cursor, ./.claude, ./.codex)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCOPE="user"
TARGETS=()

for arg in "$@"; do
  case "$arg" in
    --project) SCOPE="project" ;;
    --user) SCOPE="user" ;;
    cursor|claude|codex) TARGETS+=("$arg") ;;
    all) TARGETS=(cursor claude codex) ;;
    -h|--help)
      sed -n '2,9p' "$0"; exit 0 ;;
    *) echo "Unknown argument: $arg (expected cursor|claude|codex|all, --project, --user)"; exit 1 ;;
  esac
done

# Default: install for every tool already present on this machine (user scope)
# or all three at project scope.
if [ ${#TARGETS[@]} -eq 0 ]; then
  if [ "$SCOPE" = "project" ]; then
    TARGETS=(cursor claude codex)
  else
    [ -d "$HOME/.cursor" ] && TARGETS+=(cursor)
    [ -d "$HOME/.claude" ] && TARGETS+=(claude)
    [ -d "$HOME/.codex" ]  && TARGETS+=(codex)
    if [ ${#TARGETS[@]} -eq 0 ]; then
      echo "No ~/.cursor, ~/.claude, or ~/.codex found. Pass a target explicitly, e.g.: ./install.sh cursor"
      exit 1
    fi
  fi
fi

install_to() {
  local base="$1" tool="$2"
  mkdir -p "$base/skills/storygen" "$base/agents"
  cp "$REPO_DIR/skills/storygen/"*.md "$base/skills/storygen/"
  cp "$REPO_DIR/agents/"*.md "$base/agents/"
  echo "  $tool: skill -> $base/skills/storygen, agents -> $base/agents"
}

echo "Installing storygen ($SCOPE scope) for: ${TARGETS[*]}"
for t in "${TARGETS[@]}"; do
  if [ "$SCOPE" = "project" ]; then
    install_to "$(pwd)/.$t" "$t"
  else
    install_to "$HOME/.$t" "$t"
  fi
done

echo "Done. Restart the tool (or reload the window) so it picks up the new skill and agents."
echo "Invoke with a prompt like: \"Use the storygen skill to write a short story about ...\""
