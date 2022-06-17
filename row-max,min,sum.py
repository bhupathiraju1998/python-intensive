def print_max_min_sum_for_row_wise(num_list,m,n):
    max_list = []
    min_list = []
    sum_list = []
    for each in num_list:
        max_el = max(each)
        max_list.append(max_el)
    for each in num_list:
        min_el = min(each)
        min_list.append(min_el)
    for each in num_list:
        sum_val = sum(each)
        sum_list.append(sum_val)
    print(max_list)
    print(min_list)
    print(sum_list)
    # Complete this function

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

final_result = print_max_min_sum_for_row_wise(num_list,m,n)
