import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0, 10, 1000)

b = np.exp(np.sin(2*np.pi*a))

c = np.cos(b)
e = "allo toi"
d = "penis"
f = e + d

plt.figure(1)
plt.plot(a,b)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Y en fonction de X")
plt.grid()
plt.show()