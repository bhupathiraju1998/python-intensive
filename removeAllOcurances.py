nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
num = int(input())
count_num = nums_list.count(num)
for each in range(count_num):
    nums_list.remove(num)
    
print(nums_list)