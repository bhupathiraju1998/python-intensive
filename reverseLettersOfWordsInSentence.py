word = input()
new_list = word.split(" ")
string = ""
for each in new_list:
    string = string + each[::-1]+" "
print(string)
