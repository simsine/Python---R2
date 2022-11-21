from matplotlib import pyplot as plt
from matplotlib.axis import XAxis
import numpy as np

pi = np.pi

a = 1
b = 1 * pi
c = 0
d = 0

start = 0
slutt = 1 * pi
step = 0.1

fig, ax = plt.subplots()


a = 1
# Plot sin
x = np.arange(start,slutt,step)
y = a * np.sin(((2*pi)/b)*x + c) + d
ax.plot(x, y)

a = -1
# Plot sin
x = np.arange(start,slutt,step)
y = a * np.sin(((2*pi)/b)*x + c) + d
ax.plot(x, y)

a = 1
# Plot cos
x = np.arange(start,slutt,step)
y = a * np.cos(((2*pi)/b)*x + c) + d
ax.plot(x, y)

a = -1
# Plot -cos
x = np.arange(start,slutt,step)
y = a * np.cos(((2*pi)/b)*x + c) + d
ax.plot(x, y)


# plt.scale.FuncScale(XAxis, functions)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
plt.show()