n=list(input())
i=0
while(len(n)!=1):
  l=len(n)
  for j in range(0,l):
    n[j]=int(n[j])
  k=sum(n)
  k2=str(k)
  n=list(k2)
  i+=1
print(i)
n2=int(n[0])
if(n2%3==0): print("YES")
else: print("NO")