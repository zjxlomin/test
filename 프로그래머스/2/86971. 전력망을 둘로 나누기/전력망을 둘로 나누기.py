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
        linked[a]=len(adj[a])
        try: adj[b].append(a)
        except:
            adj[b]=[]
            adj[b].append(a)
        linked[b]=len(adj[b])
    """
    linked=sorted(linked.items(),key=lambda x:x[1],reverse=True)
    cand={1:[],2:[]}
    fst=0
    snd=0
    for temp in linked:
        if(temp[1]>=fst):
            fst=temp[1]
            cand[1].append(temp[0])
            if(len(cand[1])==2): break
        elif(temp[1]>=snd):
            snd=temp[1]
            cand[2].append(temp[0])
        else: break
    
    if(len(cand[1])==2):
        a=cand[1][0]
        b=cand[1][1]
        answer=cut(a,b,adj,n)
    else:
        res=[]
        a=cand[1][0]
        for b in cand[2]:
            res.append(cut(a,b,adj,n))
        answer=min(res)
    """
    res=[]
    for temp in wires:
        a=temp[0]
        b=temp[1]
        res.append(cut(a,b,adj,n))
    answer=min(res)
    
    return answer