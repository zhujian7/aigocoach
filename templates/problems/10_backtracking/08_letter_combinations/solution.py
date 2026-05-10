from typing import List


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
    }
    result = []

    def backtrack(idx: int, current: List[str]) -> None:
        if idx == len(digits):
            result.append(''.join(current))
            return
        for ch in phone[digits[idx]]:
            current.append(ch)
            backtrack(idx + 1, current)
            current.pop()

    backtrack(0, [])
    return result
