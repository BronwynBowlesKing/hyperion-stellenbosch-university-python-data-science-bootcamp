# With string concatenations:

name = input("What is your name? ") 
age = input("What is your age? ")
house_no = input("What is the number of the house where you live? ")
street = input("what is the name of your street? ")

print("Welcome " + name + ", we see you are " + age + " years old and you live at " + str(house_no) + " " + street + " street.")

# With an f string:

name = input("What is your name? ")
age = int(input("What is your age? "))
house_no = int(input("What is the number of the house where you live? "))
street = input("What is the name of your street? ")

print(f"Welcome {name}, we see you are {age} years old and you live at {house_no} {street} street.")