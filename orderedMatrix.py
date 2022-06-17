given_size_matrix = input().split()
m,n = given_size_matrix
m = int(m)
n = int(n)
new_list = []

for each in range(m):
    given_string = input().split()
    for item in given_string:
        item = int(item)
        new_list.append(item)
new_list.sort()
final_list = []
count = 0
count_end = n
for i in range(1,m+1):
    final_list.append(new_list[count:count_end])
    count = count_end
    count_end = count_end + n
    
for k in final_list:
    final_string  = ""
    for e in k:
        final_string += str(e)
        final_string += " "
    
    print(final_string)
    





