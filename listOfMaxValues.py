num = int(input())
final_result = []
def convert_str_int(input_list):
    new_list = []
    for each in input_list:
        num = int(each)
        new_list.append(num)
    return new_list

for each in range(num):
    input_list = input().split(" ")
    new_list = convert_str_int(input_list)
    max_of_list = max(new_list)
    final_result.append(max_of_list)
print(final_result)
    
    
    
    
    
    