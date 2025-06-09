from collections import deque

N,M,V=map(int,input().split())
adj=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    adj[a-1].append(b)
    adj[b-1].append(a)
    adj[a-1]=sorted(adj[a-1],reverse=True)
    adj[b-1]=sorted(adj[b-1],reverse=True)

bfs=[]
dfs=[]

visited=[False for _ in range(N)]
stack=[]
stack.append(V)
while(len(stack)!=0):
    u=stack.pop(-1)
    if not visited[u-1]:
        visited[u-1]=True
        dfs.append(u)
    for v in adj[u-1]:
        if not visited[v-1]:
            stack.append(v)

for i in range(N):
    adj[i]=sorted(adj[i])

visited=[False for _ in range(N)]
deq=deque()
deq.append(V)
visited[V-1]=True
bfs.append(V)
while(len(deq)!=0):
    u=deq.popleft()
    for v in adj[u-1]:
        if not visited[v-1]:
            deq.append(v)
            visited[v-1]=True
            bfs.append(v)

print(*dfs,sep=' ')
print(*bfs,sep=' ')