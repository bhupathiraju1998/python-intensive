word = input()
length = len(word)
letters = (length - 4 ) * "*"
word1 = word[:2]
word2 = word[length-2:]
print(word1+letters+word2)