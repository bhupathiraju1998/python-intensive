try:
    word = input().split()
    num_1,num_2 = int(word[0]) , int(word[1])
    result = num_1/num_2
    print(result)
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")