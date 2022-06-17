list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
num = int(input())
new_list = []
for each in range(num):
    word = input().split()
    first_index = int(word[0])
    sec_index = int(word[1])
    result = list_a[first_index][sec_index]
    new_list.append(result)
print(new_list)
    