word1 = input()
word2 = input()
new_list = []
new_word1 = word1.split(",")
new_word2 = word2.split(",")

new_word2 = set(new_word2)
new_word1 = set(new_word1)
result = new_word1&new_word2
final_result = list(result)
for each in final_result:
    final = (int(each))
    new_list.append(final)
    new_list.sort()
print(new_list)