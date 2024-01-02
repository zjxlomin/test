name = input()
res = ''
name = list(name)
n = len(name)
let = {}
for i in range(0, n):
    x = name[i]
    if (x in let):
        let[x] += 1
    else:
        let[x] = 1
let = dict(sorted(let.items()))
k = list(let.keys())
v = list(let.values())
l = len(let)
odd = []
for j in range(0, l):
    if (v[j] % 2 == 1):
        odd.append(k[j])
        let[k[j]] -= 1
    if (len(odd) > 1):
        print("I'm Sorry Hansoo")
        break
if (len(odd) <= 1):
    res2 = ''
    for p in range(0, l):
        res2 += k[p] * int(v[p] / 2)
    res += res2
    if (len(odd) == 1): res += odd[0]
    res += res2[::-1]
print(res)