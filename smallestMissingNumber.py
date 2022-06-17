given_string = input().split()
number_set = set()
for each in given_string:
    each = int(each)
    number_set.add(each)
number_list = list(number_set)
max_of_number_list = max(number_list)
#print(max_of_number_list)
new_list = []
for item in range(1,max_of_number_list+2):
    if item not in number_list:
        new_list.append(item)

print(min(new_list))