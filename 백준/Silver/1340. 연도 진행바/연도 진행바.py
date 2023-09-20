def isleap(y):
  if(y%4==0):
    if(y%400==0): return True
    elif(y%100==0): return False
    else: return True
  else: return False

notleap={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
leap={'January':31,'February':29,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
mton={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
ntom={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
m,d,y,t=input().split()
month=m
day=int(d[:-1])
year=int(y)
hour=int(t[:2])
min=int(t[3:])
res=0
if(isleap(year)==True): total=366*24*60
else: total=365*24*60
for i in range(1,mton[month]+1):
  if(i==mton[month]): res+=day-1
  else:
    if(isleap(year)==True): res+=leap[ntom[i]]
    else: res+=notleap[ntom[i]]
res*=24*60
res+=hour*60+min
print((res/total)*100)