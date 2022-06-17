word = input()
for each in word:
    if each == each.upper():
        if not each.isdigit():
            print(each)
            break