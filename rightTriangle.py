num = int(input())
for each in range(1,num+1):
    new_string = ""
    for item in range(1,each+1):
        new_string = new_string + str(item)
    new_second_string = ""
    if each > 1:
    
        for new_item in range(1,each):
            new_second_string = new_second_string + str(each - new_item)
            
    print(new_string+new_second_string)