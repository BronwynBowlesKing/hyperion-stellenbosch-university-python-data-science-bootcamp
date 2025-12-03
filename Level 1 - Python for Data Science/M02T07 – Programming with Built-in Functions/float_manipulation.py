"""Working with the statistics module"""

import statistics 

random_nums = []  # Create a list to hold user input
count = 0  # Initialise count for the while loop
while count < 10:
    try:
        num = float(input("Please supply 10 random numbers followed by 'Enter'. Some can be whole numbers and others can have decimals. "))
        random_nums.append(num) # Add each user input to the list
        count += 1
    except ValueError: # Add error handling when numbers are not input
        print("Please enter a valid number.")

print(f"The sum of these numbers is: {sum(random_nums)}.")

print(f"The index, starting at 0, of the maximum value entered is: {random_nums.index(max(random_nums))}.")

print(f"The index, starting at 0, of the minimum value entered is: {random_nums.index(min(random_nums))}.")

print(f"The average of the numbers entered (rounded off to two decimal places) is: {round(statistics.mean(random_nums), 2)}.")

print(f"The median of the numbers entered is: {statistics.median(random_nums)}.")