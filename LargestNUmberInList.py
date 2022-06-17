word = input()
result = word.split(",")
new_list = []
for each in result:
    new_list += [int(each)]
print(max(new_list))