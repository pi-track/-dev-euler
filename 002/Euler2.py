x,y = 1,2
a=list()
a.append(y)
while y > 1:
    x,y = y,x+y
    if y>4e6:
        break
    if y%2 == 0:
        a.append(y)
print(sum(a))
