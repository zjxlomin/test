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
    X=matrix[N-1].index(2)
    for j in range(N-2,0,-1):
        if(X>0 and matrix[j][X-1]==1):
            while(True):
                X-=1
                if(X==0 or matrix[j][X-1]==0): break
        elif(X<N-1 and matrix[j][X+1]==1):
            while(True):
                X+=1
                if(X==N-1 or matrix[j][X+1]==0): break
    print("#"+str(i),X)