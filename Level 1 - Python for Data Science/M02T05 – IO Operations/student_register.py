num_students = input("How many students are registering for the exam? ")

with open("reg_form.txt", "w", encoding="utf-8") as file:

    for i in num_students:
        student_id = input("Enter the student ID number. ")
        file.write(student_id + " .......................")