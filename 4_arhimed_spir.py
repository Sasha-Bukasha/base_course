import matplotlib.pyplot as plt
import numpy as np

def Arhimed_spir(k):
    phi = np.arange(0, 8*np.pi, 0.01)
    r = (2*np.pi*k) * phi

    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    plt.plot(x, y)
    plt.savefig("Arhimed_spir.png")
    plt.close

Arhimed_spir(0.3)