# np.navntilfunksjon()
import numpy as np

# skript

svar = 20 * 30

print("Hei!", 10, svar, 20*svar)

# enkel aritmetikk
print(3*4)
print(3/4)
print(3+4)
print(3-4)

# heltallsdivisjon
print(13//4)
print(13 % 4) # rest

print(3**4)

print(np.sqrt(20))

# vinkler er i radianer
print(np.cos(3))
print(np.sin(np.pi/3))
print(np.tan(1))

print(np.arccos(-1))
print(np.arcsin(-1))
print(np.arctan(2))

# punkt (x,y) i planet, arctan(y/x)  

# punktet (-1,-1)
print(np.arctan(-1/-1), np.pi/4) # ligger i feil kvadrant
print(np.arctan2(-1,-1))

print(np.exp(np.log(10)))
print(np.log(np.exp(20)))

print(np.fabs(-1.5))
print(np.fabs(1.5))

print(np.cosh(1))
print(np.sinh(1))
print(np.arccosh(1))
print(np.arcsinh(1))

print(np.cos(np.sin(2))+np.sinh(20)*np.exp(3))


import sympy as sp

print(sp.sin(sp.pi/4))
print(sp.asin(sp.sqrt(3)/2))

x, a, b = sp.symbols('x,a,b')

print(x*x+10)
print(sp.expand((x-a)*(2*x-b)))
print(sp.simplify( sp.cos(x**2)**2 + sp.sin(x**2)**2 ))

print(sp.solveset(x**2 - 1, x))

print(sp.solveset(x**2 + 1, x))

print(sp.solveset(x**2 + 1, x, domain = sp.S.Reals))

print(sp.solveset( sp.cos(x) - 1, x))






