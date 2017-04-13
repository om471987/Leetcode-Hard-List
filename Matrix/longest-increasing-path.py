
def longest_increasing_path(inp):
    if not inp or len(inp) == 0 or len(inp[0]) == 0:
        return 0
    n = len(inp)
    m = len(inp[0])
    output = 0
    cache = [[0 for _ in range(m)] for _ in range(n)]

    def dfs(i, j, count):
        if cache[i][j] > 0:
            return cache[i][j] + count
        count1, count2, count3, count4 = 0, 0, 0, 0
        if i > 0 and inp[i][j] < inp[i - 1][j]:
            count1 = dfs(i - 1, j, count + 1)
        if i < (n - 1) and inp[i][j] < inp[i + 1][j]:
            count2 = dfs(i + 1, j, count + 1)
        if j > 0 and inp[i][j] < inp[i][j - 1]:
            count3 = dfs(i, j - 1, count + 1)
        if j < (m - 1) and inp[i][j] < inp[i][j + 1]:
            count4 = dfs(i, j + 1, count + 1)
        cache[i][j] = max(count1, count2, count3, count4, count, 1)
        return cache[i][j]

    for i in range(n):
        for j in range(m):
            output = max(output, dfs(i, j, 0))
    for i in cache:
        print(i)
    return output

inp = [[9, 9, 4],
       [6, 6, 8],
       [2, 1, 1]]

print(longest_increasing_path(inp))
