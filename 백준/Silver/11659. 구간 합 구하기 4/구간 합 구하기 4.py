n,m=map(int,input().split())
arr=list(map(int,input().split()))
psum=[0]*n
psum[0]=arr[0]
for i in range(1,n):
    psum[i]=psum[i-1]+arr[i]
res=[]
for k in range(m):
    i,j=map(int,input().split())
    if(i==1): temp=psum[j-1]
    else: temp=psum[j-1]-psum[i-2]
    res.append(temp)
print(*res,sep='\n')