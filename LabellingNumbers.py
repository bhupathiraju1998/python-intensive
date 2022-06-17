def show_numbers(number):
    for each in range(0,number+1):
        if each == 0:
            print(str(each) + " EVEN")
        elif each % 2 == 0:
            print(str(each) + " EVEN")
        else:
            print(str(each) + " ODD")
    
    
    
    # Complete this Function


number = int(input())
# Call the show_numbers function
show_numbers(number)