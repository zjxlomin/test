arr=[[]]*10
for i in range(10):
    N=int(input())
    heights=list(map(int,input().split()))
    arr[i]=[N,heights]
i=1
for tmp in arr:
    res=0
    N=tmp[0]
    heights=tmp[1]
    for j in range(2,N-2):
        a=max(heights[j-2],heights[j-1],heights[j+1],heights[j+2])
        if(a<heights[j]): res+=heights[j]-a
    print("#"+str(i),res)
    i+=1