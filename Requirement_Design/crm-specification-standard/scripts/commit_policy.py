#!/usr/bin/env python3
"""Portable entrypoint for the shared CRM commit-message policy."""
import sys
sys.dont_write_bytecode = True
from kit_commits import main
if __name__ == '__main__':
    raise SystemExit(main())
