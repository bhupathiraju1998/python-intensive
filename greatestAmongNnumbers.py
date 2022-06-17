num = int(input())
first_input = int(input())
greater = first_input

for i in range(num-1):
    num2 = int(input())
    if num2 > greater:
        greater = num2
print(greater)