# generate primes
# Author: Andre Machado

'''
primes = []

for candidate in range(2, 101):
    is_prime = True
    for divisor in range(2, candidate):
        if(candidate % divisor == 0):
            is_prime = False
            break  # to jump out from the loop
    if is_prime:
        primes.append(candidate)
print(primes) '''

# Better way to do

primes = []
upto = 1000

for candidate in range(2, upto):
    is_prime = True
    # only needs to check if divisable by prime
    for divisor in primes:
        # if divisible by any int = its not prime
        if(candidate % divisor == 0):
            is_prime = False
            # so no reason to keep checking
            break
    if is_prime:
        primes.append(candidate)
print(primes)
