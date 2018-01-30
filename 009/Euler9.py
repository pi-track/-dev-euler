#Project Euler Problem 9
#Pythagorean Triplets

import time

a=0
b=0
c=0
n=2
m=1

time0 = time.time()

while a+b+c != 1000:
    a=n*n-m*m
    b=2*m*n
    c=n*n+m*m
    if n<25:
        n+=1
    else:
        n=2
        m+=1
        
print "a = %s b = %s c = %s" % (a, b, c)
                
elapsed = time.time()-time0
print "the product is %s and was found in %s seconds" % (a*b*c, elapsed)
