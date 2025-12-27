import matplotlib.pyplot as plt
import numpy as np

def Rosa(k):
    phi = np.arange(0, 8*np.pi, 0.01)
    r = np.sin((2*np.pi*k) * phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    plt.plot(x, y)
    plt.savefig("Rosa.png")
    plt.close

Rosa(0.3)