import numpy as np  
import matplotlib.pyplot as plt # numerisk plotting

import sympy as sp
import sympy.plotting as spl  # symbolsk plotting

x = np.arange(-2.0, 2.0, 0.01)
y = np.sin(3.0*x)


plt.ylim(-1.1, 2.0)
#xlim
plt.plot(x,y,"r--")
plt.plot(x,x*x,"r-")
plt.plot(x,0*x,"k-") # k = svart
plt.plot(0*x,4.0*x,"k-")

plt.show()



x = sp.symbols("x")

p1 = spl.plot(x*x, (x,-2,2), show=False)
p2 = spl.plot(sp.sin(x*x), (x,-2,2), show=False)
p1.extend(p2)

p1.show()




