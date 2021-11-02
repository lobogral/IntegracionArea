from sympy import Matrix
from sympy import integrate, Piecewise, oo
from sympy import Symbol, And, simplify


def integral(funcion, *intervalos):
    funcion_trozos = Piecewise((funcion, And(*intervalos)), (0, True))
    variables = funcion_trozos.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(funcion_trozos, *lista).simplify()


def transformar(func, list_rels, vars_reem, dicc_reem):

    matrix_1 = Matrix(list(dicc_reem.values()))
    matrix_2 = Matrix(vars_reem)
    det = matrix_1.jacobian(matrix_2).det().simplify()

    func_reem = func.subs(dicc_reem)
    list_rels_reem = [simplify(rel.subs(dicc_reem)) for rel in list_rels]

    return (det, func_reem, list_rels_reem)
