# Last Stone Weight

- **Difficulty**: Easy
- **Category**: Heap
- **Topics**: max-heap, priority queue, simulation
- **Link**: [NeetCode](https://neetcode.io/problems/last-stone-weight) | [LeetCode 1046](https://leetcode.com/problems/last-stone-weight/)

## Description

You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone. We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. If `x == y`, both stones are destroyed. If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`. At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return `0`.

## Examples

**Example 1:**

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: Smash 7 and 8 -> 1 remains. Smash 4 and 2 -> 2 remains. Smash 2 and 1 -> 1 remains. Smash 1 and 1 -> both destroyed. One stone of weight 1 remains.
```

**Example 2:**

```
Input: stones = [3,3]
Output: 0
Explanation: Both stones have the same weight, so they are both destroyed. No stones remain.
```

**Example 3:**

```
Input: stones = [1]
Output: 1
Explanation: Only one stone exists, so it is the last remaining stone.
```

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Function Signature

**Go:**

```go
func lastStoneWeight(stones []int) int
```

**Python:**
```python
def last_stone_weight(stones: List[int]) -> int:
```
