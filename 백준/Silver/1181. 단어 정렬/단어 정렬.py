n=int(input())
word_list={}
for i in range(0,n):
    word=input()
    x=word in word_list
    if(x == False):
        l=len(word)
        word_list[word]=l
m=len(word_list)
w2=sorted(word_list.items(), key=lambda x: x[1])
w2.sort(key=lambda x:(x[1],x[0]))
w3=[x[0] for x in w2]
for i in range(0,m):
    print(w3[i])