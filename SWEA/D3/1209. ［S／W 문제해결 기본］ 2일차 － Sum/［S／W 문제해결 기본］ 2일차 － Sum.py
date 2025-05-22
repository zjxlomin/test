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
    res=[]
    row=0
    col=0
    for a in range(N):
        for b in range(N):
            row+=matrix[a][b]
            col+=matrix[b][a]
        res.append(row)
        res.append(col)
        row=0
        col=0
    diag1=0
    diag2=0
    for a in range(N):
        diag1+=matrix[a][a]
        diag2+=matrix[a][N-1-a]
    res.append(diag1)
    res.append(diag2)
    print("#"+str(i),max(res))