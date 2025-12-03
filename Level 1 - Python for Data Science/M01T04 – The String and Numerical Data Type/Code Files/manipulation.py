# Task 2

str_manip = input('Please enter a short phrase.')
print(str_manip)
print(len(str_manip))

last_letter = str_manip[-1]
print(last_letter)

stringat = str_manip.replace(last_letter, "@")
print(stringat)

print(str_manip [-3:])

newstring = str_manip[:3] + str_manip[-2:]

print(newstring [-3:])