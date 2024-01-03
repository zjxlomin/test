x,y,w,s=map(int,input().split())
d=min(x,y)
p=max(x,y)
t=0
if(2*w>s): t+=d*s
else: t+=2*d*w
if(w>s):
    if((p-d)%2==1): t+=s*(p-d-1)+w
    else: t+=s*(p-d)
else: t+=(p-d)*w
print(t)