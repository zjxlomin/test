def solution(n, edge):
    adj=[[] for _ in range(n)]
    for temp in edge:
        a=temp[0]
        b=temp[1]
        adj[a-1].append(b)
        adj[b-1].append(a)
    dist={}
    dist[0]=[1]
    visited=[False for _ in range(n)]
    visited[0]=True
    i=0
    while(visited.count(False)!=0):
        for j in dist[i]:
            for e in adj[j-1]:
                if visited[e-1]: continue
                try: dist[i+1].append(e)
                except:
                    dist[i+1]=[]
                    dist[i+1].append(e)
                visited[e-1]=True
        i+=1
    res=[v for k,v in dist.items() if k==max(dist.keys())][0]
    answer = len(res)
    return answer