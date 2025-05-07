from collections import deque

n=int(input())
m=int(input())
adj=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)
visited=[False] * n
queue=deque()
queue.append(0)
visited[0]=True
while(len(queue)!=0):
    u=queue.popleft()
    for i in adj[u]:
        if not visited[i]:
            queue.append(i)
            visited[i]=True
res=0
for i in range(1, n):
    if visited[i]: res+=1
print(res)