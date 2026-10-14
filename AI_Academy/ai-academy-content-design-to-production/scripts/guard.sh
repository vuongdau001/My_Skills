#!/bin/bash
# usage: guard.sh <cmd...> ; loads .env.local and aborts unless DB host is localhost
set -a; . "${REPO:-.}/.env.local"; set +a
h=$(node -e 'console.log(new URL(process.env.DATABASE_URL).hostname)')
case "$h" in localhost|127.0.0.1) ;; *) echo "ABORT: DB host not local"; exit 1;; esac
[ -e "${REPO:-.}/.env" ] && { echo "ABORT: .env present"; exit 1; }
echo "guard OK host=$h"; exec "$@"
