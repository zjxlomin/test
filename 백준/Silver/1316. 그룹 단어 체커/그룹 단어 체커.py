def plusone(arr2):
  arr=list(arr2)
  l=len(arr)
  if(arr[-1]-arr[0]==l-1): return True
  else: return False
    
def checkword(word):
  letters=list(set(word))
  l=len(letters)
  m=len(word)
  point={}
  for i in range(0,l):
    point[letters[i]]={}
  for j in range(0,m):
    point[word[j]][j]=j
  res=1
  for k in range(0,l):
    if(plusone(point[letters[k]])==False): res=0
  return res

n=int(input())
check={}
for i in range(0,n):
  word=input()
  check[i]=checkword(word)
check2=list(check.values())
print(check2.count(1))