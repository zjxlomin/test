def res(N,L):
    fin=0
    while(L<=100):
        a=N//L
        res=[a]
        i=0
        while(sum(res)<=N and i+2<=L):
            j=i//2+1
            if(i%2==0): res.append(a+j)
            else: res.append(a-j)
            if(sum(res)==N and i+2==L): 
                fin=1
                break
            if(a-j<0): break
            i+=1
        if(fin==1): break
        else: L+=1
    if(fin==1): return sorted(res)
    else: return [-1]

N,L=map(int,input().split())
print(*res(N,L),sep=' ',end='')