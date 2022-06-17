num_1 = int(input())
num_2 = int(input())
count = 0
list_a = list(range(1,100))
new_list = []
for each in range(1,num_2+1):
    if (each * each ) in range(num_1,num_2+1):
        count += 1 
        new_list.append(each*each)
    else:
        count += 0
if count >= 1:
    print(new_list[0])
else:
    print("No Perfect Square")