n=int(input())
sold_list=[]
for i in range(0,n):
    title=input()
    sold_list.append(title)
sold_dict={}
for t in sold_list:
    if t in sold_dict: sold_dict[t]+=1
    else: sold_dict[t]=1
m=max(list(sold_dict.values()))
res=sorted([k for k, v in sold_dict.items() if v == m])
print(res[0])