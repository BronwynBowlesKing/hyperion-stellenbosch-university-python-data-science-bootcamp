# challenge_1 - Area of a triangle

# This program calculates the area of a triangle using Heron's formula and three sides of the triangle provided by the user.

import math

def triangle_area(side1, side2, side3):
    sp = (side1 + side2 + side3) / 2  # All sides of the triangle divided by 2 - the semi-perimeter (sp)
    return math.sqrt(sp * (sp - side1) * (sp - side2) * (sp - side3)) # Square root calculation of area of triangle

# int or float can be used below to request input as Python can handle decimals with both types of numbers with the math module.
side1 = int(input("Enter the length of side 1 in cm: ")) 
side2 = int(input("Enter the length of side 2 in cm: "))
side3 = int(input("Enter the length of side 3 in cm: "))

print(f"{triangle_area(side1, side2, side3)} cm²") # Print area of the triangle in cm². fstring used to format output.

