num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
num = int(input())
trail = []
for each in num_list:
    if num < each:
        trail =  trail + [each]
print(trail)