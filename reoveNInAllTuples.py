num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
num = int(input())
new_list = []
for each in num_list:
    new_tuple = each
    if num in each:
        ind = each.index(num)
        new_tuple = each[:ind] + each[ind+1:]
        
    new_list.append(new_tuple)
print(new_list)num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
num = int(input())
new_list = []
for each in num_list:
    new_tuple = each
    if num in each:
        ind = each.index(num)
        new_tuple = each[:ind] + each[ind+1:]
        
    new_list.append(new_tuple)
print(new_list)