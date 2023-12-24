def dict_and_sort(list,n):
    dict={}
    for i in range(0,n):
        dict[i]=list[i]
    dict_sorted=sorted(dict.items(), key=lambda x:x[1])
    return dict_sorted

n=int(input())

a = list(map(int, input().split()))
a_sorted=dict_and_sort(a,n)
b = list(map(int, input().split()))
b_sorted=dict_and_sort(b,n)

sum=0

for j in range(0,n):
    sum+=a_sorted[n-1-j][1]*b_sorted[j][1]

print(sum)