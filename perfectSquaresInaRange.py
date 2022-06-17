a = int(input())
b = int(input())
count = 0
for each in range(a,b+1):
    if each ** 0.5 == int(each ** 0.5) :
        count += 1 
        #print(count)
print(count)

