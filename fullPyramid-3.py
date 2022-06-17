num = int(input())
for each in range(1,num+1):
    first_case = "0 " * (num - each)
    second_case = "1 " * ((2*each) - 1)
    print(first_case+second_case+first_case)