def sum_of_the_digits(number):
    integer = 0
    numbe = str(number)# Complete this recursive function
    for each in numbe:
        integer = integer + int(each)
    return integer
        

number = int(input())
# Call the sum_of_the_digits function
result = sum_of_the_digits(number)
print(result)