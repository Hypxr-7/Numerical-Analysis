from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

xx = 5
x = [3,   4.5,  7,   9]
y = [2.5, 1,    2.5, 0.5]

# natural => second derivative at ends = 0
f = CubicSpline(x, y, bc_type='natural')
x_plot = np.linspace(1, 13, 100)
y_plot = f(x_plot)

print(f"Root at {xx}: {f(xx):.6f}")

plt.figure(figsize=(10, 10))
plt.plot(x_plot, y_plot, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()