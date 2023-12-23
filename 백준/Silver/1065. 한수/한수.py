n=int(input())
count=0
for x in range(1,n+1):
    xx=str(x)
    xx_len=len(xx)
    if(xx_len==1 or xx_len==2): count+=1
    else:
        d=int(xx[1])-int(xx[0])
        k=0
        for j in range(1,xx_len-1):
            if(int(xx[j+1])-int(xx[j])!=d):
                k=1
                break
        if(k==0): count+=1
print(count)