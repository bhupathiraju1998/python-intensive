num = int(input())
sum_of_num = 0
count = 0
for each in range(1,num):
    if num % each == 0:
        sum_of_num += each
        count += 1
        #print(count)
if count > 1 :
    print("True")
elif num == 1:
    print("False")
else:
    print("False")
