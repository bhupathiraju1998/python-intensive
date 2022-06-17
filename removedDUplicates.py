word = input().split()
new_sequence = []
for each in word:
    num = int(each)
    new_sequence.append(num)
result = set(new_sequence)
num_list = list(result)

num_list.sort()
print(num_list)















