num = input()
length_of_num = len(num)
first_digit = int(num[0]) ** length_of_num
second_digit = int(num[1]) ** length_of_num
third_digit = int(num[2]) ** length_of_num
sums = first_digit + second_digit + third_digit
if sums == int(num):
    print("True")
else:
    print("False")