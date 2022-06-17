def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    transpose_matrix = []
    for i in range(n):
        row_matrix = []
        for j in range(m):
            row_matrix.append(matrix[j][i])
        transpose_matrix.append(row_matrix)
    return transpose_matrix

def print_max_min_sum_for_row_wise(num_list,transpose_matrix):
    max_list = []
    min_list = []
    sum_list = []
    for each in transpose_matrix:
        max_list.append(max(each))
        min_list.append(min(each))
        sum_list.append(sum(each))
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


# Write your code here
transpose_matrix = get_transpose_of_matrix(num_list,m,n)

print_max_min_sum_for_row_wise(num_list,transpose_matrix)
# Call the get_transpose_of_matrix function
# Call the print_max_min_sum_for_row_wise function
    