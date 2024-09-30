import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# EXERCISE 1
def f(x, y): 
    return ((x**3)/3) - 4*x + ((y**3)/3) - 16*y

def stationary_points(f):
    x, y = sp.symbols('x y')
    f_x = sp.diff(((x**3)/3) - 4*x + ((y**3)/3) - 16*y, x)
    f_y = sp.diff(((x**3)/3) - 4*x + ((y**3)/3) - 16*y, y)
    stationary_points = sp.solve([f_x, f_y], (x, y))
    return stationary_points

def plot_surface(f, points):
    x1_vals = np.linspace(-10, 10, 100)
    x2_vals = np.linspace(-10, 10, 100)
    X_1, X_2 = np.meshgrid(x1_vals, x2_vals)
    Y = f(X_1, X_2)
    fig = plt.figure()
    fig.suptitle('f(x_1, x_2) = (x_1^3)/3 - 4x_1 + (x_2^3)/3 - 16x_2')
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        ax.scatter(point[0], point[1], f(point[0], point[1]), 
                   color='r', s=50, edgecolor='k', linewidth=1.5) 
    ax.plot_surface(X_1, X_2, Y, cmap='viridis')
    plt.show()

plot_surface(f, stationary_points(f))