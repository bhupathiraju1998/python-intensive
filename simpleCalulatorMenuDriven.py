word = input().split()
if word[1] == "+" :
    print(int(word[0]) + int(word[2]))
elif word[1] == "-" :
    print(int(word[0]) - int(word[2]))
elif word[1] == "*" :
    print(int(word[0]) * int(word[2]))
elif word[1] == "/" :
    print(int(word[0]) / int(word[2]))
elif word[1] == "%" :
    print(int(word[0]) % int(word[2]))