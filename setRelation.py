num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
word = input().split()
new_list = []
for each in word:
    new_list.append(int(each))
sort_list = sorted(new_list)
set_list = set(sort_list)

if num_set.issuperset(set_list):
    print("Superset")
elif num_set.issubset(set_list):
    print("Subset")
else:
    print("Disjoint Set")