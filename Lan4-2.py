import math
def func(x0,x1):
    W = (math.sin(x0)-math.cos(x1))*4.138*math.log(math.fabs(math.sin(math.pi/4+2.31*x0)),math.e)
    return (W)
x=float(input('Ведіть X: '))
y=float(input('Ведіть Y: '))
W=func(x,y)
print(W)
