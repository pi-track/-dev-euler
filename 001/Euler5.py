#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?

import time

def smallest_divisible_number(n):

    smallest_number=20
    divisor=n        
    while divisor !=1:
        divisor = n
        smallest_number+=20
        while smallest_number % divisor == 0:
            if divisor == 1:
                break
            divisor-=1
    return smallest_number

start = time.time()
a = smallest_divisible_number(20)
elapsed = (time.time() - start)

print "result %s returned after %s seconds." % (a,elapsed)


#8/29/14 - smallest_number increment increased from 1 to 20, increased run time by a factor of 10
