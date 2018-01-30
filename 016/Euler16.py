#problem 16

import time

time0 = time.time()

a=2**1000
alist = map(int, str(a))
asum=sum(alist)

print asum
print('that took %s seconds', (time.time()-time0))
