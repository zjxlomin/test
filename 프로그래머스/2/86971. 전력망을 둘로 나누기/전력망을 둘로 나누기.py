def cut(a,b,adj,n):
    p=0
    visited=[False for _ in range(n)]
    stack=[]
    stack.append(a)
    while(len(stack)!=0):
        u=stack.pop(-1)
        if not visited[u-1]: 
            visited[u-1]=True
            p+=1
        for v in adj[u]:
            if(v==b): continue
            if not visited[v-1]:
                stack.append(v)
    q=n-p
    return abs(p-q)

def solution(n, wires):
    adj={}
    linked={}
    for temp in wires:
        a=temp[0]
        b=temp[1]
        try: adj[a].append(b)
        except:
            adj[a]=[]
            adj[a].append(b)
        try: adj[b].append(a)
        except:
            adj[b]=[]
            adj[b].append(a)
    
    res=[]
    for temp in wires:
        a=temp[0]
        b=temp[1]
        res.append(cut(a,b,adj,n))
    answer=min(res)
    
    return answer