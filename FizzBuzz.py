def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    else:
        print(number)
    # Complete this function


number = int(input())
# Call the fizz_buzz function
fizz_buzz(number)