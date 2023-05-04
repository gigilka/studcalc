import sympy as sp
import numpy as np

def integrate(entryFunc):
    res=format(sp.Integral(entryFunc).doit())
    return sp.latex(sp.sympify(res))