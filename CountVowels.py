def count_the_vowels(word):
    result = 0
    for each in word:
        if ((((each == "a" or each == "e") or each == "i" ) or each == "o") or each == "u"):
            result += 1 
    print(result)
    
    
    
    
    
    # Complete this function


word = input()
# Call the count_the_vowels function
count_the_vowels(word)