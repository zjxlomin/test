from math import prod

s,k=map(int, input().split())
a=s//k
b=s%k
arr=[]
if(b==0):
    tmp=[]
    for i in range(0,k): tmp.append(a)
    res=prod(tmp)
    arr.append(res)
else:
    for i in range(1,b+1):
        tmp=[]
        tmp.append(a+b-i+1)
        for m in range(0,i-1): tmp.append(a+1)
        for h in range(i,k): tmp.append(a)
        res=prod(tmp)
        arr.append(res)
print(max(arr))