# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Fixed syntax error of missing brackets and removed the space after print
# print "\n" It seems this line is not needed as the program will go to a new line in any case.

# Variables declaring the user's age, casting the str to an int, and printing the result

age = 24  # Removed unneeded indentation, extra = sign, and used lowercase for variable name. Change to "age" to designate the age only
age_str = str(age)  # Convert int to string and give it a new name
print("I'm " + age_str + " years old.")  # Use age_str and add spaces. These are syntax errors

    # Variables declaring additional years and printing the total years of age
# Fixed syntax errors below, made 3 an integer for calculation, corrected variable name in print statement and used fstring format
years_from_now = 3
total_years = age + years_from_now

print(f"The total number of years: {total_years}.")

# Variable to calculate the total number of months from the given number of years and printing the result
# total is not defined and needs a better name
# There are syntax and logical errors in the print statement and part of the equation is missing. The final answer needs to include not just three years but also six months' time. A variable for six months is needed. I am not entirely happy with this option below, however.
total_months = total_years * 12
six_months = 6
print(f"In 3 years and 6 months, I'll be ", total_months + six_months, " months old.")

# #HINT, 330 months is the correct answer

