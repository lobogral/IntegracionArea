from sympy import Matrix
from sympy import integrate, Piecewise, oo
from sympy import Symbol, And, simplify

def Integral(función, *intervalos):
    funcionTrozos = Piecewise((función, And(*intervalos)),(0, True))
    variables = funcionTrozos.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(funcionTrozos, *lista).simplify()

def Transformar(func, listRels, varsRem, diccRem):

    M1 = Matrix(list(diccRem.values()))
    M2 = Matrix(varsRem)
    det = M1.jacobian(M2).det().simplify()

    funcRem = func.subs(diccRem)
    listRelsRem = [simplify(rel.subs(diccRem)) for rel in listRels]

    return (det, funcRem, listRelsRem)    

