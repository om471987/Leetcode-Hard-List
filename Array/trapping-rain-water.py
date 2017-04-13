
def trapping_rain_water(inp):
    if not inp or len(inp) < 3:
        return 0
    n = len(inp)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    max_val = 0
    for i in range(1, n):
        max_val = max(max_val, inp[i])
        left[i] = max_val

    max_val = 0
    for i in range(n - 2, -1, -1):
        max_val = max(max_val, inp[i])
        right[i] = max_val

    output = 0
    for i in range(1, n - 1):
        output += min(left[i], right[i]) - inp[i]
    return output

print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
