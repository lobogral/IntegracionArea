from sympy import Matrix, Abs, Symbol, simplify
from sympy import cos, sin, pi
from sympy import Rational as R
from Programa import Integral

def Transformar(func, listRels, varsRem, diccRem):

    M1 = Matrix(list(diccRem.values()))
    M2 = Matrix(varsRem)
    det = M1.jacobian(M2).det().simplify()

    funcRem = func.subs(diccRem)
    listRelsRem = [simplify(rel.subs(diccRem)) for rel in listRels]

    return (det, funcRem, listRelsRem)    

x = Symbol("x")
y = Symbol("y")
u = Symbol("u")
v = Symbol("v")
θ = Symbol("θ")
r = Symbol("r")

# Ejemplo 1
listRels = [x-2*y <= 0, x-2*y >= -4, x+y >= 1, x+y <= 4]
func = 3*x*y

varsRem = [u, v]
diccRem = {x:R(1,3)*(2*u + v),
           y:R(1,3)*(u - v)}

det, funcRem, listRelsRem = Transformar(func, listRels, varsRem, diccRem)
print(Integral(Abs(det)*funcRem, *listRelsRem))

# Ejemplo 2
listRels = [x**2 + y**2 >= 1, x**2 + y**2 <= 5]
func = x**2 + y

varsRem = [r, θ]
diccRem = {x:r*cos(θ),
           y:r*sin(θ)}

det, funcRem, listRelsRem = Transformar(func, listRels, varsRem, diccRem)
listRelsRem += [r >= 0, θ >= 0, θ <= 2*pi]
print(Integral(det*funcRem, *listRelsRem))
