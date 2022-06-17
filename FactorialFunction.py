def compute_factorial(n):
    if n == 0:
        return 1 
    else:
        return n * compute_factorial(n-1)


num = int(input())
# Call the compute_factorial function
result = compute_factorial(num)
print(result)



