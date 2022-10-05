import math
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
h=float(input("Введіть число h:"))
x=a
for i in range(100):
    f = math.log(5, math.fabs(2 + x + 7)) + (x-4) **1./3.
    x = x + h
    print( 'x =', x, 'f =', f)
    if x>b:
        break 
