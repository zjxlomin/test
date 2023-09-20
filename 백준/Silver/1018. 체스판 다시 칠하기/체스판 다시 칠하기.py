def reboard(board):
  case1=['W','B']
  case2=['B','W']
  count1=0
  count2=0
  for j in range(0,8):
    for k in range(0,8):
      p=(j+k)%2
      if(board[j][k]!=case1[p]): count1+=1
      if(board[j][k]!=case2[p]): count2+=1
  return min(count1,count2)

n,m=map(int,input().split())
board={}
for i in range(0,n):
  board[i]=list(input())
board=list(board.values())
res={}
i=0
for a in range(0,n-7):
  for b in range(0,m-7):
    newboard=board[a:a+8]
    for j in range(0,8):
      newboard[j]=newboard[j][b:b+8]
    res[i]=reboard(newboard)
    i+=1
print(min(res.values()))