word = input()
red_count = 0
green_count = 0
for each in word:
    if each == "R":
        red_count += 1 
    elif each == "G":
        green_count += 1 
print(min(red_count,green_count))