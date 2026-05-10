# Gas Station

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: array, greedy
- **Link**: [NeetCode](https://neetcode.io/problems/gas-station) | [LeetCode 134](https://leetcode.com/problems/gas-station/)

## Description

There are `n` gas stations along a circular route, where the amount of gas at the `i`-th station is `gas[i]`. You have a car with an unlimited gas tank, and it costs `cost[i]` of gas to travel from the `i`-th station to the next `(i + 1)`-th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

## Examples

**Example 1:**

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation: Start at station 3 (gas = 4). Tank = 0+4 = 4. Travel to station 4 (cost 1), tank = 3+5 = 8. Travel to station 0 (cost 2), tank = 6+1 = 7. Travel to station 1 (cost 3), tank = 4+2 = 6. Travel to station 2 (cost 4), tank = 2+3 = 5. Travel to station 3 (cost 5), tank = 0. You can complete the circuit.
```

**Example 2:**

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation: Total gas (9) < total cost (10), so no solution exists.
```

**Example 3:**

```
Input: gas = [5], cost = [3]
Output: 0
```

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Function Signature

**Go:**

```go
func canCompleteCircuit(gas []int, cost []int) int
```

**Python:**
```python
def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
```
