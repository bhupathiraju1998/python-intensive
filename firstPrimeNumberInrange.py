m = int(input())
n = int(input())

if not(m>1):
    m = 2

no_primes = True

for i in range(m, n+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i)
        no_primes = False
        break

if no_primes:
    print("No prime numbers in the given range")
 
    