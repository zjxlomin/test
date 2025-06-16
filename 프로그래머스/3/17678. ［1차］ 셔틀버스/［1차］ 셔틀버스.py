# t분 형태로 변환
def t_form(s):
    h=int(s[0:2])
    m=int(s[3:5])
    return 60*h+m

# "hh:mm" 형태로 변환
def s_form(t):
    h=str(t//60)
    m=str(t%60)
    return h.zfill(2) + ":" + m.zfill(2)

def solution(n, t, m, timetable):
    answer=''
    
    timetable=sorted(timetable)
    
    for i in range(len(timetable)):
        timetable[i]=t_form(timetable[i])
    # print("timetable:",timetable)
    
    shuttles=[]
    first=540
    shuttles.append(first)
    for i in range(n-1):
        first+=t
        shuttles.append(first)
    # print("shuttles:",shuttles)
    last=shuttles[-1]
    
    # 막차 못타는 크루 귀가
    timetable=[t for t in timetable if t<=last]
    
    res=[]
    
    for i in range(n):
        this_shuttle=shuttles[i]
        can_ride=[t for t in timetable if t<=this_shuttle] # 지금 셔틀 이전에 줄서있던 사람
        if(len(can_ride)>m): 
            can_ride=can_ride[:m]
        timetable=timetable[len(can_ride):]
        try: F=can_ride[0]
        except: F=[]
        try: L=can_ride[-1]
        except: L=[]
        if(i==n-1):
            if(len(can_ride)<m): # 내가 탈 자리가 남은경우
                res=this_shuttle
            else: 
                if(can_ride.count(F)==m):
                    res=F-1
                else: 
                    res=L-1
    
    answer=s_form(res)
    return answer
