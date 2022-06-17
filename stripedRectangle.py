a = int(input())
b = int(input())
for each in range(1,a+1):
    if each == 1:
        print("+ " * b)
    elif each % 2 == 0:
        print("- " * b)
    else:
        print("+ " *b)