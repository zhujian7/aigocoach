# Kth Largest Element in a Stream

- **Difficulty**: Easy
- **Category**: Heap
- **Topics**: min-heap, priority queue, streaming
- **Link**: [NeetCode](https://neetcode.io/problems/kth-largest-integer-in-a-stream) | [LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Description

Design a class that finds the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element. The class is initialized with an integer `k` and an array of integers `nums`. Each call to the `Add` method inserts a new value into the stream and returns the element representing the `k`th largest element in the current stream.

## Examples

**Example 1:**

```
Input:
  Constructor(3, [4, 5, 8, 2])
  Add(3)  -> 4
  Add(5)  -> 5
  Add(10) -> 5
  Add(9)  -> 8
  Add(4)  -> 8

Explanation: After initialization, the sorted stream is [2,4,5,8]. The 3rd largest is 4.
  Add(3): stream is [2,3,4,5,8], 3rd largest = 4.
  Add(5): stream is [2,3,4,5,5,8], 3rd largest = 5.
  Add(10): stream is [2,3,4,5,5,8,10], 3rd largest = 5.
  Add(9): stream is [2,3,4,5,5,8,9,10], 3rd largest = 8.
  Add(4): stream is [2,3,4,4,5,5,8,9,10], 3rd largest = 8.
```

**Example 2:**

```
Input:
  Constructor(1, [])
  Add(-1) -> -1
  Add(1)  -> 1
  Add(-2) -> 1

Explanation: With k=1, the 1st largest is always the maximum element in the stream.
```

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `Add`.
- It is guaranteed that there will be at least `k` elements when you search for the `k`th element.

## Function Signature

**Go:**

```go
type KthLargest struct {}

func Constructor(k int, nums []int) KthLargest

func (kl *KthLargest) Add(val int) int
```

**Python:**
```python
class KthLargest
def __init__(self, k: int, nums: List[int]):
def add(self, val: int) -> int:
```
