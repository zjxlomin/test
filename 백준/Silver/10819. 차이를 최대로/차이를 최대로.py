from itertools import permutations

n=int(input())
a=list(map(int,input().split()))
perms=list(permutations(a,n))
res=0
for arr in perms:
    L=len(arr)
    temp=0
    for i in range(1,L):
        temp+=abs(arr[i]-arr[i-1])
    if(temp>=res): 
        res=temp
print(res)