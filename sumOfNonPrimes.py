num = int(input())
factors = 0
sum = 0
for each in range(2,num+2):
    new_num = int(input())
    for item in range(4,11):
        if new_num % item == 0:
            sum += new_num
            
            break
    continue
        
print(sum)

