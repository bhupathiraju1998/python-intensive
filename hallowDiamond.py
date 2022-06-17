num = int(input())
left_spaces_count = num - 1 
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"
print(row_output)

hollow_spaces_count = -1
for each in range(2,num+1):
    left_spaces_count = num  - each
    left_spaces = " " * left_spaces_count
    
    hollow_spaces_count = hollow_spaces_count + 2
    hollow_spaces = " " * hollow_spaces_count
    
    row_output = left_spaces+"*"+hollow_spaces+"*"
    print(row_output)
for row in range(1,num-1):
    left_spaces_count = row
    left_spaces = " " * left_spaces_count
    
    hollow_spaces_count = hollow_spaces_count - 2
    hollow_spaces =  " " * hollow_spaces_count
    
    row_output = left_spaces + "*" + hollow_spaces + "*"
    print(row_output)

left_spaces_count = num - 1 
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"
print(row_output)

    
    
    
    
    
    
    
    
