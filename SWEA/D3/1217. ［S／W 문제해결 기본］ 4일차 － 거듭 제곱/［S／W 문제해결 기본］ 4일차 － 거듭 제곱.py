def square(a,b):
    if(b==1): return a
    else: return a*square(a,b-1)

T=10

arr={}
for _ in range(T):
    N=int(input())
    n,m=map(int,input().split())
    arr[N]=[n,m]
for i in range(1,T+1):
    print("#"+str(i), square(arr[i][0],arr[i][1]))