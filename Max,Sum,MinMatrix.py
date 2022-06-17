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
final_list = []
for each in num_list:
    final_list.extend(each)

max_val = max(final_list)
min_val = min(final_list)
sum_val = sum(final_list)
print(max_val)
print(min_val)
print(sum_val)