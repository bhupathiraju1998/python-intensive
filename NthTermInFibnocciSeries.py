def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # Complete this function

n = int(input())
# call the fibonacci function
result = fibonacci(n)
print(result)