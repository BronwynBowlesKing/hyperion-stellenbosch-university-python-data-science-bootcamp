incorrect_names = []  # Create an empty list

name = input("Enter your name: ")  
while name.lower() != "john":
    incorrect_names.append(name)
    name = input("Enter your name: ")  # Prompt the user again

print("Incorrect names: ", incorrect_names)