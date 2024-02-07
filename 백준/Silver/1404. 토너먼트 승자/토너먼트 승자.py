def avsb(rates):
    for i in range(0,28):
        rates[i]/=100
    vs={}
    vs['0_1']=rates[0]
    vs['1_0']=1-rates[0]
    vs['0_2']=rates[1]
    vs['2_0']=1-rates[1]
    vs['0_3']=rates[2]
    vs['3_0']=1-rates[2]
    vs['0_4']=rates[3]
    vs['4_0']=1-rates[3]
    vs['0_5']=rates[4]
    vs['5_0']=1-rates[4]
    vs['0_6']=rates[5]
    vs['6_0'] = 1 - rates[5]
    vs['0_7']=rates[6]
    vs['7_0'] = 1 - rates[6]
    vs['1_2']=rates[7]
    vs['2_1'] = 1 - rates[7]
    vs['1_3']=rates[8]
    vs['3_1'] = 1 - rates[8]
    vs['1_4']=rates[9]
    vs['4_1'] = 1 - rates[9]
    vs['1_5']=rates[10]
    vs['5_1'] = 1 - rates[10]
    vs['1_6']=rates[11]
    vs['6_1'] = 1 - rates[11]
    vs['1_7']=rates[12]
    vs['7_1'] = 1 - rates[12]
    vs['2_3']=rates[13]
    vs['3_2'] = 1 - rates[13]
    vs['2_4']=rates[14]
    vs['4_2'] = 1 - rates[14]
    vs['2_5']=rates[15]
    vs['5_2'] = 1 - rates[15]
    vs['2_6']=rates[16]
    vs['6_2'] = 1 - rates[16]
    vs['2_7']=rates[17]
    vs['7_2'] = 1 - rates[17]
    vs['3_4']=rates[18]
    vs['4_3'] = 1 - rates[18]
    vs['3_5']=rates[19]
    vs['5_3'] = 1 - rates[19]
    vs['3_6']=rates[20]
    vs['6_3'] = 1 - rates[20]
    vs['3_7']=rates[21]
    vs['7_3'] = 1 - rates[21]
    vs['4_5']=rates[22]
    vs['5_4'] = 1 - rates[22]
    vs['4_6']=rates[23]
    vs['6_4'] = 1 - rates[23]
    vs['4_7']=rates[24]
    vs['7_4'] = 1 - rates[24]
    vs['5_6']=rates[25]
    vs['6_5'] = 1 - rates[25]
    vs['5_7']=rates[26]
    vs['7_5'] = 1 - rates[26]
    vs['6_7']=rates[27]
    vs['7_6'] = 1 - rates[27]
    return vs

rates=list(map(int, input().split()))
vs=avsb(rates)

semifinal=vs
final={}
win={}

final[0]=semifinal['0_1'] * (semifinal['2_3'] * vs['0_2'] + semifinal['3_2'] * vs['0_3'])
final[1]=semifinal['1_0'] * (semifinal['2_3'] * vs['1_2'] + semifinal['3_2'] * vs['1_3'])
final[2]=semifinal['2_3'] * (semifinal['0_1'] * vs['2_0'] + semifinal['1_0'] * vs['2_1'])
final[3]=semifinal['3_2'] * (semifinal['0_1'] * vs['3_0'] + semifinal['1_0'] * vs['3_1'])
final[4]=semifinal['4_5'] * (semifinal['6_7'] * vs['4_6'] + semifinal['7_6'] * vs['4_7'])
final[5]=semifinal['5_4'] * (semifinal['6_7'] * vs['5_6'] + semifinal['7_6'] * vs['5_7'])
final[6]=semifinal['6_7'] * (semifinal['4_5'] * vs['6_4'] + semifinal['5_4'] * vs['6_5'])
final[7]=semifinal['7_6'] * (semifinal['4_5'] * vs['7_4'] + semifinal['5_4'] * vs['7_5'])

win[0]=final[0]*(final[4]*vs['0_4']+final[5]*vs['0_5']+final[6]*vs['0_6']+final[7]*vs['0_7'])
win[1]=final[1]*(final[4]*vs['1_4']+final[5]*vs['1_5']+final[6]*vs['1_6']+final[7]*vs['1_7'])
win[2]=final[2]*(final[4]*vs['2_4']+final[5]*vs['2_5']+final[6]*vs['2_6']+final[7]*vs['2_7'])
win[3]=final[3]*(final[4]*vs['3_4']+final[5]*vs['3_5']+final[6]*vs['3_6']+final[7]*vs['3_7'])
win[4]=final[4]*(final[0]*vs['4_0']+final[1]*vs['4_1']+final[2]*vs['4_2']+final[3]*vs['4_3'])
win[5]=final[5]*(final[0]*vs['5_0']+final[1]*vs['5_1']+final[2]*vs['5_2']+final[3]*vs['5_3'])
win[6]=final[6]*(final[0]*vs['6_0']+final[1]*vs['6_1']+final[2]*vs['6_2']+final[3]*vs['6_3'])
win[7]=final[7]*(final[0]*vs['7_0']+final[1]*vs['7_1']+final[2]*vs['7_2']+final[3]*vs['7_3'])

for i in range(0,8):
    res=win[i]
    if(res==int(res)): print(res, end=' ')
    else:
        res=float("{:.13f}".format(win[i]))
        print(res, end=' ')