def make_filter(first):
    filter=[]
    for i in range(0,5):
        filter.append(first+i)
    return filter

n=int(input())
nlist=[]
for i in range(0,n):
    a=int(input())
    nlist.append(a)
nlist=sorted(nlist)

tmp=[]

for j in range(0,n):
    count=0
    filter=make_filter(nlist[j])
    for k in range(0,5):
        if(filter[k] in nlist): count+=1
    tmp.append(count)
res=5-max(tmp)
print(res)