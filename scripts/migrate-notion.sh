#!/usr/bin/env bash
# Migrate one Notion Markdown export into a visible Quarto post.
# Usage: scripts/migrate-notion.sh <export-directory> <target-post-directory> [--draft] [category ...]
set -euo pipefail

SOURCE_DIR=${1:?"usage: $0 <export-directory> <target-post-directory> [category ...]"}
TARGET_DIR=${2:?"usage: $0 <export-directory> <target-post-directory> [category ...]"}
shift 2
DRAFT=false
CATEGORIES=()
while [ "$#" -gt 0 ]; do
  if [ "$1" = "--draft" ]; then
    DRAFT=true
  else
    CATEGORIES+=("$1")
  fi
  shift
done
[ "${#CATEGORIES[@]}" -gt 0 ] || CATEGORIES=(research-notes)

SOURCE_DIR=${SOURCE_DIR%/}
TARGET_DIR=${TARGET_DIR%/}
SOURCE_MD=$(find "$SOURCE_DIR" -maxdepth 1 -type f -name '*.md' -print -quit)
[ -n "$SOURCE_MD" ] || { echo "error: no Markdown export found in $SOURCE_DIR" >&2; exit 1; }
mkdir -p "$TARGET_DIR/media"

TITLE=$(sed -n '1s/^# //p' "$SOURCE_MD")
DATE_TEXT=$(sed -n '2,8p' "$SOURCE_MD" | grep -E '^[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}$' | head -1 || true)
DATE=$(printf '%s\n' "$DATE_TEXT" | perl -MTime::Piece -ne 'chomp; print Time::Piece->strptime($_, "%b %d, %Y")->strftime("%Y-%m-%d")' 2>/dev/null || date +%Y-%m-%d)
AUTHOR=$(sed -n '2,10p' "$SOURCE_MD" | grep -E '^[A-Z][A-Z .,&-]+$' | head -1 | sed 's/  */ /g' | sed 's/^ *//;s/ *$//' || true)
[ -n "$AUTHOR" ] || AUTHOR="Muhammad Ghifary"
MEDIA_SOURCE=$(find "$SOURCE_DIR" -mindepth 1 -maxdepth 1 -type d -print -quit || true)

if [ -n "$MEDIA_SOURCE" ]; then
  cp -f "$MEDIA_SOURCE"/* "$TARGET_DIR/media/" 2>/dev/null || true
fi

BODY=$(mktemp)
trap 'rm -f "$BODY"' EXIT
awk -v author="$AUTHOR" 'BEGIN { seen=0 } { if (!seen && $0 == author) { seen=1; next } if (seen) print }' "$SOURCE_MD" > "$BODY"

# Localize exported media links, embed videos, and trim whitespace around inline math.
if [ -n "$MEDIA_SOURCE" ]; then
  for file in "$TARGET_DIR"/media/*; do
    [ -f "$file" ] || continue
    name=${file##*/}
    encoded=$(printf '%s' "$name" | sed 's/ /%20/g; s/(/%28/g; s/)/%29/g')
    folder=$(basename "$MEDIA_SOURCE")
    encoded_folder=$(printf '%s' "$folder" | sed 's/ /%20/g; s/(/%28/g; s/)/%29/g')
    perl -0pi -e "s/\Q$folder\E\/\Q$name\E/media\/$name/g; s/\Q$folder\E\/\Q$encoded\E/media\/$name/g; s/\Q$encoded_folder\E\/\Q$encoded\E/media\/$name/g" "$BODY"
    case "$name" in
      *.mp4|*.webm|*.mov)
        type=${name##*.}
        perl -0pi -e "s/\[$name\]\(media\/\Q$name\E\)/<video controls preload=\"metadata\" width=\"100%\"><source src=\"media\/$name\" type=\"video\/$type\">Your browser does not support embedded video.<\/video>/g" "$BODY"
        ;;
    esac
  done
fi
perl -0pi -e 's/(?<!\\)(?<!\$)\$\s+/\$/g; s/\s+\$(?!\$)/\$/g' "$BODY"

escaped_title=$(printf '%s' "$TITLE" | sed 's/"/\\\\"/g')
{
  printf '%s\n' '---'
  printf 'title: "%s"\n' "$escaped_title"
  printf 'author: "%s"\n' "$AUTHOR"
  printf 'date: %s\n' "$DATE"
  printf '%s\n' 'description: "Imported and normalized from a Notion article."' 'categories:'
  for category in "${CATEGORIES[@]}"; do printf '  - %s\n' "$category"; done
  printf 'draft: %s\n' "$DRAFT"
  printf '%s\n' '---' ''
  cat "$BODY"
} > "$TARGET_DIR/index.qmd"

# Explicit project render globs otherwise include drafts, so exclude only when
# the caller explicitly requests --draft.
CONFIG="_quarto.yml"
EXCLUSION="    - \"!$TARGET_DIR/index.qmd\""
if [ "$DRAFT" = true ] && [ -f "$CONFIG" ] && ! grep -Fqx "$EXCLUSION" "$CONFIG"; then
  awk -v exclusion="$EXCLUSION" '{ print; if ($0 == "    - \"posts/*/*.qmd\"") print exclusion }' "$CONFIG" > "$CONFIG.tmp"
  mv "$CONFIG.tmp" "$CONFIG"
fi

printf 'created %s\n' "$TARGET_DIR/index.qmd"
