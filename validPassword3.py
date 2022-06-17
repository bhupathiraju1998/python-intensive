word = input()

is_digit = False
for each in word:
    if_number = each.isdigit()
    if if_number:
        is_digit = True

is_lower = (word.lower() == word)
is_upper = (word.upper() == word)
contains_lower_and_upper = (not is_lower) and (not is_upper)

is_valid_password =(is_digit and contains_lower_and_upper)

if is_valid_password:
    print("Valid Password")
else:
    print("Invalid Password")
