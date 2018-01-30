'''
Patrick Eells
Project Euler 12
'''
import time
import math

clock = time.time()
triangle=1
divisors=0
i = 2


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

while divisors <= 500:
    triangle = i + triangle
    i+=1
    primes = prime_factors(triangle)
    k=0
    r=0
    a_list = []
    divisors=1
    while k < len(primes):
        a=primes.count(primes[k])
        a_list.append(a)
        r+=1
        k+=a
        
    for j in range(len(a_list)):
        divisors*=(a_list[j]+1)
        
print triangle
print('that took %s secs', (time.time()-clock))


'''
take triangular number
figure out number of prime factors
put the power to which each of these prime factors are raised in the composite version of the number
implement formula from wiki
'''

