n=int(input())
serial= {}
res=[]
for _ in range(0,n):
    x=input()
    serial[x]=len(x)
serial=sorted(serial.items(), key=lambda x:x[1])
comp={}
for i in range(0,n):
    x=serial[i][1]
    y=serial[i][0]
    if(x in comp.keys()): comp[x].append(y)
    else: comp[x]=[y]
k=list(comp.keys())
for j in range(0,len(comp)):
    arr=comp[k[j]]
    arr_sort=[]
    if(len(arr)==1): arr_sort.append(arr)
    else:
        t={}
        for p in range(0,len(arr)):
            x=0
            for q in range(0,k[j]):
                try: x+=int(arr[p][q])
                except: x+=0
            if(x in t.keys()):
                t[x].append(arr[p])
                t[x]=sorted(t[x])
            else: t[x]=[arr[p]]
        t=dict(sorted(t.items()))
        arr_sort=list(t.values())
    for a in range(0,len(arr_sort)):
        if(len(arr_sort[a])==1): res.append(arr_sort[a][0])
        else:
            for b in range(0,len(arr_sort[a])): res.append(arr_sort[a][b])
for i in range(0,len(res)): print(res[i])