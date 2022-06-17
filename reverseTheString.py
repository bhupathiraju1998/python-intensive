word = input()
len_word = len(word)
sum =""
for i in range(1,len_word+1):
    result = len_word-i
    d = word[result]
    sum = sum + d
print(sum)
