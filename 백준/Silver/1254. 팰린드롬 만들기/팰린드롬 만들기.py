word = input()
word=list(word)
l=len(word)
rev_word=list(word)[::-1]
i=l
while(i>0):
    if(word[l-i:l]==rev_word[:i]): break
    i-=1
res=2*l-i
print(res)