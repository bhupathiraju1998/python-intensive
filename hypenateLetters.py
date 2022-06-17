word = input()
new_string = ""
length = len(word)
for each in word:
    new_string += (each + "-")
new_word_length = len(new_string)
print(new_string[:new_word_length-1])