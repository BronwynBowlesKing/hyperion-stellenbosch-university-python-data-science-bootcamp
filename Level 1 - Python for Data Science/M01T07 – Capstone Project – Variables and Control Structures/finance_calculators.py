# Capstone Project

# This function creates a calculator that allows the user to determine the value of an investment at a future date or to find out their bond repayment per month.

def calculator():
    request = input("Type 'investment' to access the investment calculator and find out the amount of interest you'll earn. Or, type 'bond' for the bond calculator to find out the amount you'll have to pay on a home loan. ").lower()
    # The input for request is changed to lowercase to ensure only 'investment' or 'bond' is fed to the function.

    if request == "investment":
        deposit = float(input("Enter the amount of money you want to deposit: "))
        inv_interest = float(input("Enter the interest rate as a number only and leave out the percentage sign: "))
        inv_period = int(input("Enter the number of years for the investment period: "))
        interest_type = input("Type 'simple' for simple interest or 'compound' for compound interest: ").lower()
        # Input is lowercased.

        if interest_type == "simple":
            total_amount = deposit * (1 + (inv_interest / 100) * inv_period) # 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
            print(f"The total investment after {inv_period} years with simple interest will be: {total_amount:.2f}.") # Output is rounded to 2 decimal places.

        elif interest_type == "compound":
            total_amount = deposit * (1 + (inv_interest / 100)) ** inv_period  # 𝐴 = 𝑃(1 + 𝑟)^𝑡 (exponent format)
            print(f"The total amount after {inv_period} years with compound interest will be: {total_amount:.2f}.")

        else:
            print("Please enter 'simple' or 'compound'.")

    elif request == "bond":
        house_value = float(input("Enter the value of the house you want to buy: "))
        bond_interest = float(input("Enter the interest rate as a number only and leave out the percentage sign: "))
        bond_period = int(input("Enter the number of months (not years) you want to pay off the bond: "))
        
        monthly_interest_rate = (bond_interest / 100) / 12
        monthly_payment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** -bond_period)
        
        print(f"The monthly payment for the bond will be: {monthly_payment:.2f}.")

    else:
        print("Please make a valid selection.") # Handle errors in initial input

calculator() # Run the function

# INVESTMENT CALCULATOR
# Simple interest: 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
# Compound interest: 𝐴 = 𝑃(1 + 𝑟)^𝑡 - t is an exponent here and can be calculated with **
# Where:
# A is the total amount once interest has been applied (total_amount).
# P is deposit (deposit).
# r is interest rate entered divided by 100 (inv_interest).
# t is period in years (inv_period).

# BOND CALCULATOR
# A = (𝑖 × 𝑃) / 1 - (1 + 𝑖)^-𝑛
# Where:
# A is the monthly payment (monthly_payment).
# P is present value of the house (house_value).
# i is monthly interest rate entered divided by 100 for percentage and then by 12 for monthly (monthly_interest_rate). 
# n is the number of months over which the bond will be repaid (bond_period).