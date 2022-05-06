# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# def is_prime(number):
#     factors = [candidate_factor for candidate_factor in range(1, number+1) if number % candidate_factor == 0]
#     return len(factors) == 2

# number = 10

# #generates a list of numbers.
# primes = [number for number in range(2, 101) if is_prime(number)]
# prime_total = sum(primes)
# print (prime_total)

def sumOfPrimes(n):
    # list to store prime numbers
    prime = [True] * (n + 1)

    # Create a boolean array "prime[0..n]"
    # and initialize all entries it as true.
    # A value in prime[i] will finally be
    # false if i is Not a prime, else true.
     
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then
        # it is a prime
        if prime[p] == True:
            # Update all multiples of p
            i = p * 2
            while i <= n:
                prime[i] = False
                i += p
                print(i)
        p += 1   
          
    # Return sum of primes generated through
    # Sieve.
    sum = 0
    for i in range (2, n + 1):
        if(prime[i]):
            sum += i
    return sum
 
n = 2000000
print(sumOfPrimes(n))