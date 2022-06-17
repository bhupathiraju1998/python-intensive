num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
num = int(input())
new_list = []
for each in num_list:
    result = each[:-1] + (num,)
    
    new_list.append(result)
print(new_list)
