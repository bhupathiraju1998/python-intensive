word = input().split()
new_dict = {}
for each in word:
    count = 1
    if each in new_dict:
        new_dict[each] = new_dict[each] + count
    else :
        new_dict[each] = count

for each in new_dict:
    print("{}: {}".format(each,new_dict[each]))
