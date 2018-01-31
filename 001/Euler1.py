#!/usr/bin/env python

a=list()
for x in range(1000):
    if(x%3)==0:
        a.append(x)
    elif(x%5)==0:
        a.append(x)
print(sum(a))
