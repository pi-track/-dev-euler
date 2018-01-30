#project euler # 10
'''
So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1< sqrt n.
This is 3 times as fast as testing all n

'''

import math
import time

clock=time.time()
prime = 33
primesum = 160
i=0
while prime < 2e6:
    is_prime = False
    prime+=2
    if (prime%2 != 0 and prime%3 != 0):
        k=1
        while (6*k-1 < int(math.sqrt(prime)+1)):
            if (prime%(6*k+1) != 0 and prime%(6*k-1) != 0):
                k += 1
                is_prime = True
            else:
                is_prime = False
                break
    if (is_prime is True):
        primesum=prime+primesum
        i+=1

print(primesum)
print(i)
print('that took %s secs' % (time.time()-clock))
