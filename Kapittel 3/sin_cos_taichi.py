from time import sleep
import taichi as ti
import numpy as np
ti.init(arch=ti.cpu)
gui = ti.GUI("Drawing", fullscreen=False)

a = 5
b = 5
c = 0
d = 0

start = 0
slutt = 2 * np.pi
step = 0.1

x = 0
y = 0

@ti.kernel
def steg():
    if x > slutt:
        x = 0
    y = calculate(y)
    render()
    x += step
    sleep(0.5)

@ti.func
def calculate():
    return (a * np.sin(((2*np.pi)/b)*x + c) + d)

@ti.func
def render():
    gui.circle((x, y), 0xffffff, 5)
    gui.show()