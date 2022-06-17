input_number = int(input())
first_number = int(input())
smaller_number = first_number

for i in range(input_number - 1):
    number = int(input())
    if number < smaller_number:
        smaller_number = number
print(smaller_number)
