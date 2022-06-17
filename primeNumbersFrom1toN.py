num = int(input())
for each in range(2,num+1):
    factors = 0
    for i in range(2,each):
        if (each % i) == 0:
            factors = factors + 1 
    if factors == 0:
        print(each)
    
    