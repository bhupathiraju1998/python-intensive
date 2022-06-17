word = input().split(",")
new_list = []

for each in word:
    result = each.isdigit()
    if result:
        new_list.append(int(each))
print(new_list)