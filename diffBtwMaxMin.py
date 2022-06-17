word = input()
result = word.split(",")
new_list = []
for each in result:
    new_list += [int(each)]
largest_num = max(new_list)
smallest_num = min(new_list)
result = largest_num - smallest_num
print(result)