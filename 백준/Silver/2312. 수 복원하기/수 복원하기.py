def prime(n):
    res=[]
    i=2
    res.append(i)
    i+=1
    while(i<=n):
        for j in res:
            k=0
            if(i%j==0):
                k=1
                break
        if(k==0): res.append(i)
        i+=1
    return res

cases=int(input())
n_list=[]
for _ in range(0,cases):
    n=int(input())
    n_list.append(n)
prime_list=prime(max(n_list))
for n in n_list:
    res={}
    for p in prime_list:
        if(p<=n):
            i=0
            while(True):
                if(n%p!=0): break
                else:
                    n//=p
                    i+=1
            if(i>0): res[p]=i
    for key in res:
        print(key,res[key])