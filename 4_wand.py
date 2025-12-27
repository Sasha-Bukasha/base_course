import matplotlib.pyplot as plt
import numpy as np

def Zhezl_spir(k):
    phi = np.arange(0.01, 8*np.pi, 0.01)
    r = (2*np.pi*k) / (phi**0.5)

    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig("Zhezl_spir.png")
    plt.close

Zhezl_spir(0.3)