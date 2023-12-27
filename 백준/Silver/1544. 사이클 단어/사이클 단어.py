n=int(input())
words=[]
for i in range(0,n):
    word=input()
    words.append(word)
words_exs=[]
words_exs.append(words[0])
for j in range(1,n):
    word=words[j]
    l=len(word)
    for k in range(0,l):
        exs=0
        new_word=word[k:l]+word[0:k]
        if(new_word in words_exs):
            exs=1
            break
        if(k==l-1 and exs==0): words_exs.append(word)
print(len(words_exs))