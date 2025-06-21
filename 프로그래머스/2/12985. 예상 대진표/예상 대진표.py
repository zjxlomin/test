def solution(n,a,b):
    answer = 1
    a-=1
    b-=1
    while(n!=2): 
        if((a-b==1 and a//2==b//2) or (b-a==1 and b//2==a//2)): break
        a=a//2
        b=b//2
        n=n//2
        answer+=1
    return answer