from __future__ import annotations

import argparse
import json

from .search import search_community_index, update_and_search


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", action="store_true")
    parser.add_argument("--query")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args()

    if args.search:
        if not args.query:
            print("--query is required")
            return 1
        results = update_and_search(args.query, args.limit) if args.update else search_community_index(args.query, args.limit)
        print(json.dumps({"packs": results}, indent=2))
        return 0

    print("rulebook-ai MCP server stub")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
