# A challenging assignment that I need much help for. I wrote the code as best I could on my own
# and then asked a friend, Petrus, to give me some feedback. After several attempts I went back to him
# and he helped me clean up some of the things it was doing that it is not supposed to like errors 
# with messages displayed to the user and incorrect logic. 

"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:
    
    # Initialise the instance variables for each email.
    def __init__ (self, email_address, sub_line, email_content):
        self.email_address = email_address 
        self.sub_line = sub_line
        self.email_content = email_content
        self.has_been_read = False

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    inbox_content = [
        ("welcome@email.com", "Get started with email settings", "Dear user,\nIt's time to choose your email settings. Click on the link below to access the settings page:\nhttps://youremailsettings.com"), 
        ("welcome@email.com", "Set-up a personalised email signature", "Dear user, \nHave you set up your personal email signature? Click the link below to open the personal signature set-up page: \nhttps://personalemailsignature.com"), 
        ("john_t@gmail.com", "Greetings!", "Hey there, \nThanks for sharing your new email address. I'll be in touch again soon.")]
    for email_address, sub_line, email_content in inbox_content:
        emails.append(Email(email_address, sub_line, email_content))

def list_emails():
# Create a function that prints each email's subject line
# alongside its corresponding index number,
# regardless of whether the email has been read.
    for index, email in enumerate(emails):
        print(f"{index} {email.sub_line}")   

def read_email(index):
# Create a function that displays the email_address, subject_line,
# and email_content attributes for the selected email.
# After displaying these details, use the 'mark_as_read()' method
# to set its 'has_been_read' instance variable to True.
    try:
        email = emails[index]
        print(f"Sender: {email.email_address}")
        print(f"Subject: {email.sub_line}")
        print(f"{email.email_content}")
        email.mark_as_read()
    except IndexError:
        print("Enter one of the email index numbers. ")

def view_unread_emails():
# Create a function that displays all unread Email object subject lines
# along with their corresponding index numbers.
# The list of displayed emails should update as emails are read.
    email_unread = False 
    for index, email in enumerate(emails):
        if not email.has_been_read:
            print(f"{index} {email.sub_line}")
            email_unread = True
        if not email_unread:
            print("You have no unread emails right now.")

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
emails = []

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
    # Logic here to read an email
        list_emails()
        try:
            index = int(input("Enter email index number please: "))
            read_email(index)
        except ValueError:
            print("Please try again to enter an index number.")

    elif user_choice == 2:
        # Logic to view unread emails
        print("Your unread emails are below:\n")
        view_unread_emails()

    elif user_choice == 3:
        # Lgic to quit app
        print("Email box closed.")
        break

    else:
        print("Make another selection please. ")