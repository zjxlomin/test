def psum_ij(i,j,psum):
    if(i==1): res=psum[j-1]
    else: res=psum[j-1]-psum[i-2]
    return res

n,m=map(int,input().split())
num_list=[0]*n
psum_list=[0]*n
for i in range(n):
    num_temp=list(map(int,input().split()))
    psum_temp=[0]*m
    psum_temp[0]=num_temp[0]
    for j in range(1,m):
        psum_temp[j]=psum_temp[j-1]+num_temp[j]
    num_list[i]=num_temp
    psum_list[i]=psum_temp
k=int(input())
res=[]
for _ in range(k):
    i,j,x,y=map(int,input().split())
    sum=0
    for p in range(i-1,x):
        sum+=psum_ij(j,y,psum_list[p])
    res.append(sum)
print(*res,sep='\n')