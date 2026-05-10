def solve_num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    prev, curr = 1, 1
    for i in range(1, len(s)):
        tmp = 0
        if s[i] != '0':
            tmp = curr
        two_digit = int(s[i - 1]) * 10 + int(s[i])
        if 10 <= two_digit <= 26:
            tmp += prev
        prev, curr = curr, tmp
    return curr
