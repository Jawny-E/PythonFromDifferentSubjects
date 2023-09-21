import sympy as sp


x, y, z, f, s, t = sp.symbols("x y z f s t")

f = sp.sin(x**2 + y**2)

print(f)

print(f.diff(x))

dfx = f.diff(x) # derivasjon mhp. x
dfy = f.diff(y)

print(dfx, dfy)

print(f.subs(x,1).subs(y,2)) # f(1,2)
print(dfx.subs(x,1).subs(y,2), dfy.subs(x,1).subs(y,2)) # gradient i (1,2)

x = sp.exp(t)   # e^t
y = sp.exp(2*t)   # e^2t
f = sp.sin(x**2 + y**2)

print(f, f.diff(t))

f = sp.exp(x**2 + y**2)
print(f)

# lineærapproksimasjon i (1,2)
dfx = f.diff(x).subs(x,1).subs(y,2)
dfy = f.diff(y).subs(x,1).subs(y,2)
f12 = f.subs(x,1).subs(y,2)

# likning tangentplan:  z=linapp
linapp = f12 + dfx*(x-1) + dfy*(y-2)

print(linapp.subs(x, 1.1).subs(y,2.2))

print(f.subs(x,1.1).subs(y,2.2))


f = x**2 + sp.sin(y**2)

sp.pprint(f)

# lage pdffil, eller html
print(sp.latex(f))