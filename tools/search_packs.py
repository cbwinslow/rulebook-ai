#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from typing import Any

from rulebook_ai.community_packs import load_index_cache, update_index_cache


def _match(entry: dict[str, Any], query: str) -> bool:
    q = query.lower()
    return any(q in (entry.get(field, "").lower()) for field in ("name", "repo", "description", "username"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Search community packs index")
    parser.add_argument("--query", "-q", required=True)
    parser.add_argument("--limit", "-n", type=int, default=10)
    parser.add_argument("--update", action="store_true", help="Refresh index cache first")
    args = parser.parse_args()

    if args.update:
        rc = update_index_cache()
        if rc != 0:
            return rc

    index = load_index_cache().get("packs", [])
    results = [p for p in index if _match(p, args.query)]
    results = results[: args.limit]
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
