num1 = 99.23
num2 = 23
num3 = 150
string1 = '100'

num1 = int(num1)  # Recast num1 from float to  integer
num2 = float(num2)  # Recast num2 from integer to float
num3 = str(num3)  # Recast num3 from integer to string
string1 = int(string1)  # Recast string1 from string to integer

# Print the values of all variables each on a different line
# First tried this but it didn't work
# print(num1, 
#      num2, 
#      num3, 
#      string1)  

# Second attempt
print(num1)  
print(num2)
print(num3)
print(string1)

# Found an alternative way:
print(f'{num1}\n{num2}\n{num3}\n{string1}')

# Source
# BuiltIn. 2023. Guide to String Formatting in Python Using F-Strings. https://builtin.com/data-science/python-f-string