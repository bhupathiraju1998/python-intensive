def convert_str_int(word):
    new_list = []
    for each in word:
        new_list.append(int(each))
    return new_list

def convert_key_value(key_list,value_list):
    dict_a = {}
    for item in range(len(key_list)):
        dict_a[key_list[item]] = value_list[item]
    return dict_a


word_one = input().split()
num_one = input().split()
word_two = input().split()
num_two = input().split()
dict_a_values = convert_str_int(num_one)
dict_b_values = convert_str_int(num_two)

student_details_1 = convert_key_value(word_one,dict_a_values)
student_details_2 = convert_key_value(word_two,dict_b_values)

student_details_1.update(student_details_2)
student_details = student_details_1.items()

student_details = sorted(student_details)
print(student_details)