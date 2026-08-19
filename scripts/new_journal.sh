#!/usr/bin/env bash
# Helper script to create a timestamped local journal entry
set -euo pipefail

TITLE="${1:-scratchpad}"
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd '[:alnum:]_')
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FILENAME="Journal/${TIMESTAMP}_${SLUG}.md"

mkdir -p Journal

cat << EOF > "$FILENAME"
# Journal Entry: ${TITLE}
**Timestamp:** $(date +"%Y-%m-%d %H:%M:%S")  
**Context / Project:** Quarto Technical Notes  

---

## Objectives & Focus
- 

## Notes & Observations
- 

## Next Actions
- [ ] 
EOF

echo "✓ Created local journal entry: $FILENAME"
