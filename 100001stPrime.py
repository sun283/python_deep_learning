# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import numpy as np

MAX_SIZE = 1000000
def SOE(primelst):
    is_prime = np.ones(MAX_SIZE)
    
    prime = 2
    while (prime * prime) < MAX_SIZE:
        if is_prime[prime] == True:
            i = (prime * prime)
            while i < MAX_SIZE:
                is_prime[i] = 0
                i += prime
        prime += 1

    prime = 2
    while prime < MAX_SIZE:
        if is_prime[prime]:
            primelst.append(prime)

        prime += 1

    return primelst

result = SOE([])

n = 10001
print(result[n - 1])
