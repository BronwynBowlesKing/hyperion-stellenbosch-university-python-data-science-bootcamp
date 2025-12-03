# Database name: test_database
# Table name: python_programming

import sqlite3

try:
    with sqlite3.connect("test_database.db") as db:  # with handles db closure
        cursor = db.cursor()

        # Create the table python_programming
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS python_programming (
                id INTEGER PRIMARY KEY,
                name TEXT,
                grade INTEGER
            )
        ''')

        # Clear data in table if it already exists to add new data and
        # avoid errors
        cursor.execute('DELETE FROM python_programming')

        # Prepare data for multiple new rows. Ids are explicitedly stated
        student_grades = [
            (55, "Carl Davis", 61),
            (66, "Dennis Fredrickson", 88),
            (77, "Jane Richards", 78),
            (12, "Peyton Sawyer", 45),
            (2, "Lucas Brooke", 99)
        ]

        # Insert data
        cursor.executemany(
            '''INSERT INTO python_programming(id, name, grade) VALUES(?, ?, ?)
            ''', student_grades
        )

        # Ensure changes are committed
        db.commit()

        print("Table python_programming updated in test_database.")

except sqlite3.Error as error:
    print(f"An error occurred: {error}.")


# Query: All grades from 60% to 80%
cursor.execute(
    'SELECT name, grade FROM python_programming WHERE grade BETWEEN ? AND ?', 
    (60, 80)
    )

# Fetch and display all rows that match the query 
students = cursor.fetchall()  # Print each student's name and grade

print(f'Students with a grade between 60% and 80%: ')
for student in students: 
    print(f'{student[0]}: {student[1]}%')

# Update a student's grade
id = 55
grade = 65

cursor.execute(
    '''UPDATE python_programming SET grade = ? WHERE id = ?''', 
    (grade, id)
)

# Delete a table row
id = 66

cursor.execute(
    '''DELETE FROM python_programming WHERE id = ?''', 
    (id,)
)

# Change the grade of all students with id between 55 and 80. 
# The grade is changed to 75%. New data to insert here is specified 
# outside the cursor command. Parameters for search are inside this command
grade = 75

cursor.execute(
    '''UPDATE python_programming SET grade = ? WHERE id BETWEEN ? AND ?''',
    (grade, 55, 80)
)

# Display the data to verify changes
print("Data in table python_programming: \n (id, name, grade (%))")
cursor.execute('SELECT * FROM python_programming')
rows = cursor.fetchall()
for row in rows:
    print(row)