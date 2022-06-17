salary = int(input())
years_of_service = int(input())
bonus_salary = ((salary/100)*5)
if years_of_service>5:
    print(bonus_salary)
else:
    print("No Bonus")