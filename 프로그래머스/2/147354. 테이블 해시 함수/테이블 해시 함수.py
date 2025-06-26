def solution(data, col, row_begin, row_end):
    answer = 0
    
    col-=1
    
    temp={}
    for i in range(len(data)):
        k=data[i][col]
        try: 
            temp[k].append(data[i])
            temp[k]=sorted(temp[k],key=lambda x:x[0], reverse=True)
        except:
            temp[k]=[]
            temp[k].append(data[i])
        
    temp=dict(sorted(temp.items(),key=lambda x:x[0]))
    
    new_data=[]
    for a in temp.values():
        new_data.extend(a)
    
    S_i=[]
    for i in range(row_begin-1,row_end):
        temp=new_data[i]
        s=0
        for x in temp:
            s+=x%(i+1)
        S_i.append(s)
    
    for x in S_i:
        answer^=x
    
    return answer