word=input()
l=len(word)
res={}
for i in range(1,l-1):
  first=word[:i]
  for j in range(i,l-1):
    second=word[i:j+1]
    third=word[j+1:]
    a=first[::-1]
    b=second[::-1]
    c=third[::-1]
    res[a+b+c]=1
res2=sorted(res)
print(res2[0])