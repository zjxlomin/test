n = int(input())
i = 0
len = 0
while (n >= 10 ** i):
    a = 10 ** i
    b = 10 ** (i + 1) - 1
    t = b - a + 1
    if (n > b):
        len += (i + 1) * t
    else:
        k = b - n
        len += (i + 1) * (t - k)
    i += 1
print(len)