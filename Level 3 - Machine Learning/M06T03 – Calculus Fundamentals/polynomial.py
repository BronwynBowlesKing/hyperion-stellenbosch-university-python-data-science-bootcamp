def format_num(num):

    '''
    Helper function to format whole numbers with the g format specifier.
    Automatically removes .0 for whole numbers but keeps decimals.
    '''

    return f'{num:g}'


def power_rule_derivative():
    
    '''
    Function to request user input and then apply the power rule
    formula: f(x) = ax^n and then calculate the gradient (rate of 
    change) at a specific point.
    '''

    a = float(input('Enter the coefficient of x: '))
    n = float(input('Enter the power to raise x to: ')) 
    x = float(input('Enter x-coordinate of point to calculate gradient: '))

    # Calculate the derivative using the power rule 
    deriv_coef = a * n
    deriv_pwr = n - 1

    # Calculate gradient at x-coordinate
    gradient = deriv_coef * (x ** deriv_pwr)  # ** = to the power of

    print(
        f'Derivative of polynomial {format_num(a)}x^{format_num(n)}:'
        f'\n{format_num(deriv_coef)}x^{format_num(deriv_pwr)}'
        f'\nGradient at point x = {format_num(x)} is: {format_num(gradient)}'
    )


# Run the function
power_rule_derivative()