import sympy as sp
b = 3
x, y = sp.symbols('x y')

g = y* sp.ln(y**2+x**2)
print("Expression : {}".format(g))
deriv = sp.diff(g,x)
deriv = sp.diff(deriv,x)
deriv = sp.diff(deriv,y)
deriv = sp.diff(deriv,y)

print("Derivative: {}".format(deriv))