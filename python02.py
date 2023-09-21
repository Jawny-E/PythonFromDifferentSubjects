import numpy as np  
import numpy.linalg as la

import sympy as sp
import sympy.physics.vector as sv


u = np.array([1,2,3])
v = np.array([-11,45,22])

print(u, v)
print(3*u + 4*v - 14*(u-v))

# skalar og kryssprodukt
print(np.dot(u,v))
print(np.cross(u,v))
print(np.dot(u, np.cross(u,v)))

# lengden/størrelsen til vektor
print(np.sqrt(np.dot(u,u)))
print(la.norm(u))

# enhetsvektor med samme retning som u
enu = u / la.norm(u)
print(enu)
print(la.norm(enu))
print(np.cross(u, enu))
print(u / np.sqrt(np.dot(u,u)))

# projeksjon av u på v
# (u*v) * v / |v|^2
proj = np.dot(u,v) * v / np.dot(v,v)
print("Projeksjon av u paa v", proj)


R = sv.ReferenceFrame("R")

u = 3*R.x + 4*R.y - 11*R.z
v = -3*R.x + 8*R.y - 4*R.z

print(u)
print(3*u + 2*v)

print(sv.dot(u,v))
print(sv.cross(u,v))
print(u.magnitude())
print(u.normalize())
print(u / u.magnitude())

