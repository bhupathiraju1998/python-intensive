word = input().split()
new_dict = {}
for each in word:
    count = 1
    if each in new_dict:
        new_dict[each] = new_dict[each] + count
    else :
        new_dict[each] = count
item_val = sorted(new_dict.items())

for each,item in item_val:
    print("{}: {}".format(each,item))

    
    
    