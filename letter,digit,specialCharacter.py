word = input()
if 33 >= ord(word) or ord(word) <= 41 or ord(word)== 64 or ord(word) == 95 or ord(word)==93:
    print("Special Character")
elif 48 >= ord(word) or ord(word) <= 57:
    print("Digit")
elif 65 >= ord(word) or ord(word)<= 90:
    print("Uppercase Letter")
elif 97 >= ord(word) or ord(word)<= 122:
    print("Lowercase Letter")
