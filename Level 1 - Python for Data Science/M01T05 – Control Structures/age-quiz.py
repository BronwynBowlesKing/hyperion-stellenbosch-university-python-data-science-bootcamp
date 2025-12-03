# age-quiz

age = int(input("How old are you? "))

if age > 100: # age is more than 100
    print("Sorry, you're dead.")

elif 40 <= age < 65: # age is 40 to 64
    print("You're over the hill.")

elif 65 <= age <= 100: # age is 65 to 100
    print("Enjoy your retirement!")

elif age <= 13: # age is 13 or lower
    print("You qualify for the kiddie discount.")

elif age == 21: # age is 21
    print("Congrats on your 21st!")

else:
    print("Age is but a number.")
