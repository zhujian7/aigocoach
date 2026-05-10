from typing import List


def solve_group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for s in strs:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord('a')] += 1
        groups.setdefault(tuple(key), []).append(s)
    return list(groups.values())
