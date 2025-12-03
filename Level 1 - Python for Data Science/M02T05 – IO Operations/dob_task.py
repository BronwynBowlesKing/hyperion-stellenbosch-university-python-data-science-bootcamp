# Create empty lists first for the data
names = []
birth_dates = []

with open("DOB.txt", "r") as file:
    for line in file:  # For every line in the file... six processes are needed:
        stripped_line = line.strip()        # 1. Strip the front and end whitespace
        words = stripped_line.split()       # 2. Split the line into words
        name = " ".join(words[:-3])         # 3. Join all the words except the last 3 to create names
        birth_date = " ".join(words[-3:])   # 4. Join the last 3 words to make up birthdates
        names.append(name)                  # 5. Add the names to their []
        birth_dates.append(birth_date)      # 6. Add birthdates to their [] 

# Check if the stripping and rejoining worked
print(names)
print(birth_dates)

# Print the data as requested
print("Names")
for name in names:
    print(name)

print("\nBirth dates")
for birth_date in birth_dates:
    print(birth_date)

