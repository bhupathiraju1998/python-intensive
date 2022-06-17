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
final_result = []


for each in num_list:
    final_result.append(max(each))

maximum = max(final_result)

row_index = final_result.index(maximum)

max_row = num_list[row_index]

print(max_row)

column_index_containing_max = max_row.index(maximum)

max_column = []
for row in num_list:
    final = max_column.append(row[column_index_containing_max])
    
print(max_column)

    
    