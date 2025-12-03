class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for HO location
    ho_loc = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to display HO location
    def head_office(self):
        print("Our head office is based in", self.ho_loc)

# Subclass for specific course
class OOPCourse(Course):   

    def __init__(self, description, trainer, show_course_id):
        # No need to call super().__init__() with arguments, as Course has no __init__ defined
        self.description = description
        self.trainer = trainer
        self.show_course_id_value = show_course_id

    def trainer_details(self):
        print(f"{self.description}: OOP is object-orientated programming where you will learn how to reuse code more efficently and create code blueprints. \nYour trainer is: {self.trainer}.")
    
    def show_course_id(self):
        print(f"Your course ID is: {self.show_course_id_value}.")

    def course_1(self):
        print(self.trainer_details())
        print(self.contact_details())
        print(self.show_course_id())
    
# Example usage:
# Create an instance of the Course class
course = Course()

# Create an instance of the OOPCourse subclass
oop_course = OOPCourse(description="OOP Fundamentals", trainer="Mr Anon A. Mouse", show_course_id="#12345")

# Call methods specific to OOPCourse
oop_course.trainer_details()
oop_course.show_course_id()
course.contact_details()