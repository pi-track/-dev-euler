'''
Project Euler
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import time
x=1

def nth_prime(stop):
    testprime=3
    n=1
    while n<stop:
        i=2
        while x==1:
            if i == testprime:
                prime=testprime
                testprime+=1
                n+=1
                break
            if testprime%i == 0:
                testprime+=1
                break
            else:
                i+=1
    return(prime)
start = time.time()
a = nth_prime(10001)
elapsed = (time.time()-start)

print "result is %s returned after %s seconds" % (a, elapsed) 


#could be optimized by changing testprime increment from 1 to 2 - didn't work
#better way to generate primes?
