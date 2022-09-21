import math
x = float(input('Введіть Х: '))
y = ((math.pow(math.e,0.9*x+4)+math.pow(x+2*math.pow(x,2),1/4))/(6*(math.fabs(x+2)+1)))-9*math.cos(0.7*x+math.sqrt(x))
print(y)
