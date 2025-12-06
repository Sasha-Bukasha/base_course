
"""def sr_arifmet(*args):
    s=0
    for arg in args:
        s += args

    return s / len(args)

S = sr_arifmet(1, 5, 7, 29)
print(S)"""

import numpy as np

def parabola (a, b, N):
    x = np.linspace(a, b, N)
    return {'x':x}, {'y': x**2}

F = parabola(-1, 1, 10)
print(F)


"""def figure (n):
    deg = (180 - (n - 2)/ n)
    triang = (n - 2)
    circ = 
    return print(deg, triang, circ)

figure()"""

def area_calculator(figure, *kwargs):
    if figure == 'circle':
        area = np.pi * kwargs['r']**2
    elif figure == 'triangle':
        area = 0.5 * kwargs['l']*kwargs['h']
    else:
        area = 0.5 * kwargs['l']*kwargs['h']