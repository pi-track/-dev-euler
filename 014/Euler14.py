#problem 14
#longest collatz sequence
#takes 10 seconds

import time

#function that takes some number a, and returns the length of the collatz chain
def collatz(a):
    chain=1
    while a != 1:
        if a%2==0:
            a=a/2
            chain+=1
        else:
            a=3*a+1
            chain+=1
    return chain


time0 = time.time()

chain=1
big_chain=1
a_list=[]
#iterates from 1 million to 800000, searching for the longest collatz chain
for i in range(200000):
    a=1000000-i
    chain=collatz(a)
    if chain > big_chain:
        big_chain=chain
        a_list.append(a)

print a_list[-1],big_chain
print('that took %s secs', (time.time()-time0))
