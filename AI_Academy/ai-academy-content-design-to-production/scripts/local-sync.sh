#!/bin/bash
# Local-only: temporarily publish $TRACK in working tree, seed|content-sync the guarded localhost DB, then restore. Usage: REPO=… TRACK=… local-sync.sh [seed|content-sync]
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
cd ${REPO:?set REPO}
cp curriculum/${TRACK:?set TRACK}/index.json /tmp/${TRACK}-index.bak
trap 'cp /tmp/${TRACK}-index.bak curriculum/${TRACK:?set TRACK}/index.json' EXIT
sed -i 's/"isPublished": false/"isPublished": true/g' curriculum/${TRACK:?set TRACK}/index.json
$HERE/guard.sh npx tsx scripts/${1:-content-sync}.ts
