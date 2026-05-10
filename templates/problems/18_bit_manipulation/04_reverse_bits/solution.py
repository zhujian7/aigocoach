def solve_reverse_bits(num: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (num & 1)
        num >>= 1
    return result
