def replace_old_value_with_new_value(matrix, old_value, new_value):
    updated_matrix = []
    for each in matrix:
        updated_row = each 
        for i in range(len(each)):
            if each[i] == old_value:
                updated_row[i] = new_value
        updated_matrix.append(updated_row)
    return updated_matrix
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

values = input().split()
old_value, new_value = convert_string_to_int(values)

updated_matrix = replace_old_value_with_new_value(num_list,old_value,new_value)
# Call the replace_old_value_with_new_value function
# Write your code here
for each in updated_matrix:
    print(each)