import math
x = float(input("Ведіть X: "))
if x > 3 :
    a = 2.31 - math.log1p(abs( x - 6 ))
    print(a)
elif 0 <= x <= 3 :
    b = math.cos(x + 3) + math.sin(2,(x) + math.pi / 2 )
    print(b)
elif x < 0 :
    c = 3/x + math.e**x / pow(x,3)
else :
    print("Неможливо знайти")