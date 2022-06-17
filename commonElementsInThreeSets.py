word_one = input().split()
word_two = input().split()
word_three = input().split()
new_list_one = []
new_list_two = []
new_list_three = []

for each in word_one:
    new_list_one.append(int(each))
for each in word_two:
    new_list_two.append(int(each))
for each in word_three:
    new_list_three.append(int(each))
set_one = set(new_list_one)
set_two = set(new_list_two)
set_three = set(new_list_three)
first_case = set_one & set_two
second_case = first_case & set_three
result = sorted(list(second_case))
print(result)










    