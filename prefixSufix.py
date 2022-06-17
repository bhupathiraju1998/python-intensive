word_1 = input()
leng_word_1 = len(word_1)

word_2 = input()
leng_word_2 = len(word_2)
new_string = ""

for each in range(1,leng_word_1+1):
    suffix = word_1[-each:]
    
    for item in range(0,leng_word_2):
        prefix = word_2[:item]
        if suffix == prefix:
            new_string += suffix
            break
        continue
    
   
if len(new_string) > 0:
    print(new_string)
else:
    print("No overlapping")
  
    