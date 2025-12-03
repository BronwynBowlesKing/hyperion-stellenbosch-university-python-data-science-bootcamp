# NumPy is our numerical computational framework
import numpy as np

X = np.array([1, 2.5, 3, 3.25, 6, 8, 9.4])
y = np.array([0, 5, 7, 6.5, 9.5, 23.5, 18.7])


def model(x, m):
    """
    Our linear model f(x) = mx
    Receives: a data point x and the line gradient m
    Returns: a prediction for y
    """
    return m * x


def error_function(m):
    """
    Our error function J(m)
    This is done using the Mean Square Error (MSE) between our model and 
    the data
    Receives: m, the gradient of the line
    Returns: J(m), the Mean Squared Error between the model and the data
    Hint: you can use the data itself (X and y) from this function
    """
    y_predict = model(X, m)  
    mse = np.mean((y - y_predict) ** 2)  
    return mse


def derivative(m):
    """
    The derivation of the error_function J(m)
    Receives: m, the gradient of the line
    Returns: dJ/dm, the derivative of the error function with respect
    to m
    """
    n = len(X)
    y_predict = model(X, m)
    dJ_dm = (2 / n) * np.sum(X * (y_predict - y))
    return dJ_dm


def update_step(m, learning_rate=0.01):
    """
    Update the gradient m using the derivative of J(m)
    Receives: m, the gradient of the line
    Returns: a new and updated m
    """
    gradient = derivative(m)  
    m_new = m - learning_rate * gradient  
    return m_new


# Training for linear regression with step-by-step 
# improvement of model parameter and performance

m = -6  # Set initial value of the model’s slope (gradient)
n_epochs = 5 # Number of update steps

print('EPOCHS')
# Iterate for n epochs
for epoch in range(n_epochs):
    # Update and print m
    m = update_step(m)
    print(
        f'Epoch {epoch + 1}:' 
        f'm = {round(m,2)} and loss = {round(error_function(m), 2)}'
    )

# Print Final Results
print("--------------------------")
print("FINAL RESULTS")
print("--------------------------")
print(f'm = {round(m,2)} and loss = {round(error_function(m), 2)}')
print("--------------------------")