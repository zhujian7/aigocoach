def solve_is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not is_alpha_num(s[l]):
            l += 1
        while l < r and not is_alpha_num(s[r]):
            r -= 1
        if to_lower(s[l]) != to_lower(s[r]):
            return False
        l += 1
        r -= 1
    return True


def is_alpha_num(c: str) -> bool:
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')


def to_lower(c: str) -> str:
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32)
    return c
