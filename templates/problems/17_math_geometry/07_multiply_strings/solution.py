def solve_multiply(num1: str, num2: str) -> str:
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + pos[p2]
            pos[p2] = total % 10
            pos[p1] += total // 10
    result = []
    for v in pos:
        if not result and v == 0:
            continue
        result.append(str(v))
    return ''.join(result) if result else "0"
