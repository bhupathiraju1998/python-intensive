word = input()
new_word = word.lower()
len_word = len(word)
sum =""
for i in range(1,len_word+1):
    result = len_word-i
    d = word[result]
    sum = sum + d
    new = sum.lower()
if new == new_word:
    print("Palindrome")
else:
    print("Not a Palindrome")




