import matplotlib.pyplot as plt
import numpy as np

def Lissaju_figures (a=1, b=0.5, A=1, B, delta = np.pi/2):
    t = np.linspace(0, 2 + delta, 1000)
    x = A * np.sin(a*t * delta)
    y = B * np.sin(b*t)

    plt.plot(x, y)
    plt.savefig("Lisaju.png")
    plt.close

Lissaju_figures(1)