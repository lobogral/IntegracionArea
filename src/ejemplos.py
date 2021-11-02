from sympy import Rational as R
from sympy import E, Symbol, Abs, cos, sin, pi
from programa import integral, transformar

x = Symbol("x")
y = Symbol("y")
u = Symbol("u")
v = Symbol("v")
θ = Symbol("θ")
r = Symbol("r")

# Ejemplo 1
v1 = (x < 1)
v2 = (y > 0)
v3 = (y < x)
funcion = E**(-(x**2))

print(integral(funcion, v1, v2, v3))

# Ejemplo 2
list_rels = [x-2*y <= 0, x-2*y >= -4, x+y >= 1, x+y <= 4]
func = 3*x*y

vars_reem = [u, v]
dicc_reem = {x: R(1, 3)*(2*u + v),
             y: R(1, 3)*(u - v)}

det, func_reem, list_rels_reem = transformar(func, list_rels,
                                             vars_reem, dicc_reem)
print(integral(Abs(det)*func_reem, *list_rels_reem))

# Ejemplo 3
list_rels = [x**2 + y**2 >= 1, x**2 + y**2 <= 5]
func = x**2 + y

vars_reem = [r, θ]
dicc_reem = {x: r*cos(θ),
             y: r*sin(θ)}

det, func_reem, list_rels_reem = transformar(func, list_rels,
                                             vars_reem, dicc_reem)
list_rels_reem += [r >= 0, θ >= 0, θ <= 2*pi]
print(integral(det*func_reem, *list_rels_reem))
