from sympy import integrate, Piecewise, oo
from sympy import Symbol, And
from sympy.functions import exp

x = Symbol("x", real=True)
y = Symbol("y", real=True)

def __crearFuncionTrozos(función, *intervalos):
    lista = [] 
    lista += [(función, And(*intervalos))]
    lista += [(0, True)]
    return Piecewise(*lista)

def Integral(función, *intervalos):
    funcionTrozos = __crearFuncionTrozos(función, *intervalos)
    variables = funcionTrozos.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(funcionTrozos, *lista)

v1 = (x<1)
v2 = (0<y)
v3 = (y<x)
funcion = exp(-x**2)

print(Integral(funcion, v1, v2, v3))
