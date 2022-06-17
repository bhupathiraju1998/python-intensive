word = input().split(",")
k = int(input())
new_list = []
for each in word:
    new_list.append(int(each))
leng_of_new_list = len(new_list)
divison_num = k % leng_of_new_list
print(divison_num)
part_one = new_list[0:divison_num]
part_two = new_list[divison_num:]
part_two.extend(part_one)
print(part_two)