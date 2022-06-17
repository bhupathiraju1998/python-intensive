def sum_of_squares_m_to_n(m, n):
    result = 0
    for each in range(m,n+1):
        squared_number = each ** 2
        result += squared_number
    print(result)
    # Complete this function


m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
sum_of_squares_m_to_n(m,n)