def isleap(y):
  if(y%4==0):
    if(y%400==0): return True
    elif(y%100==0): return False
    else: return True
  else: return False

notleap={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
leap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
ty,tm,td=map(int,input().split())
dy,dm,dd=map(int,input().split())
if((dy-ty==1000 and dm==tm and dd>=td) or (dy-ty==1000 and dm>tm) or (dy-ty>1000)): 
  print("gg")
else:
  d_day=0
  years=dy-ty
  if(years>=2):
    ty2=ty+1
    for i in range(0,years-1):
      if(isleap(ty2)==True): d_day+=366
      else: d_day+=365
      ty2+=1
  if(years==0):
    for m in range(tm,dm+1):
      if(isleap(ty)==True):
        if(m==tm): d_day+=leap[m]-td
        elif(m==dm): d_day+=dd
        else: d_day+=leap[m]
      else:
        if(m==tm): d_day+=notleap[m]-td
        elif(m==dm): d_day+=dd
        else: d_day+=notleap[m]
  else:
    for j in range(tm,13):
      if(isleap(ty)==True): 
        if(j==tm): d_day+=leap[j]-td
        else: d_day+=leap[j]
      else: 
        if(j==tm): d_day+=notleap[j]-td
        else: d_day+=notleap[j]
    for k in range(1,dm+1):
      if(isleap(dy)==True): 
        if(k==dm): d_day+=dd
        else: d_day+=leap[k]
      else: 
        if(k==dm): d_day+=dd
        else: d_day+=notleap[k]
  print("D-",d_day,sep='')