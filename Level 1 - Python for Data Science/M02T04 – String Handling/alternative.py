# alternative

user_sentence = input("Please write down your goal in five words or less. ")

print(user_sentence)

characters = list(user_sentence)  # list built-in function to split into individual characters 

for i in range(len(characters)):
    if i % 2 == 0:
        characters[i] = characters[i].upper()
    else:
        characters[i] = characters[i].lower()

up_low_string = "".join(characters)    

print(up_low_string)


for i in range(len(characters)):
    if i % 2 == 0:
        characters[i] = characters[i].lower()
    else:
        characters[i] = characters[i].upper()

low_up_string = "".join(characters)    

print(low_up_string)