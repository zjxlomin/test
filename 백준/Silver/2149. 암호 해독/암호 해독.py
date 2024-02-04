class dup(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def __repr__(self):
        return "'"+self.name+"'"

key_input=input()
code=input()
tmp={}

key_input=list(key_input)
key_sorted=sorted(key_input)
n=len(key_input)
l=len(code)
key_dict={}
for h in range(0,n):
    key_dict[h]=key_input[h]
for i in range(0,n):
    tmp[i]=[]
for j in range(0,l):
    k=int(j/(l/n))
    tmp[k].append(code[j])
chart={}
for p in range(0,n):
    chart[dup(key_sorted[p])]=tmp[p]

orig={}
for key in chart:
    t=[k for k, v in key_dict.items() if v == str(key)]
    if(len(t)>1):
        # key 인 value들을 추출하여 tmp
        tmp=chart.get(key)
        for q in range(0,len(t)):
            if(t[q] not in orig):
                orig[t[q]]=tmp
                break
    else: orig[t[0]]=chart[key]
orig=sorted(orig.items())
res=''
for a in range(0,int(l/n)):
    for b in range(0,n):
        res+=orig[b][1][a]
print(res)