word_list=[]
while(True):
    word=input()
    if(word=='*'):
        break
    else: word_list.append(word)
for word in word_list:
    if(len(word)==1): print(word,"is surprising.")
    else:
        res={}
        d=1
        while(d<len(word)):
            temp=[]
            for i in range(0,len(word)-d):
                temp.append(word[i]+word[i+d])
            res[d-1]=temp
            d+=1
        sur=0
        for key in res:
            a=sorted(res[key])
            b=sorted(list(set(a)))
            if(a!=b):
                sur=1
                break
        if(sur==0): print(word,"is surprising.")
        else: print(word,"is NOT surprising.")