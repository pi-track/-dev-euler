'''
Patrick Eells
Project Euler
Problem 4: Largest Palindrome
'''
import numpy as np
import time

start = time.time()
#how many digits does the number have? i is the number
def size(number):        
    i=0
    check=1
    while check != 0:
        i+=1
        check = number//(10**i)
    return i

def is_palindrome(a):
    #even check
    if len(a)%2 == 0:
        for i in range(len(a)/2):
            if (a[i] == a[len(a)-1-i]):
                continue
            else:
                return False
        return True
            
    #odd check
    else:
        for i in range(len(a)/2-1):
            if (a[i] == a[len(a)-1-i]):
                continue
            else:
                return False
        return True

def list_to_num(a):
    number = 0
    for i in range(len(a)):
        number += a[i]*10**(len(a)-i-1)
    return number

#check if the number is a palindrome
big_numbers = list()
biggest_palindrome = 0
for k in np.linspace(999,900,100):
    for j in np.linspace(999,900,100):
        number = int(k*j)
        a = list()
        
        #how many digits
        num_of_digits = size(number)

        #break the number up into a list
        for i in reversed(range(num_of_digits)):
            temp=number//(10**i)
            number=number-(temp*10**i)
            a.append(temp)
        #palindrome check
        is_it = is_palindrome(a)
        if is_it is True:
            temp_biggest_palindrome = list_to_num(a)
            if temp_biggest_palindrome > biggest_palindrome:
                biggest_palindrome = temp_biggest_palindrome

elapsed = (time.time() - start)
print "result %s returned after %s seconds." % (biggest_palindrome, elapsed)
