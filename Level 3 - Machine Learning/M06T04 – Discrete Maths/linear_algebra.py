import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5 
# (0.5 is approximate because there are 199 intervals between the numbers)

start_val = 0  
stop_val = 100  
n_samples = 200  # 100 / 200 = 0.5

# np linspace function creates array X of 200 numbers
X = np.linspace(start_val, stop_val, n_samples)  

params = np.array([2, -5])

"""
-----------------
Task 1
------------------

Plot f(x) = P.X, where p is your params
"""

Y = params[0] * X + params[1]

plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 2x - 5')
plt.show()
