names = input().split(",")
ids = input().split(",")
dict_a = {}
length_of_names = len(names)
for each in range(length_of_names):
    dict_a[names[each]] = ids[each]
    

student_details = sorted(dict_a.items())

for i in student_details:
    print(*i)
    