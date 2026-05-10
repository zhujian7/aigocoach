# Koko Eating Bananas

- **Difficulty**: Medium
- **Category**: Binary Search
- **Topics**: binary search, math
- **Link**: [NeetCode](https://neetcode.io/problems/eating-bananas) | [LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/)

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Examples

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: At speed 4, Koko takes 1+2+2+3 = 8 hours, which fits exactly within h = 8.
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: With 5 piles and only 5 hours, Koko must eat each pile in one hour, so speed must be at least max(piles) = 30.
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
Explanation: At speed 23, Koko takes 2+1+1+1+1 = 6 hours, fitting within h = 6.
```

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Function Signature

**Go:**

```go
func minEatingSpeed(piles []int, h int) int
```

**Python:**
```python
def min_eating_speed(piles: List[int], h: int) -> int:
```
