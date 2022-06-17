word = input()
first_character=word[0]
word_len=len(word)
last_character=word[word_len-1]
num_stars="*"*(word_len-2)
result = first_character+num_stars+last_character
print(result)