first_number = int(input())
second_number = int(input())
first_case = first_number == second_number
second_case = (first_number) > (second_number)
third_case = first_number < second_number
if first_case:
    print("A == B")
elif second_case:
    print("A > B")
else:
    print("A < B")