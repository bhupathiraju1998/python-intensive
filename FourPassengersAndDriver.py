def number_of_cars_needed(no_of_people):
    if (no_of_people % 5) == 0:
        print(int(no_of_people / 5))
    else :
        print(int((no_of_people / 5) + 1))
    
    
    # Complete this function


no_of_people = int(input())
# Call the number_of_cars_needed function
number_of_cars_needed(no_of_people)