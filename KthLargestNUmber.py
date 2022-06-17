word = input()
result = word.split(",")
index = int(input())
new_list = []
for each in result:
    new_list += [int(each)]
largest_num = sorted(new_list)

print(largest_num[-index])
