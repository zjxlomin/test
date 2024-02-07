x,y=map(int,input().split())
z=y*100/x
if(y>=0.99*x): print(-1)
else:
    k=((int(z)+1)*x - 100*y)/(99-int(z))
    if(k>int(k)): k=int(k)+1
    print(int(k))

# z = (y/x)*100 = z'+a, z'=int(z), a = 0.xxx...
# z'+1 <= ((y+k)/(x+k))*100
# k>= ((z'+1)*x - 100*y)/(99-z')