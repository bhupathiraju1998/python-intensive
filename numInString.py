given_string = input().split()
num = []
for k in given_string:
    if k.isdigit():
       num.append(k) 
    else:
        for j in k:
            if j.isdigit():
                num.append(j)

new_list = []
for each in num:
    each = str(each)
    length = len(each)
    for i in range(length):
        new_list.append(int(each[i]))

print(sum(new_list))
avg = (sum(new_list))/len(new_list)
print(round(avg,2))