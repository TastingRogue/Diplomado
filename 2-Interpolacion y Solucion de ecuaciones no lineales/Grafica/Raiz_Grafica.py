from math import exp

def f(x):
    return exp(2-x)-7*x

def f2(x):
    return -exp(2-x)-7

x0=1.5
x1=x0-f(x0)/f2(x0)

print('x1 = ', x1)

x2=x1-f(x1)/f2(x1)
print('x2 = ', x2)

x3=x2-f(x2)/f2(x2)
print('x3 = ', x3)
print('valor =',f(x3))
print('La raiz es ',x3)
