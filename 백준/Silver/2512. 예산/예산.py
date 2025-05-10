import math

n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr,reverse=True)
m=int(input())
res=max(arr)
s=sum(arr)
i=arr.count(max(arr))
pdiff=[0]*(n-1)
for j in range(n-1):
    pdiff[j]=arr[j]-arr[j+1]
while s > m:
    if i - 1 >= len(pdiff):
        x = math.ceil((s - m) / i)
        res -= x
        break
    p = pdiff[i - 1]
    if s - p * i >= m:
        s -= p * i
        res -= p
    else:
        x = math.ceil((s - m) / i)
        res -= x
        break
    i += 1
print(res)