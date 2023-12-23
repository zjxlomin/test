a,b=map(str, input().split())
m=len(b)

if(len(a)!=len(b)):
    n=len(b)-len(a)
    min=0
    for i in range(0,n+1):
        aa=b[0:i]+a+b[m-(n-i):m]
        count=0
        for j in range(0,m):
            if(aa[j]!=b[j]): count+=1
        if(i==0): min=count
        else:
            if(min>=count): min=count
    print(min)
else:
    count=0
    for i in range(0,m):
        if(a[i]!=b[i]): count+=1
    print(count)