import math
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
h=float(input("Введіть число h:"))
spisok = []
x=a
while x<b:
  f = math.log(5, math.fabs(2 + x + 7)) + (x-4) **1./3.
  spisok.append(f)
  x=x+h
print(spisok)