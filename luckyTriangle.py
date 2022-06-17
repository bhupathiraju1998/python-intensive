number_one = int(input())
number_two = int(input())
first_case = ((number_one == 6) or (number_two == 6))
second_case = ((number_one+number_two == 6)  or ((number_one-number_two == 6 or number_two-number_one ==6)) )
final_case = (first_case or second_case)
if final_case:
    print("Lucky")
else:
    print("Not Lucky")+