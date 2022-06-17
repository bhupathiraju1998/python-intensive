word = input().split()
new_list = []
for each in word:
    new_list.append(int(each))

booleanValue = True
new_set = set(new_list)
result = sorted(list(new_set))
if len(new_set) == 1 :
    print(booleanValue)
else:
    print(result)