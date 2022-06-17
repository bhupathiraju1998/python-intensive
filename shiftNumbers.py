word = input()
word_list = []
num_list = []
for each in word:
    if each in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        word_list.append(each)
    else:
        num_list.append(each)
final_list = word_list + num_list
final_result = "".join(final_list)

print(final_result)