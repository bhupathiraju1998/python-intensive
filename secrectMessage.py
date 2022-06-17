list_a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
"r","s","t","u","v","w","x","y","z"]
list_b= list_a[::-1]

word = input()
word = word.lower()
new_word = ""
for each in word:
    if each == " ":
        new_word += " "
    else:
        r = list_a.index(each)
        new_word += list_b[r]
print(new_word)