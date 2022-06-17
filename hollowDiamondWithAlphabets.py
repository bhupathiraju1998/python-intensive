list_a = [" ","A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num = int(input())
hollow_space_count = -1
print((" "*(num-1)) + "A" )
for each in range(2,num+1):
    left_spaces = " " * (num-each)
    alphabets = list_a[each]
    hollow_space_count = hollow_space_count +2
    middile_spaces = " " * hollow_space_count
    print(left_spaces+alphabets+middile_spaces+alphabets)

for item in range(1,num-1):
    left_spaces = " " * item
    alphabets = list_a[num - item]
    hollow_space_count = hollow_space_count - 2
    
    middile_spaces = " " * hollow_space_count
    
    print(left_spaces+alphabets+middile_spaces+alphabets)
    
    
    
print((" "*(num-1)) + "A" )