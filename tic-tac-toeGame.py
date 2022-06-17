def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = item
        new_list.append(num)
    return new_list



num_list = []

for i in range(3):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
#for each in range(len(num_list)):
x_alphabet = "X"
o_alphabet = "O"
count = 0
if num_list[0][0] == num_list[1][0] == num_list[2][0] == "X":
    print("Anjali Wins")
    count += 1
elif num_list[0][0] == num_list[1][0] == num_list[2][0] == "O":
    print("Abhinav Wins")
    count += 1
if num_list[0][1] == num_list[1][1] == num_list[2][1] == "X":
    print("Anjali Wins")  
    count += 1
elif num_list[0][1] == num_list[1][1] == num_list[2][1] == "O":
    print("Abhinav Wins")
    count += 1
if num_list[0][2] == num_list[1][2] == num_list[2][2] == "X":
    print("Anjali Wins")  
    count += 1
elif num_list[0][2] == num_list[1][2] == num_list[2][2] == "O":
    print("Abhinav Wins")
    count += 1
  
  
if num_list[0][0] == num_list[0][1] == num_list[0][2] == "X":
    print("Anjali Wins")
    count += 1
elif num_list[0][0] == num_list[0][1] == num_list[0][2] == "O":
    print("Abhinav Wins")
    count += 1
if num_list[1][0] == num_list[1][1] == num_list[1][2] == "X":
    print("Anjali Wins")  
    count += 1
elif num_list[1][0] == num_list[1][1] == num_list[1][2] == "O":
    print("Abhinav Wins")
    count += 1
if num_list[2][0] == num_list[2][1] == num_list[2][2] == "X":
    print("Anjali Wins")  
    count += 1
elif num_list[2][0] == num_list[2][1] == num_list[2][2] == "O":
    print("Abhinav Wins") 
    count += 1
    
if num_list[0][0] == num_list[1][1] == num_list[2][2] == "X":
    print("Anjali Wins")
    count += 1
elif num_list[0][0] == num_list[1][1] == num_list[2][2] == "O":
    print("Abhinav Wins")
    count += 1
if num_list[0][2] == num_list[1][1] == num_list[2][0] == "X":
    print("Anjali Wins")
    count += 1
elif num_list[0][2] == num_list[1][1] == num_list[2][0] == "O":
    print("Abhinav Wins") 
    count += 1
    
if count == 0:
    print("Tie")
    
    
    