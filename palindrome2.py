word = input().lower()
new_word = ""
length_of_word = len(word)
for each in range(length_of_word):
    new_word += word[(length_of_word-1)-each]
if new_word == word:
    print("True")
else:
    print("False")