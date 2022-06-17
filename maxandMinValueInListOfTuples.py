num = int(input())
first_list = []
second_list = []
for each in range(num):
    word = input().split()
    first_index = int(word[0])
    second_index = int(word[1])
    first_list.append(first_index)
    second_list.append(second_index)
tuple_one = max(first_list)
tuple_two = min(first_list)
tuple_one_one = max(second_list)
tuple_two_two = min(second_list)
new_list_one = []
new_list_two = []

new_list_one.append(tuple_one)
new_list_one.append(tuple_two)


new_list_two.append(tuple_one_one)
new_list_two.append(tuple_two_two)
print(tuple(new_list_one))
print((tuple(new_list_two)))