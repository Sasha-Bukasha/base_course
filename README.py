import matplotlib.pyplot as plt
import numpy as np

# Ваши точки (x, y)
x_points = [0, 1, 2, 3, 4]
y_points = [0, 2, 1, 3, 2]

# Строим график
plt.plot(x_points, y_points, marker='o') # marker='o' показывает точки
plt.title("Кусочно-линейная кривая")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
plt.savefig('test.png')