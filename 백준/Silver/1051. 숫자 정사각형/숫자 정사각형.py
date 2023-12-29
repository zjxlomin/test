n, m = map(int, input().split())
rect = []
for i in range(0, n):
    inp = input()
    arr = list(inp)
    rect.append(arr)
k = min(n, m)  # 10
while (k > 1):
    sq = 0
    p = min(n, m) - k + 1  # 1
    q = max(n, m) - k + 1  # 2
    if (n < m):
        for x in range(0, p):
            for y in range(0, q):
                a = rect[x][y]
                b = rect[x][y + k - 1]
                c = rect[x + k - 1][y]
                d = rect[x + k - 1][y + k - 1]
                if (a == b and b == c and a == d): sq = 1
    else:
        for x in range(0, q):
            for y in range(0, p):
                a = rect[x][y]
                b = rect[x][y + k - 1]
                c = rect[x + k - 1][y]
                d = rect[x + k - 1][y + k - 1]
                if (a == b and b == c and a == d): sq = 1
    if (sq == 1): break
    k -= 1
print(k ** 2)