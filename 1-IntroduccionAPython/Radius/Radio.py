import math

def Radius(a,b,c,s):
    r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    return r

def SemiPerimetro(a,b,c):
    s = (a+b+c)*(1/2)
    return s

print("Radio = ",Radius(8,16,14,SemiPerimetro(8,16,14)))