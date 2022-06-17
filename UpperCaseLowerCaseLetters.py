def get_lower_and_upper_case_letters(word):
    upper_result = ""
    lower_result = ""
    for each in word:
        if each == each.upper():
            upper_result += each
        else:
            lower_result += each
    print(upper_result)
    print(lower_result)
    
    # Complete this function
word = input()
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)
