num = int(input())
k = int(input())
number = num
is_factor = False
count = 0
for each in range(1,num+1):
    if not is_factor:
        if (num % number) == 0:
            count = count + 1 
        if count == k:
            print(number)
            is_factor = True
    number = number - 1