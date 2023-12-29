def fibo(n):
    t=n+1
    res=[]
    for i in range(0,t):
        if(i==0): res.append(0)
        else:
            if(i==1): res.append(1)
            else: res.append(res[i-1]+res[i-2])
    return res[n]

t=int(input())
res=[]
for i in range(0,t):
    n=int(input())
    if(n==0): z=1
    else: z=fibo(n-1)
    o=fibo(n)
    res.append([z,o])
for j in range(0,t):
    print(res[j][0],res[j][1])