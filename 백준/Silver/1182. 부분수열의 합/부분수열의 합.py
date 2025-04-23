from itertools import combinations

def res(arr,s):
    combs=[]
    count=0
    for i in range(1,len(arr)+1):
        combs+=list(combinations(arr,i))
    for temp in combs:
        if(sum(temp)==s): 
            count+=1
    return count

n,s=map(int,input().split())
arr=list(map(int, input().split()))
print(res(arr,s))