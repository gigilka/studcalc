import sympy as sp
import numpy as np

x, y, z = sp.symbols('x y z')

sp.init_printing(use_unicode=True)


def integrate(entryFunc):
    res = format(sp.Integral(entryFunc).doit())
    return sp.latex(sp.sympify(res))


def diff(entryFunc):
    res = format(sp.diff(entryFunc).doit())
    return sp.latex(sp.sympify(res))
