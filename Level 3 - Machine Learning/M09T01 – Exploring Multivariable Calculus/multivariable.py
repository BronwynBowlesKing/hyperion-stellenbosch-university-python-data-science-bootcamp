## Exploring Multivariable Calculus: Practical task 2

import sympy as sp


def compute_gradient():

    """
    Requests a two-term multi-variable function from the user and
    then computes the gradient and returns answer.
    
    Mathematical symbols are specified for x, y and ∇. SymPy is 
    applied for symbolic computation of partial derivatives with
    respect to x and y. Error-handling is included. 
    """ 

    x, y = sp.symbols('x y')
    
    while True:
        func_str = input(
            "Please enter a two-variable function for x and y (e.g. x**2 + y**2): "
        )

        try:
            func = sp.sympify(func_str)
            variables = func.free_symbols  # Verify if input contains x and/or y
            
            if not (sp.Symbol('x') in variables or sp.Symbol('y') in variables):
                print("Error has occured. Please include variables x and/or y.")
                continue
            
            grad_x = sp.diff(func, x)  # Partial derivatives computed here
            grad_y = sp.diff(func, y)
            
            print(
                f"""
                The gradient vector of function f = {func} is: 
                ∇f = ({grad_x}, {grad_y}).
                """
            )
            break

        except (sp.SympifyError, SyntaxError):
            print(
                "Input is not a valid mathematical expression. Please retry."
            )


compute_gradient()



# References

# Code adapted from:

# Kumar, P. (2020). Python partial derivative. 
# https://stackoverflow.com/questions/52567518/python-partial-derivative

# SymPy Development Team. (2018). SymPy Documentation. Release 1.2. 
# https://nrp-services.fr/ressources/nrp-4096-informatique-documentation-computer-sympy.pdf