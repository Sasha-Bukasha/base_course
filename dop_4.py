import matplotlib.pyplot as plt
import numpy as np

def lesenka(n):
    N = 1
    x = np.arange(0, n, 0.1)
    y = x // 1
    plt.plot(x, y, color='g')
    plt.savefig("lesenka.png")
    plt.close
    
lesenka(5)