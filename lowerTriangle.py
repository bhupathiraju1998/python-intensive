def print_lower_triangle(matrix,m,n):
    result_list = []
    for i in range(m):
        result_list.append(matrix[i][:i+1])
    return result_list
        
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


# Call the print_lower_triangle function

result_list = print_lower_triangle(num_list,m,n)
for each in result_list:
    print(each)