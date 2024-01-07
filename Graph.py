import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y) = x^3 + y^3 - 1
f = lambda x, y: x**3 + y**3 - 1

# Create a grid of x and y values
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plot the contour where f(x, y) = 0
plt.figure(figsize=(8, 6))
contours = plt.contour(X, Y, Z, levels=[0], colors='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour plot of x^3 + y^3 = 1')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.show()