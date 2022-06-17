def add_two_matrices(first_matrix, second_matrix, m, n):
    final_result = []
    for i in range(m):
        row_result = []
        for j in range(n):
            value = first_matrix[i][j] + second_matrix[i][j]
            row_result.append(value)
        final_result.append(row_result)
    return final_result
    # Complete this function

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


def read_matrix_inputs(m):
    num_list = []
    for i in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


m, n = input().split()
m, n = int(m), int(n)

first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)

# call the add_two_matrices matrices
final_result = add_two_matrices(first_matrix,second_matrix,m,n)
for each in final_result:
    print(each)
