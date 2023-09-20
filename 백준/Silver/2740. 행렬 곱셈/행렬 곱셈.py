an,am=map(int,input().split())
a={}
for i in range(0,an):
  a[i]=list(map(int,input().split()))
bm,bk=map(int,input().split())
b={}
for j in range(0,bm):
  b[j]=list(map(int,input().split()))
cn=an
ck=bk
for i in range(0,cn):
  for j in range(0,ck):
    res=0
    for x in range(0,am):
      res+=a[i][x]*b[x][j]
    if(j==ck-1): print(res)
    else: print(res,end=' ')