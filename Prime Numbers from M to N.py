num1 = int(input())
num2 = int(input())
for each in range(num1,num2+1):
    factors = 0
    for i in range(2,each):
        if (each % i) == 0:
            factors = factors + 1 
            
    if factors == 0:
        print(each)
    