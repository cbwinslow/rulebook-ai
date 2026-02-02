from __future__ import annotations

from typing import Dict, List

from .community_packs import load_index_cache, update_index_cache


def search_community_index(query: str, limit: int = 10) -> List[Dict[str, str]]:
    q = query.lower()
    packs = load_index_cache().get("packs", [])
    results = [
        p
        for p in packs
        if q in p.get("name", "").lower()
        or q in p.get("description", "").lower()
        or q in p.get("repo", "").lower()
        or q in p.get("username", "").lower()
    ]
    return results[:limit]


def update_and_search(query: str, limit: int = 10) -> List[Dict[str, str]]:
    update_index_cache()
    return search_community_index(query, limit=limit)
