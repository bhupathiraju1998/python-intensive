num = int(input())
underscore = num +1 
print("_" * underscore)
for each in range(1,num+1):
    hollow_spaces = " " * (num-each)
    print("|" + hollow_spaces + "/")