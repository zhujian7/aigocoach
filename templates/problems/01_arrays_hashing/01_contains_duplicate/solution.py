from typing import List


# Time: O(n), Space: O(n)
def solve_contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
