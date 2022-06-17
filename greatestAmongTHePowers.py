first_num = int(input())
second_num = int(input())
first_case = first_num ** second_num
second_case = second_num ** first_num
result = first_case > second_case
if result:
    print(first_case)
else :
    print(second_case)