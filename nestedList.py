num = int(input())
final_result = []
def con_str_num(newlist):
    new_list =[]
    for each in newlist:
        each_num = int(each)
        new_list.append(each_num)
    return new_list
for each in range(num):
    newlist = input().split(" ")
    newlist = con_str_num(newlist)
    final_result.append(newlist)
print(final_result)