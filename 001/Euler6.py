#Project Euler
#Problem 6

#sum of the squares
import time

def sum_of_squares(n):
    x=1
    sum1=0
    while x<=n:
        sum1+=(x*x)
        x+=1
    return sum1

def square_of_sum(n):
    x=1
    sum2=0
    while x<=n:
        sum2+=x
        x+=1
    sum2_sq=sum2*sum2
    return sum2_sq

start = time.time()
sum_sq = sum_of_squares(100)
sq_sum = square_of_sum(100)
elapsed = (time.time() - start)

print sum_sq
print sq_sum
print "result of %s returned after %s seconds" % (sq_sum-sum_sq, elapsed)
