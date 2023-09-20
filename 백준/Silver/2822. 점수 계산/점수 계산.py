score={}
for i in range(1,9):
  score[i]=int(input())
score=dict(sorted(score.items(),key=lambda x:(-x[1])))
score2=list(score.values())
sum=0
for j in range(0,5):
  sum+=score2[j]
print(sum)
score3=sorted(list(score.keys())[0:5])
print(*score3)