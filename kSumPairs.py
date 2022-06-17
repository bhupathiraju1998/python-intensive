word = input().split(",")
num = int(input())
new_list = []
for each in word:
    new_list.append(int(each))
def get_pair(new_list,num):
    end_index = len(new_list) - 1 
    final_set = set()
    for item in range(end_index):
        if item == num:
            pair = item,
            sorted_pair = tuple(sorted(pair))
            final_set.add(sorted_pair)
        if item < num:
            num1= item
            num2 = num-num1
            pair  = ()
    return final_set
            

unique_pairs = get_pair(new_list,num)
for each in unique_pairs:
    print(each)
