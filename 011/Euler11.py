'''
Patrick Eells
Euler 11
'''

import numpy as np

a = np.loadtxt("20by20.txt")
bignumber = 0
position = list()
#loop through all adjacent in rows
for j in range(20):
    for i in range(20):
        number = a[j][i%20]*a[j][(i+1)%20]*a[j][(i+2)%20]*a[j][(i+3)%20]
        if number > bignumber:
            bignumber = number
#loop through all in columns
for j in range(20):
    for i in range(20):
        number = a[i%20][j]*a[(i+1)%20][j]*a[(i+2)%20][j]*a[(i+3)%20][j]
        if number > bignumber:
            bignumber = number
#loop through all diagonally
for j in range(20):
    for i in range(20):
        number = a[j%20][i%20]*a[(j+1)%20][(i+1)%20]*a[(j+2)%20][(i+2)%20]*a[(j+3)%20][(i+3)%20]
        if number > bignumber:
            bignumber = number
            print('diag')
for j in range(20):
    for i in range(20):
        number = a[j%20][i%20]*a[(j-1)%20][(i+1)%20]*a[(j-2)%20][(i+2)%20]*a[(j-3)%20][(i+3)%20]
        if number > bignumber:
            bignumber = number
            print('backdiag')
print (bignumber)
