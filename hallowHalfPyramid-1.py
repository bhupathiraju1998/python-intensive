num = int(input())
k=1
for i in range(1,num+1):
    if i >2 and i < num:
        print("* " + " "* (i-k)+"* ")
        k = k -1
    else:
        print("* " * i)