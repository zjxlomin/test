from collections import deque

def cut(a,b,adj,n):
    p=0
    visited=[False for _ in range(n)]
    deq=deque()
    deq.append(a)
    visited[a-1]=True
    p+=1
    while(len(deq)!=0):
        u=deq.popleft()
        for v in adj[u]:
            if(v==b): continue
            if not visited[v-1]:
                deq.append(v)
                visited[v-1]=True
                p+=1
    q=n-p
    return abs(p-q)

def solution(n, wires):
    answer = -1
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