def non_zero(n):
    while(True):
        if(n%10==0): n//=10
        else: break
    return n
def fact(n):
    res=1
    for i in range(1,n+1):
        i=non_zero(i)
        res*=i
        l=len(str(i))+1
        res=non_zero(res)%(10**l)
    return res%10

n=int(input())
print(fact(n))