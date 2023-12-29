aa,bb=map(int,input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))
if(aa>bb): b+=([0]*(aa-bb))
if(aa<bb): a+=([0]*(bb-aa))
ab_dict={}
for x,y in zip(a,b):
    if x in ab_dict: ab_dict[x] += 1
    else:
        if(x!=0): ab_dict[x]=1
    if y in ab_dict: ab_dict[y] += 1
    else:
        if(y!=0): ab_dict[y] = 1
res=[]
for i in range(0,aa):
    m=a[i]
    if(ab_dict[m]==1): res.append(m)
res=sorted(res)
k=len(res)
print(k)
if(k>0):
    for j in range(0,k): print(res[j],end=' ')