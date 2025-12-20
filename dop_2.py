import matplotlib.pyplot as plt
import numpy as np

def elips(p, e):
    phi = np.arange(0, 8*np.pi, 0.01)
    a = 1 + e * np.cos(phi)
    r = p / a

    plt.plot(r)
    plt.savefig("experiment.png")
    plt.close

elips(1,0.1)