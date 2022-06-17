word = input()
word = word.lower()
leng = len(word)
vowel_count = 0
consonants_count = 0
space_count = 0
for each in word:
    
    if each == "a" or each == "e" or each == "i" or each == "o" or each =="u":
        vowel_count += 1 
    elif each == " ":
        space_count += 1 
        
 
print(vowel_count)
print((leng - space_count)-vowel_count)