from sympy import Matrix, Abs, Rational
from sympy.abc import x, y, u, v
from Programa import Integral

r1 = (x - 2*y <= 0)
r2 = (x - 2*y >= -4)
r3 = (x + y >= 1)
r4 = (x + y <= 4)

func = 3*x*y

dicc = {x:Rational(1,3)*(2*u + v),
        y:Rational(1,3)*(u - v)}

r1 = r1.subs(dicc)
r2 = r2.subs(dicc)
r3 = r3.subs(dicc)
r4 = r4.subs(dicc)
func = func.subs(dicc)

M1 = Matrix(list(dicc.values()))
M2 = Matrix([u, v])
det = M1.jacobian(M2).det().simplify()

print(Integral(func*Abs(det), r1, r2, r3, r4))
