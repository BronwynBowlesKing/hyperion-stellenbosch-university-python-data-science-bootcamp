"""A simple calculator app for two numbers and one operator"""          

def calculator_app(): # No parameters inside the brackets here or the program tries to do something else

    while True: 
        query = input(
            "Press 1 to calculate an equation, 2 to see any previous equations, or any other key to exit, followed by enter: "
        ).strip()  # .strip() to help prevent input errors

        if query == '2':
            
            try:
                with open("equations.txt", "r") as file:
                    for line in file:
                        print(line)
            
            except FileNotFoundError:   # Raise an error for a missing file
                print("Sorry, no record is currently available.")
       
        elif query == '1':
            
            try:
                num1 = float(input("Enter the first number: ").strip())
                operator = input("Enter operator (+, -, *, /): ").strip()
                num2 = float(input("Enter the second number: ").strip())

                if operator == '+':  # Work around to handle operator input which could not be accepted in maths format
                    answer = num1 + num2
                
                elif operator == '-':
                    answer = num1 - num2
                
                elif operator == '*':
                    answer = num1 * num2
                
                elif operator == '/':
                    if num2 == 0:
                        print("Error: Division by zero cannot be done.")  # Manage division by 0
                        continue  # Restart the loop for the user to try again
                    answer = num1 / num2
                
                else:
                    print("Invalid operator.")  # Raise an error for invalid operator entered
                    continue

                print('The answer to this equation is:', answer)
                with open("equations.txt", "a") as file:  # Append the answer or the file will be overwritten
                    file.write(f"{num1} {operator} {num2} = {answer}\n")
            
            except ValueError:  
                print("Please enter numbers for the equation.")
        
        else:
            break

# Run the app
calculator_app()
