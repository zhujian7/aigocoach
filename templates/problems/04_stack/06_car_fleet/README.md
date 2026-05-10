# Car Fleet

- **Difficulty**: Medium
- **Category**: Stack
- **Topics**: stack, sorting, monotonic stack
- **Link**: [NeetCode](https://neetcode.io/problems/car-fleet) | [LeetCode 853](https://leetcode.com/problems/car-fleet/)

## Description

There are `n` cars at given miles away from the starting mile 0, heading to a target at `target` miles. You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting position of the `i`th car and `speed[i]` is the speed of the `i`th car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up and then travel at the same speed as the car ahead. A car fleet is a group of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet at the exact moment the fleet reaches the target, it is considered part of that fleet. Return the number of car fleets that will arrive at the target.

## Examples

**Example 1:**

```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The car starting at 0 never catches up. The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting at 6. So there are 3 fleets.
```

**Example 2:**

```
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, so there is one fleet.
```

**Example 3:**

```
Input: target = 100, position = [0,50], speed = [1,1]
Output: 2
Explanation: Both cars travel at the same speed but the car at position 50 is ahead, so they never meet and form 2 separate fleets.
```

## Constraints

- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- `0 < speed[i] <= 10^6`
- All the values of `position` are unique

## Function Signature

**Go:**

```go
func carFleet(target int, position []int, speed []int) int
```

**Python:**
```python
def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
```
