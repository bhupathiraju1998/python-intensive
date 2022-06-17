def anti_diagonals(matrix,m,n):
    no_of_diagonals = m+n-1
    final_li = []
    if m > n:
        for e in range(n):
            row_index = 0
            col_index = e
            new_li = []
            while row_index <= e:
                if row_index > e :
                    break 
                else:
                    new_li.append(str(matrix[row_index][col_index]))
                    row_index += 1 
                    col_index -= 1 
            final_li.append(new_li)
        
        start = 1
        end = 2
        new_list1 = []
        while start <= n:
            if start > n:
                break 
            else:
                new_list1.append(str(matrix[start][end]))
                start += 1 
                end -= 1 
        final_li.append(new_list1)
        
        for w in range(2,m):
            row_start = w 
            col_start = m -n 
            new_list2 = []
            while row_start <= 4:
                if row_start > 4:
                    break 
                else:
                    new_list2.append(str(matrix[row_start][col_start]))
                    row_start += 1 
                    col_start -= 1 
            final_li.append(new_list2)
        
        
        
        
        
        
        
        
        
        
        
        
    else:
        for each in range(m):
            row_index = 0
            col_index = each
            
            new_li = []
            while row_index <= each:
                if row_index > each :
                    break 
                else:
                    new_li.append(str(matrix[row_index][col_index]))
                row_index += 1 
                col_index -= 1 
            final_li.append(new_li)
        
        range_of_below_diagonals = no_of_diagonals - m 
        for items in range(range_of_below_diagonals):
            if m == n:
                row_index_below = items + 1
                col_index_below = range_of_below_diagonals
                new_li_below = []
                while row_index_below <= range_of_below_diagonals:
                    if row_index_below > range_of_below_diagonals:
                        break 
                    else:
                        new_li_below.append(str(matrix[row_index_below][col_index_below]))
                        row_index_below += 1 
                        col_index_below -= 1
                final_li.append(new_li_below)
                
            else:
                row_index_below = items
                col_index_below = range_of_below_diagonals
                new_li_below = []
                while row_index_below < range_of_below_diagonals:
                    if row_index_below > range_of_below_diagonals:
                        break 
                    else:
                        new_li_below.append(str(matrix[row_index_below][col_index_below]))
                        row_index_below += 1 
                        col_index_below -= 1
                final_li.append(new_li_below)
                
    return final_li    

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

final_result = anti_diagonals(num_list,m,n)

for sub in final_result:
    top_diagonal = " ".join(sub)
    print(top_diagonal)




 