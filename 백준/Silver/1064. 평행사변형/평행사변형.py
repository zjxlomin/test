xa,ya,xb,yb,xc,yc=map(int, input().split())
dxab=xa-xb
dyab=ya-yb
dxbc=xb-xc
dybc=yb-yc
dxac=xa-xc
dyac=ya-yc
if(xa==xb and xb==xc): print(-1)
else:
    if((xa!=xb and xa!=xc and xb!= xc) and dyab/dxab == dybc/dxbc): print(-1)
    else:
        ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** (1 / 2)
        bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** (1 / 2)
        ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** (1 / 2)
        case1 = 2*(ab+ac)
        case2 = 2*(ab+bc)
        case3 = 2*(bc+ac)
        print(max(case1,case2,case3)-min(case1,case2,case3))