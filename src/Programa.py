from sympy import integrate, Piecewise, oo, E
from sympy import Symbol, And

x = Symbol("x", real=True)
y = Symbol("y", real=True)

def Integral(función, *intervalos):
    funcionTrozos = Piecewise((función, And(*intervalos)),(0, True))
    variables = funcionTrozos.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(funcionTrozos, *lista).simplify()

v1 = (x<1)
v2 = (0<y)
v3 = (y<x)
funcion = E**(-(x**2))

print(Integral(funcion, v1, v2, v3))
