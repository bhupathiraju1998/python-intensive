number = input()

len_number = len(number)
if len_number == 1:
    print(number)
elif len_number == 2:
    print(int(number[0]) + int(number[1]))
elif len_number == 3:
    print(int(number[0]) + int(number[1]) + int(number[2]))
elif len_number == 4:
    print(int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]))   
elif len_number == 5:
    print(int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4])) 