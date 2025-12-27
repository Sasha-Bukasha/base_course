import matplotlib.pyplot as plt
import numpy as np

def lesenka(n):
    N = 1
    for i in range(0, n, 1):
        if i == n:
            plt.plot(n)
        else:
            X = N + 1
            y = N
            N = N + 1
    plt.savefig("lesenka.png")
    plt.close
    
lesenka(5)