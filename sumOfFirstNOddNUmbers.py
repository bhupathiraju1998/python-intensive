num = int(input())
sum = 0
for each in range(1, num + 1):
    odd = each % 2 != 0
    if odd :
        sum = sum + each
print(sum)