def transpose(matrix):
    transpose_matrix = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(matrix[j][i])
        transpose_matrix.append(row)
    return transpose_matrix

def range_one(li):
    list_to_append_matrix = []
    final_transpose_matrix = transpose(num_list)
    for a in final_transpose_matrix:
        list_to_append_matrix.append(a[::-1]) 
    
    return list_to_append_matrix
def range_two(li):
    list_to_append_matrix = []
    list_to_append_matrix_2 = []
    final_transpose_matrix = transpose(num_list)
    for a in final_transpose_matrix:
        list_to_append_matrix.append(a[::-1]) 
    final_transpose_matrix = transpose(list_to_append_matrix)
    for a in final_transpose_matrix:
        list_to_append_matrix_2.append(a[::-1]) 
    
    return list_to_append_matrix_2
def range_three(li):
    list_to_append_matrix = []
    list_to_append_matrix_2 = []
    list_to_append_matrix_3 = []
    final_transpose_matrix = transpose(num_list)
    for a in final_transpose_matrix:
        list_to_append_matrix.append(a[::-1]) 
    final_transpose_matrix = transpose(list_to_append_matrix)
    for a in final_transpose_matrix:
        list_to_append_matrix_2.append(a[::-1])
    final_transpose_matrix = transpose(list_to_append_matrix_2)
    for a in final_transpose_matrix:
        list_to_append_matrix_3.append(a[::-1])
    
    return list_to_append_matrix_3


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = item
        new_list.append(num)
    return new_list
num = int(input())
num_list = []
gopal = []
for i in range(num):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
count = 0
degree_count = 0
angle_count =0
for i in range(8):
    given_string = input().split()
    
    if given_string[0] == "R":
        degree_count = degree_count + int(given_string[1])
        divided_by_90 = degree_count // 90
        obtained_range = divided_by_90 % 4 
        if obtained_range == 0:
            list_num = num_list
            
        if obtained_range == 1:
            list_num = range_one(num_list)
        if obtained_range == 2:
            list_num = range_two(num_list)
        if obtained_range == 3:
            list_num = range_three(num_list)
    elif given_string[0] == "Q" and i == 0:
        print(num_list[int(given_string[1])] [int(given_string[2])] )
        
    elif given_string[0] == "Q" and i != 0:
        
        print(list_num[int(given_string[1])] [int(given_string[2])] )
    
    elif given_string[0] == "U":
        #print(num_list)
        num_list[int(given_string[1])][int(given_string[2])] = (given_string[3])
        divided_by_90 = degree_count // 90
        obtained_range = divided_by_90 % 4 
        if obtained_range == 0:
            
            list_num = num_list
        if obtained_range == 1:
            list_num = range_one(num_list)
        if obtained_range == 2:
            list_num = range_two(num_list)
        if obtained_range == 3:
            list_num = range_three(num_list)
    elif given_string[0] == "-1":
        break
    
    