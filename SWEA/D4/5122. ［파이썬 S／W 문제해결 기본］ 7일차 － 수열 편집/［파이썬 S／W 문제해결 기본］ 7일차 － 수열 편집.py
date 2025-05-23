T=int(input())
test={}
for i in range(1,T+1):
    N,M,L=map(int,input().split())
    arr=list(map(int,input().split()))
    for _ in range(M):
        cmd=list(map(str,input().split()))
        cmd_type=cmd[0]
        a=int(cmd[1])
        if(cmd_type=="I"):
            b=int(cmd[2])
            arr.insert(a,b)
        if(cmd_type=="D"):
            arr.pop(a)
        if(cmd_type=="C"):
            b=int(cmd[2])
            arr[a]=b
    try: test[i]=arr[L]
    except: test[i]=-1
for i in range(1,T+1):
    print("#"+str(i),test[i])