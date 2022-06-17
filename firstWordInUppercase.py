word = input()
first_word_end_index = 0
for each in word:
    if each == " " :
        break 
    else:
        first_word_end_index = first_word_end_index + 1 


first_word = word[0:first_word_end_index]
first_word_upper = first_word.upper()
last_sentence = word[first_word_end_index:] 
result = first_word_upper + last_sentence
print(result)