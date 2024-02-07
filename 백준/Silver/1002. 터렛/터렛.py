n=int(input())
test=[]
for _ in range(0,n):
    l=list(map(int, input().split()))
    test.append(l)
for i in range(0,n):
    l=test[i]
    x1 = l[0]
    y1 = l[1]
    r1 = l[2]
    x2 = l[3]
    y2 = l[4]
    r2 = l[5]
    c=((x2-x1)**2+(y2-y1)**2)**(1/2)
    a=max(r1,r2)
    b=min(r1,r2)
    if (c == 0 and a == b): print(-1)
    else:
        if(a+b>c):
            if(a-b<c): print(2)
            elif(a-b==c): print(1)
            elif(a-b>c): print(0)
        elif(a+b==c): print(1)
        elif(a+b<c): print(0)
