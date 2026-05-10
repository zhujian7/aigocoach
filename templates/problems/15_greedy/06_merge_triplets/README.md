# Merge Triplets to Form Target Triplet

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: array, greedy
- **Link**: [NeetCode](https://neetcode.io/problems/merge-triplets-to-form-target) | [LeetCode 1899](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)

## Description

A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]` describes the `i`-th triplet. You are also given an integer array `target = [x, y, z]` that describes the triplet you want to obtain. To obtain `target`, you may apply the following operation on `triplets` any number of times: choose two indices `i` and `j` (where `i != j`) and update `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`. Return `true` if it is possible to obtain the `target` triplet as an element of `triplets`, or `false` otherwise.

## Examples

**Example 1:**

```
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Merge triplets [2,5,3] and [1,7,5] to get [2,7,5].
```

**Example 2:**

```
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: No combination can produce a value of 2 in the second position since both triplets have values >= 4 in the second position.
```

**Example 3:**

```
Input: triplets = [[2,5,3],[10,1,1],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Triplet [10,1,1] is filtered out because 10 > target[0]. Merge [2,5,3] and [1,7,5] to get [2,7,5].
```

## Constraints

- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= ai, bi, ci, x, y, z <= 1000`

## Function Signature

**Go:**

```go
func mergeTriplets(triplets [][]int, target []int) bool
```

**Python:**
```python
def merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
```
