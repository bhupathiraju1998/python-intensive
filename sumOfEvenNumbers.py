num = int(input())
sum_of_num = 0
for each in range(2,num+1):
    if each %2 == 0:
        sum_of_num += each
print(sum_of_num)