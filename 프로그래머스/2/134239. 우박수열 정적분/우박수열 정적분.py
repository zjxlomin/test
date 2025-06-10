def solution(k, ranges):
    answer = []
    hail=[]
    S=[]
    hail.append(k)
    i=0
    while(k>1):
        if(k%2==0): k=k//2
        else: k=k*3+1
        hail.append(k)
        i+=1
        S.append((hail[i]+hail[i-1])/2)
    
    for range in ranges:
        a=range[0]
        b=range[1]
        if(a==0 and b==0): x=sum(S)
        else:
            b=i+b
            if(a>b): x=-1
            elif(a==b): x=0
            else:
                x=sum(S[a:b])
        answer.append(x)
        
    return answer