import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from -100 to 100 in intervals of 0.5
start_val = -100
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

# Below is cubic polynomial of the form: 

# f(x) = 1.2x^3 + 0.5x^2 + 2x − 5

params = [1.2, 0.5, 2, -5]  

# where: 

# 1.2 is coefficient for x^3
# 0.5 is coefficient for x^2
# 2 is coefficient for x
# -5 is the constant term


"""
-----------------
Optional Task
------------------

Plot f(x) = P.X, where p is your params
"""

Y = np.polyval(params, X)

plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 1.2x³ + 0.5x² + 2x - 5')
plt.show()
