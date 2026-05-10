# Combination Sum II

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, sorting, deduplication
- **Link**: [NeetCode](https://neetcode.io/problems/combination-target-sum-ii) | [LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)

## Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

## Examples

**Example 1:**

```
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
```

**Example 2:**

```
Input: candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1,2,2], [5]]
```

**Example 3:**

```
Input: candidates = [3, 5], target = 1
Output: []
Explanation: No combination sums to 1.
```

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Function Signature

**Go:**

```go
func combinationSum2(candidates []int, target int) [][]int
```

**Python:**
```python
def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
```
