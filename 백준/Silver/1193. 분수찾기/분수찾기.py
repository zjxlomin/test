n=int(input())
i=1
sum=0
while(True):
    sum+=i
    if(sum>=n): break
    i+=1
k=sum-n
if(i%2==0): print(i-k,1+k,sep='/')
else: print(1+k,i-k,sep='/')