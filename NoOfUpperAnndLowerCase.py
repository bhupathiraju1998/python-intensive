def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase = 0
    count_of_lowercase = 0
    for each in word:
        if each.upper() == each :
            count_of_uppercase += 1 
        else:
            count_of_lowercase += 1
    
    # Complete this function

    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
count_of_lowercase_and_uppercase_letters(word)
# Call the count_of_lowercase_and_uppercase_letters function
