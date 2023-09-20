e,s,m=map(int,input().split())
year=1
while(True):
  if((year%15==e or (e%15==0 and year%15==0)) and (year%28==s or (s%28==0 and year%28==0)) and (year%19==m or (m%19==0 and year%19==0))): break
  year+=1
print(year)