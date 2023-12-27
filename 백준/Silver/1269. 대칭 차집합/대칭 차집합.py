aa,bb=map(int,input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))
if(aa>bb): b+=([0]*(aa-bb))
if(aa<bb): a+=([0]*(bb-aa))
ab_dict={}
for x,y in zip(a,b):
    if x in ab_dict: ab_dict[x]+=1
    else: ab_dict[x]=1
    if y in ab_dict: ab_dict[y] += 1
    else: ab_dict[y] = 1
aub=sorted(ab_dict.items(), key=lambda x:x[1])
l=len(aub)
anb=[]
for i in range(0,l):
    if (aub[i][1]!=1 and aub[i][0]!=0): anb.append(aub[i][0])
m=len(anb)
res=aa+bb-2*m
print(res)