n=int(input())
res={}
for i in range(0,n):
  cntry,n,score=map(int,input().split())
  res[score]=[cntry,n]
res=sorted(res.items(),reverse=True)
j=0
l=0
c={}
while(l<3):
  p=res[j][1][0]
  c[j]=p
  k=list(c.values())
  if(k.count(p)<3):
    print(res[j][1][0],res[j][1][1])
    l+=1
  j+=1