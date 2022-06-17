def get_final_list(number):
    final_list = []
    end_index = len(number) -1 
    for each in range(end_index):
        final = number[each] + number[each+1]
        final_list.append(final)
    return final_list
    
    return final_list


def get_required_list(number):
    
    
    while len(number) > 1:
        final_list = get_final_list(number)
        print(final_list)
        number = final_list


def convert_str_int(word):
    new_list = []
    for item in word:
        new_list.append(int(item))
    return new_list
word = input().split(",")

number =convert_str_int(word)
print(number)
get_required_list(number)



