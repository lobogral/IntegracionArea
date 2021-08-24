from sympy import integrate, Piecewise, oo
from sympy import Symbol, And

def Integral(función, *intervalos):
    funcionTrozos = Piecewise((función, And(*intervalos)),(0, True))
    variables = funcionTrozos.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(funcionTrozos, *lista).simplify()
