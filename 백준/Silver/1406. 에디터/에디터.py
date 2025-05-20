from collections import deque
import sys

arr=sys.stdin.readline().strip()
deq_left=deque(arr)
deq_right=deque()
n=int(sys.stdin.readline())
for _ in range(n):
    cmd=sys.stdin.readline().strip()
    if(cmd=="L"):
        try: 
            x=deq_left.pop()
            deq_right.appendleft(x)
        except: True
    if(cmd=="D"):
        try: 
            x=deq_right.popleft()
            deq_left.append(x)
        except: True
    if(cmd=="B"):
        try: deq_left.pop()
        except: True
    if(cmd[0]=="P"):
        x=cmd[-1]
        deq_left.append(x)
res=list(deq_left+deq_right)
print(*res,sep='')