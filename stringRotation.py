given_string = input()
rotated_string = input()
new_list = []
for each in range(len(given_string)):
    sub_string = given_string[each:] + given_string[:each]
    new_list.append(sub_string)
new_list = new_list[::-1]
if given_string == rotated_string:
    print(0)
elif rotated_string in new_list:
    ind = new_list.index(rotated_string)
    print(ind+1)
elif rotated_string not in new_list:
    print("No Match")
