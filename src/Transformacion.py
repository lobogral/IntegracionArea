from sympy import Matrix, Abs
from sympy.abc import x, y, u, v
from Programa import Integral
from sympy import Rational as R

def Transformar(func, listRels, varsRem, diccRem):

    M1 = Matrix(list(diccRem.values()))
    M2 = Matrix(varsRem)
    det = M1.jacobian(M2).det().simplify()

    funcRem = Abs(det)*func.subs(diccRem)
    listRelsRem = [rel.subs(diccRem) for rel in listRels]

    return (funcRem, listRelsRem)    


listRels = [x-2*y <= 0, x-2*y >= -4, x+y >= 1, x+y <= 4]
func = 3*x*y

varsRem = [u, v]
diccRem = {x:R(1,3)*(2*u + v),
           y:R(1,3)*(u - v)}

funcRem, listRelsRem = Transformar(func, listRels, varsRem, diccRem)

print(Integral(funcRem, *listRelsRem))
