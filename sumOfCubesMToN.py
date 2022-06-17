def sum_of_cubes_m_to_n(m, n):
    result = 0
    for each in range(m,n+1):
        cubed_number = each ** 3
        result += cubed_number
    print(result)# Complete this function


m = int(input())
n = int(input())
# Call the sum_of_cubes_m_to_n function
sum_of_cubes_m_to_n(m,n)