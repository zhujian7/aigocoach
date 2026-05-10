from typing import List


def partition(s: str) -> List[List[str]]:
    result = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, current: List[str]) -> None:
        if start == len(s):
            result.append(current[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                current.append(sub)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result
