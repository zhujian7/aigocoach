# Top K Frequent Elements

- **Difficulty**: Medium
- **Category**: Arrays & Hashing
- **Topics**: array, hash table, bucket sort, heap
- **Link**: [NeetCode](https://neetcode.io/problems/top-k-elements-in-list) | [LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

## Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

It is guaranteed that the answer is unique.

## Examples

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times and 2 appears 2 times. The two most frequent elements are 1 and 2.
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Example 3:**

```
Input: nums = [-1,-1,-2,-2,-2,-3], k = 1
Output: [-2]
Explanation: -2 appears 3 times, which is the most frequent element.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

## Function Signature

**Go:**

```go
func topKFrequent(nums []int, k int) []int
```

**Python:**
```python
def top_k_frequent(nums: List[int], k: int) -> List[int]:
```
