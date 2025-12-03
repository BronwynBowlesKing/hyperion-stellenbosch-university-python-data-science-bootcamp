# challenge_2

# Write Python code to take the name of a user's favourite restaurant and store it in a variable called string_fav.

string_fav = input("Tell me the name of your favourite restaurant.") 

# Write a statement to take in the user's favourite number. Use casting to store it in an integer variable called int_fav.

int_fav = int(input("Tell me your favourite number."))

# Print out both of these using two separate print statements below what you have written.

print(string_fav) 
print(int_fav)

# Once this is working, try to cast string_fav to an integer. What happens? Add a comment in your code to explain why this is.

string_fav = int(string_fav) 
# Output is "ValueError: invalid literal for int() with base 10"
# This produces an error because string_fav is non-numeric.

# CONCLUSION:
# The string cannot be converted to an integer because it has characters.
# The int() function can only convert whole numbers into integers.
# There is no solution to turning a string into an integer if the string contains characters. 



