password = input()
is_lower = (password.lower() == password)
if is_lower:
    print("Invalid Password")
else:
    print("Valid Password")
