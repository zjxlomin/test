N=100
T=10

arr={}
for _ in range(T):
    n=int(input())
    matrix=[[]]*N
    for i in range(N):
        row=list(map(int,input().split()))
        matrix[i]=row
    arr[n]=matrix
for i in range(1,T+1):
    matrix=arr[i]
    start=[i for i, value in enumerate(matrix[0]) if value==1]
    res={}
    for K in start:
        X=K
        L=0
        for j in range(1,N-1):
            L+=1
            if(X>0 and matrix[j][X-1]==1):
                while(True):
                    X-=1
                    L+=1
                    if(X==0 or matrix[j][X-1]==0): break
            elif(X<N-1 and matrix[j][X+1]==1):
                while(True):
                    X+=1
                    L+=1
                    if(X==N-1 or matrix[j][X+1]==0): break
        res[K]=L
    ans=max([k for k,v in res.items() if v==min(res.values())])
    print("#"+str(i),ans)