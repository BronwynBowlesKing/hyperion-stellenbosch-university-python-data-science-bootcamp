class Adult():
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        self.can_drive = True
        print(f"{self.name} is old enough to drive.")
        
class Child(Adult):
    def can_drive(self):
        self.can_drive = False
        print(f"{self.name} is not old enough to drive.")
    
def create_person(name, age, hair_colour, eye_colour):
    if age >= 18:
        person = Adult(name = name, age = age, hair_colour = hair_colour, eye_colour = eye_colour)
    else:
        person = Child(name = name, age = age, hair_colour = hair_colour, eye_colour = eye_colour)
    return person

name = input("What is your name? ")
age = int(input("What is your age? ")) 
hair_colour = input("What is your hair colour? ")
eye_colour = input("What is your eye colour? ")

person = create_person(name, age, hair_colour, eye_colour)
person.can_drive()