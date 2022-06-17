num_1 = int(input())
num_2 = int(input())
even_count = 0
odd_count = 0
for each in range(num_1,num_2+1):
    if each % 2 == 0:
        even_count += 1 
        
    elif each % 2 != 0:
        odd_count += 1
        
print(odd_count)
print(even_count)