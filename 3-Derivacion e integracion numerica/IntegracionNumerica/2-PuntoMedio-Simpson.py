def f(x):
    return (7**-x)+3

a = -1
b = 2
m = (a+b)/2

r1 = f(m)*(b-a)
print("Regla del punto medio: ",r1)

r1 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print("Regla de Simpson: ",r1)