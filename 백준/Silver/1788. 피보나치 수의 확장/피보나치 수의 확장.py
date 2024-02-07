def fibo(n):
    res=[]
    i=0
    while(i<=abs(n)):
        if (i == 0 or i == 1): res.append(i)
        else:
            if(n>0): k=res[1]+res[0]
            else: k=res[0]-res[1]
            if(abs(k)>=1000000000):
                if(k>0): k%=1000000000
                else: k=((-1*k)%1000000000)*(-1)
            res.append(k)
            res.pop(0)
        i+=1
    return res[-1]

n=int(input())
res=fibo(n)
if(res>0): print(1)
elif(res==0): print(0)
else: print(-1)
print(abs(res))