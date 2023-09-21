import sympy as sp

x, a, b = sp.symbols("x,a,b")

# grenseverdi
print(sp.limit(x**3+5, x, 0), 0**3+5)
print(sp.limit(sp.sin(x)/x, x, 0))

print(sp.diff(x**3+5, x))
print(sp.diff(sp.sin(x**3), x))
print(sp.diff(sp.sin(a*x), x))

# konstantledded mangler
print(sp.integrate(sp.sin(x), x))
print(sp.integrate(sp.sin(a*x),x))

print(sp.integrate(sp.sin(x*x)*x, x))
print(sp.integrate(sp.sin(x)*sp.cos(x), x))

print(sp.integrate(sp.sin(x), (x,0,1)))
print(sp.integrate(x*x, (x,0,1)))

#L�sning av differensiallikninger

f, df, ddf = sp.symbols("f,df,ddf", cls=sp.Function)
df = f(x).diff
ddf = df(x).diff

print(sp.dsolve(f(x)+df(x), f(x)))
print(sp.dsolve(f(x)+df(x)+ddf(x), f(x)))

print(sp.dsolve(f(x)+df(x), f(x), ics={f(1) : 2}))
print(sp.dsolve(f(x)+df(x)+ddf(x), f(x), ics={f(1) : 2, df(x).subs(x,0) : 2}))


