one = input()
two = input()
subseq_index = 0
leng_subseq  = len(two)
for each in one:
    if each == two[subseq_index]:
        subseq_index += 1 
        if subseq_index == leng_subseq:
            break 
if subseq_index == leng_subseq :
    print("Yes")
else:
    print("No")