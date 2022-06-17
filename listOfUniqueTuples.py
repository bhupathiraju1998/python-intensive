def convert_to_int(values_list):
    new_list = []
    for item in values_list:
        each_num = int(item)
        new_list.append(each_num)
    return new_list

num = int(input())
final_list = []
for each in range(num):
    list_a = input().split()
    list_a = convert_to_int(list_a)
    set_list = set(list_a)
    is_equal = len(set_list) == len(list_a)
    if is_equal:
        final_list.append(list_a)
print(final_list)
    
    
    
    
    
    
    