"""
*Task Manager Application 3.0*

Task management system for teams.
It allows users to log in, add new tasks, and view assigned tasks.

Administrators have additional access to register new users, view completed
tasks, and delete tasks.

Standard features:
- User registration and authentication with username and password
- Storage of user and task details
- Task reporting, updating and tracking
- Separate access and menus for admin and general users

New features in version 3.0:
- Enhanced task reporting and tracking
- Enhanced user records
- Improved data backup and storage
- Create new databases for reporting:
    * Task Overview (task_overview.txt): Aggregate task reporting
    * User Overview (user_overview.txt): Comprehensive task reporting by user

External data dependencies:
- user.txt: Stores usernames and passwords
- tasks.txt: Stores all task details

"""

# ===== Import modules ===========

import os
from datetime import datetime


# ========Preparation step==========

# Check if the required files are available in the user's working directory
# and handle errors

try:
    with open("user.txt", "r", encoding="utf-8") as f_user, open(
        "tasks.txt", "r", encoding="utf-8"
    ) as f_tasks:
        pass
    print("Welcome to Task Manager 3.0...")

except FileNotFoundError:
    print(
        f"""
        One or both required files ('user.txt', 'tasks.txt') are missing.
        Move these files to your working directory at:
            {os.getcwd()}
        Alternatively, contact IT Support for assistance.
        """
    )
    exit()

except Exception as error:
    print(
        f"""
        An error occurred while accessing the required files:
        {error}
        Please check file permissions or contact IT Support.
        """
    )
    exit()


# === General helper function ===

# Improved line-writing checking from 1.0 and 2.0


def write_newline(line, filename):
    """
    Ensures data is written on a new line in plain text files.
    """

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            if content and not content.endswith("\n"):
                needs_newline = True
            else:
                needs_newline = False

    except FileNotFoundError:
        needs_newline = False

    with open(filename, "a", encoding="utf-8") as f:
        if needs_newline:
            f.write("\n")
        f.write(line + "\n")


# === Administrator Functions ===


def reg_user(logged_user):
    """
    For administrator to register a new user.
    Prevents duplicate usernames and password inconsistency.
    """

    # Load all existing usernames to check for duplicates
    with open("user.txt", "r", encoding="utf-8") as f:
        existing_users = {
            line.strip().split(", ")[0] for line in f if line.strip()
        }  # Dictionary comprehension plus conditional logic

    # Loop until a valid and unique username is entered
    while True:
        new_username = input("Enter the new username: ").strip()
        if not new_username:
            print("Username cannot be empty. Please retry.")
            continue
        if " " in new_username:
            print("Username should not contain spaces. Please retry.")
            continue
        if new_username in existing_users:
            print("Username is already in use. Please choose another one.")
            continue

        # Loop until the new password matches
        while True:
            new_password = input("Enter the new password: ").strip()
            if not new_password:
                print("Password cannot be empty. Please retry.")
                continue
            confirm_password = input("Confirm the new password: ").strip()
            if new_password == confirm_password:
                write_newline(f"{new_username}, {new_password}", "user.txt")
                print(f"New user {new_username} was registered successfully.")
                return
            else:
                print("Passwords do not match. Please retype carefully.")


def view_completed():
    """
    For administrator to view completed tasks.
    """

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            found = False
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
                ) = parts  # Unpack list elements 'backwards'
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

    except FileNotFoundError:
        print("tasks.txt not found. Please check your files.")

    except Exception as error:
        print("Error reading tasks file:", error)


def delete_task():
    """
    For administrator to delete tasks.
    """

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = f.readlines()

        # Display summary of tasks with numbers for selection
        print("\n--- TASKS LIST ---")
        for i, line in enumerate(tasks, 1):
            parts = line.strip().split(", ")
            if len(parts) == 6:
                print(
                    f"""
{i}. Task: {parts[1]} / Team member: {parts[0]} / 
Due: {parts[4]} / Complete: {parts[5]}
"""
                )
            else:
                print(f"{i}. {line.strip()}")

        while True:
            try:
                del_choice = int(
                    input("Enter number of task to delete or -1 to exit):")
                )
                if del_choice == -1:
                    return

                # Check if choice is within range
                elif 1 <= del_choice <= len(tasks):
                    break

                else:
                    print("Invalid number. Type carefully.")

            except ValueError:
                print("Please enter a digit to continue.")

        deleted_task = tasks.pop(del_choice - 1)

        with open("tasks.txt", "w", encoding="utf-8") as f:
            for line in tasks:
                f.write(line)
        print(f"The task was deleted: \n, {deleted_task}")

    except FileNotFoundError:
        print("tasks.txt not found. Please check your files.")

    except Exception as error:
        print("Error with function or tasks file:", error)


# === Reporting functions ===

# Two main functions (gen_report and display_stats) to generate reports
# for the whole team or to display statistics on task completion for a
# certain user. Both main functions have associated helper functions.


def gen_report():
    """
    Main function for administrators to generate task_overview.txt report.
    The report shows aggregate information on task completion for the whole
    team.
    """

    tasks = load_tasks()
    task_stats = pull_task_stats(tasks)
    write_task_overview(task_stats)
    print(
        f"""
          Report generated. See the Task Overview below or view the report
          in this folder now:
          {os.getcwd()}
          """
    )
    
    print(
        f"""
TASK OVERVIEW REPORT
------------------------------------------
Total number of tasks: {task_stats['total']}
Total number of completed tasks: {task_stats['complete']}
Total number of incomplete tasks: {task_stats['incomplete']}
Total number of overdue tasks: {task_stats['overdue']}
Percentage of tasks incomplete: {task_stats['percent_incomp']:.2f}%
Percentage of tasks overdue: {task_stats['percent_overdue']:.2f}%
------------------------------------------
"""
    )


def load_tasks():
    """
    gen_report helper function to load tasks from tasks.txt and return
    a list of task dictionaries.
    """

    tasks = []
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Lines split into components and stored as dictionary
                parts = line.strip().split(", ")
                if len(parts) == 6:
                    tasks.append(
                        {
                            "assign_to": parts[0],
                            "title": parts[1],
                            "descrip": parts[2],
                            "assign_date": parts[3],
                            "due_date": parts[4],
                            "complete": parts[5],
                        }
                    )

    except FileNotFoundError:
        print("tasks.txt not found. Please check your files.")

    except Exception as error:
        print("Error reading tasks file:", error)

    return tasks


def pull_task_stats(tasks):
    """
    gen_report helper function returns a dictionary with statistics for the
    Task Overview Report.
    """

    # Count complete, incomplete, and overdue tasks
    total = len(tasks)
    complete = sum(1 for t in tasks if t["complete"].lower() == "yes")
    incomplete = total - complete

    overdue = 0
    today = datetime.today()
    for t in tasks:
        if t["complete"].lower() == "no":
            try:
                due = datetime.strptime(t["due_date"], "%d %b %y")
                if due < today:
                    overdue += 1
            except Exception:
                continue

    # Calculate percentages and handle division by zero
    percent_incomp = (incomplete / total * 100) if total else 0
    percent_overdue = (overdue / total * 100) if total else 0

    return {
        "total": total,
        "complete": complete,
        "incomplete": incomplete,
        "overdue": overdue,
        "percent_incomp": percent_incomp,
        "percent_overdue": percent_overdue,
    }


def write_task_overview(stats):
    """
    gen_report helper function to write the Task Overview Report to
    task_overview.txt.
    """

    with open("task_overview.txt", "w", encoding="utf-8") as f:
        f.write("TASK OVERVIEW REPORT\n")
        f.write(f"Total tasks: {stats['total']}\n")
        f.write(f"Total completed tasks: {stats['complete']}\n")
        f.write(f"Total incomplete tasks: {stats['incomplete']}\n")
        f.write(f"Total overdue tasks: {stats['overdue']}\n")
        f.write(
            f"Incomplete tasks percentage: {stats['percent_incomp']:.2f}%\n"
        )
        f.write(
            f"Overdue tasks percentage: {stats['percent_overdue']:.2f}%\n"
        )


def display_stats():
    """
    Main function for administrators to view user-disaggregated statistics
    for performance monitoring. Reads user task data, generates
    user_overview.txt, and prints requested data.
    """

    users = load_users()
    tasks = load_tasks()
    stats = pull_user_stats(users, tasks)
    write_user_overview(stats)
    print(
        f"""
          User Overview Report generated. See the overview below or view the
          report in this folder now:
          {os.getcwd()}
          """
    )
    print_user_stats(stats)


def load_users():
    """
    display_stats helper function. Loads all usernames from user.txt
    and returns them as a list.
    """

    users = []
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    username = line.strip().split(", ")[0]
                    users.append(username)

    except FileNotFoundError:
        print("user.txt not found. Please check your files.")

    except Exception as error:
        print("Error reading tasks file:", error)

    return users


def pull_user_stats(users, tasks):
    """
    display_stats helper function. Returns a dictionary with statistics
    for each user as well as aggregate data.
    """

    total_users = len(users)
    tot_tasks = len(tasks)
    today = datetime.today()
    user_stats = {}

    for user in users:
        user_tasks = [t for t in tasks if t["assign_to"] == user]
        num_tasks = len(user_tasks)
        complete = sum(
            1 for t in user_tasks if t["complete"].lower() == "yes"
        )
        incomplete = num_tasks - complete
        overdue = 0
        for t in user_tasks:
            if t["complete"].lower() == "no":
                try:
                    due = datetime.strptime(t["due_date"], "%d %b %y")
                    if due < today:
                        overdue += 1
                except Exception:
                    continue

        percent_assign = (num_tasks / tot_tasks * 100) if tot_tasks else 0
        percent_comp = (complete / num_tasks * 100) if num_tasks else 0
        percent_incomp = (incomplete / num_tasks * 100) if num_tasks else 0
        percent_overdue = (overdue / num_tasks * 100) if num_tasks else 0

        user_stats[user] = {
            "tot_tasks": num_tasks,
            "percent_assign": percent_assign,
            "percent_complete": percent_comp,
            "percent_incomp": percent_incomp,
            "percent_overdue": percent_overdue,
        }

    return {
        "tot_users": total_users, 
        "tot_tasks": tot_tasks, 
        "user_stats": user_stats
    }


def write_user_overview(stats):
    """
    display_stats helper function. Writes the User Overview Report to
    user_overview.txt.
    """

    with open("user_overview.txt", "w", encoding="utf-8") as f:
        f.write("USER OVERVIEW REPORT\n")
        f.write(f"Total number of users: {stats['tot_users']}\n")
        f.write(f"Total number of tasks: {stats['tot_tasks']}\n\n")
        for user, data in stats["user_stats"].items():
            f.write(f"User: {user}\n")
            f.write(f"Total tasks assigned: {data['tot_tasks']}\n")
            f.write(
                f"% of all tasks assigned: {data['percent_assign']:.2f}%\n"
            )
            f.write(f"Complete: {data['percent_complete']:.2f}%\n")
            f.write(f"Incomplete: {data['percent_incomp']:.2f}%\n")
            f.write(f"Overdue: {data['percent_overdue']:.2f}%\n\n")


def print_user_stats(stats):
    """
    display_stats helper function. Prints user statistics.
    """

    print("\nUSER OVERVIEW REPORT")
    print("------------------------")
    print(f"Total number of users: {stats['tot_users']}")
    print(f"Total number of tasks: {stats['tot_tasks']}\n")
    for user, data in stats["user_stats"].items():
        print(f"User: {user}")
        print(f"Total tasks assigned: {data['tot_tasks']}")
        print(
            f"Percentage of all tasks assigned: {data['percent_assign']:.2f}%"
        )
        print(f"Percentage completed: {data['percent_complete']:.2f}%")
        print(f"Percentage incomplete: {data['percent_incomp']:.2f}%")
        print(f"Percentage overdue: {data['percent_overdue']:.2f}%\n")


# === General Functions ===


def add_task():
    """
    To prompt the user for new task details.
    Called by display_menu() for option a.
    Checks if a user exists before accepting new task and validates
    dates for correct scheduling.
    """

    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            users = {
                line.strip().split(", ")[0] for line in f if line.strip()
            }
    except FileNotFoundError:
        print("user.txt not found. Cannot assign tasks at this time.")
        return

    while True:
        assign_to = input("Task assigned to: ").strip()
        if assign_to in users:
            break
        print("Name is not on record. Please enter a registered username.")

    title = input("Enter the title of the task: ").strip()
    descrip = input("Provide a short description of the task: ").strip()    
    assign_date = datetime.today().strftime("%d %b %y")
    assign_dt = datetime.strptime(assign_date, "%d %b %y")
    
    while True:
        due_date = get_valid_date("Enter due date (format: 01 Jan 25): ")
        due_dt = datetime.strptime(due_date, "%d %b %y")    
        if due_dt >= assign_dt:
            break
        print(
            "Due date must be after assigned date. Please re-enter due date."
            )

    task_entry = (
        f"{assign_to}, {title}, {descrip}, {assign_date}, {due_date}, No"
    )

    write_newline(task_entry.strip(), "tasks.txt")
    print("Task added successfully.")


def get_valid_date(prompt):
    """
    add_task helper function to validate dates.
    """

    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%d %b %y")
            return date_str
        except ValueError:
            print("Invalid date format. Please use format: 01 Jan 25).")


def view_all():
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

    except FileNotFoundError:
        print("tasks.txt not found. Please check your files.")

    except Exception as error:
        print("Error reading tasks file:", error)


def view_mine(username):
    """
    Display tasks for the current user, allow them to mark as complete or
    edit. Called by display_menu() for option vm.
    """

    def get_valid_task_num(user_tasks):
        """
        Recursively prompt the user for a valid task number or to enter -1
        to return.
        """

        selection = input(
            "Enter number of the task to edit or -1 to return to main menu:"
        )
        # Base case is set here for user to return to previous menu
        if selection == "-1":
            return None
        # Verify input is a number and in designated range
        if selection.isdigit() and 1 <= int(selection) <= len(user_tasks):
            return int(selection) - 1
        print("Invalid selection. Please try again.")
        # Recursive call
        return get_valid_task_num(user_tasks)

    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f if line.strip()]

        user_tasks = pull_user_tasks(username, tasks)
        if not user_tasks:
            print("You have no tasks to do at this time!")
            return

        display_user_tasks(user_tasks)
        task_num = get_valid_task_num(user_tasks)
        if task_num is None:
            return

        task_index, parts = user_tasks[task_num]
        manage_task(tasks, task_index, parts)

    except FileNotFoundError:
        print("tasks.txt not found. Please check your files.")

    except Exception as error:
        print("Error reading tasks file:", error)


# view_mine helper functions


def pull_user_tasks(username, tasks):
    """
    view_mine helper function to retrieve user's tasks.
    """

    for task in tasks:
        if not isinstance(task, str):
            print("Non-string in tasks:", task, type(task))

    return [  # List comprehension with conditions
        (index, line.split(", "))
        for index, line in enumerate(tasks)
        if isinstance(line, str)
        and len(line.split(", ")) == 6
        and line.split(", ")[0] == username
    ]


def display_user_tasks(user_tasks):
    """
    view_mine helper function to display user's tasks.
    """

    print("\n------ YOUR TASKS ------")
    for num, (task_index, parts) in enumerate(user_tasks, 1):
        assign_to, title, descrip, assign_date, due_date, complete = parts
        print(
            f"""{num}. Task: {title}
   Assigned to: {assign_to}
   Date assigned: {assign_date}
   Due date: {due_date}
   Complete: {complete}
   Description: {descrip}
"""
        )


def manage_task(tasks, task_index, parts):
    """
    view_mine helper function to edit and update task records.
    """

    assign_to, title, descrip, assign_date, due_date, complete = parts
    print(f"\nSelected Task: {title}")
    print("Options:\n1 - Mark complete\n2 - Edit task\n-1 - Return to menu")
    action = input("Choose an option: ").strip()
    if action == "1":
        if complete.lower() == "yes":
            print("Task is already marked complete.")
        else:
            parts[5] = "Yes"
            tasks[task_index] = ", ".join(parts)
            with open("tasks.txt", "w", encoding="utf-8") as f:
                for line in tasks:
                    f.write(line + "\n")
            print("Task marked complete.")
    elif action == "2":
        if complete.lower() == "yes":
            print(
                "Completed tasks cannot be edited."
            )
            return
        new_user = input(
            "Enter a new user to assign or press Enter to cancel: "
        ).strip()
        if new_user:
            if new_user not in load_users():
                print("Invalid or unregistered user.")
                return
            parts[0] = new_user
        new_due = input(
            "Enter a new due date or press Enter to cancel: "
        ).strip()
        if new_due:
            parts[4] = new_due
        tasks[task_index] = ", ".join(parts)
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for line in tasks:
                f.write(line + "\n")
        print("Task updated.")
    elif action == "-1":
        return
    else:
        print("Invalid option. Try again please.")


# ==== Login Section ====


def user_login():
    """
    User access program for Task Manager. Validates the
    username and password using a while loop. Allows different
    access levels for administrator and general users.
    """

    # Read all users and passwords
    print(">> Task Manager Login <<")
    with open("user.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Loop until correct details are entered
    while True:
        req_username = input("Enter your username: ").strip()
        req_password = input("Enter your password: ").strip()
        found = False
        for line in lines:
            username, password = line.strip().split(", ")
            if req_username == username and req_password == password:
                found = True
                print("You are now logged in.")
                # Direct user to admin or general menu based on username
                if username == "admin":
                    display_admin_menu(username)
                else:
                    display_user_menu(username)
                return
        if not found:
            print("Invalid username and/or password. Please retype.")


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
vm - View and manage my tasks
vc - View completed tasks
del - Delete tasks
gr - Generate reports 
ds - Display statistics 
e - Exit
___________________________________\n
        """
            )
            .strip()
            .lower()
        )

        # --- Register a new user ---
        if menu == "r":
            reg_user(logged_user)

        # --- Add a new task ---
        elif menu == "a":
            add_task()

        # --- View all tasks ---
        elif menu == "va":
            view_all()

        # --- View my tasks ---
        elif menu == "vm":
            view_mine(logged_user)

        # --- View completed tasks ---
        elif menu == "vc":
            view_completed()

        # --- Delete tasks ---
        elif menu == "del":
            delete_task()

        # --- Generate reports ---
        elif menu == "gr":
            gen_report()

        # --- Display statistics ---
        elif menu == "ds":
            display_stats()

        # --- Exit the program ---
        elif menu == "e":
            print("The Task Manager program is now closed.")
            exit()

        else:
            print("You have entered invalid input. Please retype.")


# ==== General User Interface ====


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
___________________________________\n
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
            view_all()

        # --- View my tasks ---
        elif menu == "vm":
            view_mine(logged_user)

        # --- Exit the program ---
        elif menu == "e":
            print("The Task Manager program is now closed.")
            exit()

        else:
            print("You have entered invalid input.")


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

# Python Software Foundation. (2025). 6.13. Conditional expressions.
# https://docs.python.org/3/reference/expressions.html#conditional-expressions

# Python Software Foundation. (2025). datetime — Basic date and time types.
# https://docs.python.org/3/library/datetime.html

# Python Software Foundation. (2025). Dictionary comprehension.
# https://docs.python.org/3/glossary.html#term-dictionary-comprehension

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
