#Problem 20

import time
time0=time.time()
n=100
factorial = 1

for i in range(1,n+1):
    factorial*=i

a=map(int, str(factorial))
asum=sum(a)
print asum

print('that took %s seconds',(time.time()-time0))
