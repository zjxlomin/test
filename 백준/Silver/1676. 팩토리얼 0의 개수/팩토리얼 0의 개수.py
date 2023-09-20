def fact(n):
  res=1
  for i in range(1,n+1):
    res*=i
  return res

n=int(input())
ftos=list(str(fact(n)))
i=-1
count=0
while(True):
  if(ftos[i]=='0'): 
    count+=1
    i-=1
  else: break
print(count)