"""
*Task Manager Application 2.0*

Simple task management system for teams.
It allows users to log in, add new tasks, and view assigned tasks.
Administrators have additional acess to register new users,
view completed tasks, and delete tasks.

Standard features:
- User registration and authentication with username and password
- Storage of user and task details
- Task reporting

New features in version 2.0:
- Separate access and menus for admin and general users
- Enhanced task updating and tracking

External data dependencies:
- user.txt: Stores usernames and passwords
- tasks.txt: Stores all task details

How to use:
- Run the script and follow on-screen prompts

"""

## Please note, code was written in modular form from the beginning as
# per instructions on page 3 of "Capstone Project – Task Manager".


# ===== Import modules ===========

import os


# ========Preparation step==========

# Check if the required files are available in the user's working directory

if not os.path.exists("user.txt") or not os.path.exists("tasks.txt"):
    print(
        f"""
        Move the files 'user.txt' and 'tasks.txt' to the working directory:
            {os.getcwd()}
        Alternatively, contact IT Support for assistance.
    """
    )

else:
    print("Welcome to Task Manager 2.0...\n")


# === Helper function ===


def write_newline(line, filename):
    """
    Ensures data is written on a new line in plain text files.
    """
    last_char = ""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            f.seek(0, 2)  # Move to end of file
            if f.tell() > 0:
                f.seek(0)
                content = f.read()
                last_char = content[-1]

    except FileNotFoundError:
        last_char = ""

    with open(filename, "a", encoding="utf-8") as f:
        if last_char and last_char != "\n":
            f.write("\n")
        f.write(line + "\n")


# === Administrator Functions ===


def register_user(logged_user):
    """
    For administrator to register a new user.
    Called by display_menu() for option r.
    """

    if logged_user != "admin":
        print("Only admin can register users.")
        return

    new_username = input("Enter the new username: ")

    # Addition of while loop here allows password re-entering
    while True:
        new_password = input("Enter the new password: ")

        # Password verification step
        confirm_password = input("Confirm the new password: ")
        if new_password == confirm_password:

            # Save details to the file using reusable function
            write_newline(f"{new_username}, {new_password}", "user.txt")
            print(f"New user {new_username} registered successfully.")
            break
        else:
            print("Passwords do not match. Please type carefully.")


def complete_tasks():
    """
    For administrator to view completed tasks.
    """

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            found = False
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) != 6:
                    continue  # Skip incomplete lines to avoid errors
                (
                    assign_to,
                    title,
                    descrip,
                    assign_date,
                    due_date,
                    complete,
                ) = parts
                if complete.lower() == "yes":
                    found = True

                    print(
                        f"""
------COMPLETED TASK------
Task:            {title}
Assigned to:     {assign_to}
Assigned date:   {assign_date}
Due date:        {due_date}
Complete:        {complete}
Description:     {descrip}
                    """
                    )

            if not found:
                print("No completed tasks were found.")

    except Exception:
        print("Error reading tasks file.")


def delete_tasks():
    """
    For administrator to delete tasks.
    """

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = f.readlines()

        print("--- TASKS LIST ---")
        for i, line in enumerate(tasks, 1):
            parts = line.strip().split(", ")
            if len(parts) == 6:
                print(
                    f"{i}. Task: {parts[1]} / "
                    f"Team member: {parts[0]} / "
                    f"Due: {parts[4]} / "
                    f"Complete: {parts[5]}\n"
                )

            else:
                print(f"{i}. {line.strip()}")

        # Option to delete tasks
        while True:
            try:
                del_choice = int(
                    input("Enter number of the task to delete or 0 to exit: ")
                )
                if del_choice == 0:
                    return
                elif 1 <= del_choice <= len(tasks):
                    break
                else:
                    print("Invalid number. Type carefully.")
            except ValueError:
                print("Please enter a digit to continue.")

        # Remove the selected task
        deleted_task = tasks.pop(del_choice - 1)

        # Rewrite the file without the deleted task
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for line in tasks:
                f.write(line)
        print("The task was deleted.")

    except Exception as error:
        print("There was a problem deleting a task:", error)


# === General Functions ===


def add_task():
    """
    To prompt the user for new task details.
    Called by display_menu() for option a.
    """

    assign_to = input("Task assigned to: ")
    title = input("Enter the title of the task: ")
    descrip = input("Provide a short description of the task: ")
    assign_date = input("Enter the assigned date (format: 01 Jan 25): ")
    due_date = input("Enter the due date (format: 01 Jan 25): ")

    # Prepare the data for writing
    task_entry = f"{assign_to}, {title}, {descrip}, {assign_date}, {due_date}, No"

    # Add the data to the file
    write_newline(task_entry.strip(), "tasks.txt")
    print("Task added successfully.")


def view_tasks():
    """
    To display all incomplete tasks for the user.
    Called by display_menu() for option va.
    """

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) != 6:
                    continue
                (
                    assign_to,
                    title,
                    descrip,
                    assign_date,
                    due_date,
                    complete,
                ) = parts

                print(
                    f"""
------TASK MANAGER REPORT------
Task:            {title}
Assigned to:     {assign_to}
Assigned date:   {assign_date}
Due date:        {due_date}
Complete:        {complete}
Description:     {descrip}
                """
                )

    except Exception:
        print("System failure imminent. Contact IT Support.")


def my_tasks(username):
    """
    To display tasks for the current user.
    Called by display_menu() for option vm.
    """

    found = False
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) != 6:
                    continue
                (
                    assign_to,
                    title,
                    descrip,
                    assign_date,
                    due_date,
                    complete,
                ) = parts
                if assign_to == username:
                    found = True

                    print(
                        f"""
                          
------TASK MANAGER REPORT------
Task:            {title}
Assigned to:     {assign_to}
Date assigned:   {assign_date}
Due date:        {due_date}
Complete:        {complete}
Description:     {descrip}
                    """
                    )

        if not found:
            print("You have no tasks to do at this time.")

    except Exception:
        print("Critical system failure. Contact IT Support.")


# ==== Login Section ====


def user_login():
    """User access program for Task Manager. Validates the
    username and password using a while loop. Allows different
    access levels for administrator and general users.
    """

    print("Task Manager Login")
    with open("user.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    while True:
        req_username = input("Enter your username: ")
        req_password = input("Enter your password: ")
        found = False
        for line in lines:
            username, password = line.strip().split(", ")
            if req_username == username and req_password == password:
                found = True
                print("You are now logged in.")
                if username == "admin":
                    display_admin_menu(username)
                else:
                    display_user_menu(username)
                return
        if not found:
            print("Invalid username and/or password. Please type nicely.")


# ==== Administrator Interface ====


def display_admin_menu(logged_user):
    """
    Task Manager interface for administrators with extended functionality.
    """

    while True:
        menu = (
            input(
                """
----------- TASK MANAGER -----------
____________________________________
Select one of the following options:
r - Register a new user
a - Add a new task
va - View all tasks
vm - View my tasks
vc - View completed tasks
del - Delete tasks
e - Exit
___________________________________\n
        """
            )
            .strip()
            .lower()
        )

        # --- Register a new user ---
        if menu == "r":
            register_user(logged_user)

        # --- Add a new task ---
        elif menu == "a":
            add_task()

        # --- View all tasks ---
        elif menu == "va":
            view_tasks()

        # --- View my tasks ---
        elif menu == "vm":
            my_tasks(logged_user)

        # --- View completed tasks ---
        elif menu == "vc":
            complete_tasks()

        # --- Delete tasks ---
        elif menu == "del":
            delete_tasks()

        # --- Exit the program ---
        elif menu == "e":
            print("The Task Manager program is now closed.")
            exit()

        else:
            print("You have entered invalid input. Please type slowly.")


# ==== User Interface ====


def display_user_menu(logged_user):
    """Task Manager interface for general users."""

    while True:
        menu = (
            input(
                """
----------- TASK MANAGER -----------
____________________________________
Select one of the following options:
a - Add a new task
va - View all tasks
vm - View my tasks
e - Exit
___________________________________
        """
            )
            .strip()
            .lower()
        )

        # --- Add a new task ---
        if menu == "a":
            add_task()

        # --- View all tasks ---
        elif menu == "va":
            view_tasks()

        # --- View my tasks ---
        elif menu == "vm":
            my_tasks(logged_user)

        # --- Exit the program ---
        elif menu == "e":
            print("The Task Manager program is now closed.")
            exit()

        else:
            print("You have entered invalid input. Please type slowly.")


# Run the program

user_login()


# *References*

# Firzod, S. (2023). Create a python menu to run various commands.
# https://medium.com/@firozkaif27/create-a-python-menu-to-run-various
# -commands-7be4d70cc127

# Galindo, P. (2024). PEP 760 – No More Bare Excepts.
# https://peps.python.org/pep-0760

# Geeks4Geeks. (2025). List Comprehension in Python.
# https://www.geeksforgeeks.org/python-list-comprehension

# Geeks4Geeks. (2024). Python - Output Formatting.
# https://www.geeksforgeeks.org/python-output-formatting

# Hunner, T. (2021). Breaking up long lines of code in Python.
# https://www.pythonmorsels.com/breaking-long-lines-code-python

# llego.dev. (2023). Practical Exercises for Modular Programming in Python.
# https://llego.dev/posts/practical-exercises-modular-programming-python/
# #example-1-geometry-module

# Stack Overflow. (2023). Writing string to a file on a new line every time.
# https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a
# -new-line-every-time

# Stack Overflow. (2014). How do I make a password program in Python 3.4?
# https://stackoverflow.com/questions/26940297/how-do-i-make-a-password
# -program-in-python-3-4

# Van Rossum, G. (2013). Code layout.
# https://peps.python.org/pep-0008/code-lay-out

# Van Rossum, G., Warsaw, B. & Coghlan, N. (2001). PEP 8 – Style Guide for
# Python Code. Python Software Foundation. https://peps.python.org/pep-0008
