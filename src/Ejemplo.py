from Programa import Integral
from sympy import E
from sympy.abc import x,y

v1 = (x<1)
v2 = (0<y)
v3 = (y<x)
funcion = E**(-(x**2))

print(Integral(funcion, v1, v2, v3))
