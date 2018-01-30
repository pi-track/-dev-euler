#problem 25

import time

time0=time.time()

x,y = 1,2
f=3
while len(str(y)) < 1000:
    x,y = y,x+y
    f+=1

print('time = ',(time.time()-time0))
print f
