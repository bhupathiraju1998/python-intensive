num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
new_list = input().split()
for each in new_list:
    num = int(each)
    num_set.discard(num)
result = list(num_set)
result.sort()
print(result)