import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0, 10, 1000)

b = np.exp(np.sin(2*np.pi*a))

d = np.abs(a)
x0 = 0
xf = 5
npts = 15
c = np.linspace(x0, xf, npts)
e = "allo toi"
a = "genre comme"
d = "penis"
f = e + d


plt.figure(1)
plt.plot(a,b)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Y en fonction de X")
plt.grid()
plt.show()