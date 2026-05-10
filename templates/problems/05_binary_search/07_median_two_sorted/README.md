# Median of Two Sorted Arrays

- **Difficulty**: Hard
- **Category**: Binary Search
- **Topics**: binary search, array, divide and conquer
- **Link**: [NeetCode](https://neetcode.io/problems/median-of-two-sorted-arrays) | [LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(min(m, n))).

The median is the middle value in an ordered list. If the list has an even number of elements, the median is the average of the two middle values.

## Examples

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Explanation: The merged array is [1,2,3] and the median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
Explanation: The merged array is [1,2,3,4] and the median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.0
Explanation: The merged array is [1] and the median is 1.
```

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Function Signature

**Go:**

```go
func findMedianSortedArrays(nums1 []int, nums2 []int) float64
```

**Python:**
```python
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
```
