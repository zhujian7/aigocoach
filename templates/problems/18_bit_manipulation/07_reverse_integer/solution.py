def solve_reverse(x: int) -> int:
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)
    result = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x != 0:
        digit = x % 10
        x //= 10
        if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
            return 0
        result = result * 10 + digit
    result *= sign
    if result < MIN_INT or result > MAX_INT:
        return 0
    return result
