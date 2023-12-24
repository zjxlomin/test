import random

n, jm, hs = map(int,input().split())
if(n>=2 and jm<=n and hs<=n and jm!= hs):
    round=1
    met=0
    next_round = {}
    while(n!=1):
        k=1
        for j in range(1,n+1,2):
            if(j==n):
                next_round[k]=j
                if(j==jm): jm=k
                if(j==hs): hs=k
            else:
                if(j==jm or j+1==jm or j==hs or j+1==hs):
                    if((j==jm and j+1==hs) or (j==hs and j+1==jm)): met=1
                    else:
                        if(j==jm or j+1==jm):
                            next_round[k]=jm
                            jm=k
                        if (j == hs or j + 1 == hs):
                            next_round[k] = hs
                            hs=k
                else:
                        next = random.choice([j,j+1])
                        next_round[k]=next
            k+=1
        if(met==1): break
        l=len(next_round)
        for i in range(1,l+1):
            next_round[i]=i
        round+=1
        n=k
    print(round)