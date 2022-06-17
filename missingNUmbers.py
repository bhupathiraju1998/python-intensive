word = input().split()
new_list = []
for each in word:
    new_list.append(int(each))
max_of_new_list = max(new_list)
set_of_new_list = set(new_list)
max_set_of_set = set(range(1,max_of_new_list+1))
missing_num = max_set_of_set - set_of_new_list
list_missing_num = list(missing_num)
sort_missing_num = sorted(list_missing_num)
print(sort_missing_num)