def solution(n, l, r):
    K=['1']
    
    L=l-1
    R=r-1
    
    cut={}
    cut[0]=[0,0]
    
    for i in range(n,0,-1):
        L=L//5
        R=R//5
        cut[i]=[L,R]
        
    for i in range(n):
        a=cut[i+1][0]-(cut[i][0]*5)
        b=cut[i+1][1]-(cut[i][0]*5)
        K=K[a:b+1]
        for j in range(a,b+1):
            j-=a
            if(int(K[j])==0): K[j]='00000'
            if(int(K[j])==1): K[j]='11011'
        K=list(''.join(K))
    
    answer = K[l-1-(cut[n][0]*5) : r-(cut[n][0]*5)].count('1')
    return answer