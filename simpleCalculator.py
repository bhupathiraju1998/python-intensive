operator = input()
first_number = int(input())
second_number = int(input())
first_case = operator == "+"
second_case = operator == "-"
third_case = operator == "*"
fourth_case = operator == "/"
fifth_case = operator == "%"
if first_case:
    print(first_number + second_number)
elif second_case:
    print(first_number - second_number)
elif third_case:
    print(first_number * second_number)
elif fourth_case:
    print(first_number / second_number)
elif fifth_case:
    print(first_number % second_number)
