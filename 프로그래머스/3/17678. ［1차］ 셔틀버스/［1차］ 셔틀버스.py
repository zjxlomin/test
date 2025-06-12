# [시,분] 형태로 변환
def t_form(s):
    h=int(s[0:2])
    m=int(s[3:5])
    return [h,m]

# string 형태로 변환
def s_form(t):
    h=str(t[0])
    m=str(t[1])
    return h.zfill(2) + ":" + m.zfill(2)

# t분 추가
def min_add(time,t):
    h=time[0]
    m=time[1]
    m+=t
    if(m>=60):
        h+=m//60
        m%=60
    if(m<0):
        h-=(-1*m)//60+1
        m=60-((-1*m)%60)
    return [h,m]

# a가 b보다 이르거나 같은지
def early(a,b):
    h1=a[0]
    m1=a[1]
    h2=b[0]
    m2=b[1]
    if(h1<h2): return True
    elif(h1==h2 and m1<=m2): return True
    else: return False

def solution(n, t, m, timetable):
    answer=''
    
    timetable=sorted(timetable)
    
    for i in range(len(timetable)):
        timetable[i]=t_form(timetable[i])
    # print("timetable:",timetable)
    
    shuttles=[]
    first=[9,0]
    shuttles.append(first)
    for i in range(n-1):
        first=min_add(first,t)
        shuttles.append(first)
    # print("shuttles:",shuttles)
    last=shuttles[-1]
    
    # 막차 못타는 크루 귀가
    timetable=[t for t in timetable if early(t,last)]
    
    board={}
    res=[]
    
    for i in range(n):
        this_shuttle=shuttles[i]
        can_ride=[t for t in timetable if early(t,this_shuttle)] # 지금 셔틀 이전에 줄서있던 사람
        if(len(can_ride)>m): 
            can_ride=can_ride[:m]
        # print("can ride:",can_ride)
        timetable=timetable[len(can_ride):]
        board[i]=can_ride
        try: F=can_ride[0]
        except: F=[]
        try: L=can_ride[-1]
        except: L=[]
        if(i==n-1):
            if(len(can_ride)<m): # 내가 탈 자리가 남은경우
                res=this_shuttle
            else: 
                if(can_ride.count(F)==m):
                    res=min_add(F,-1)
                else: 
                    res=min_add(L,-1)
    
    answer=s_form(res)
    return answer