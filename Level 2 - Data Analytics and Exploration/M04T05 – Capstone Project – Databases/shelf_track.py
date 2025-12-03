"""
>> Welcome to *SHELF TRACKER* <<

This script, shelf_track.py, is the executable file for the bookstore
manager SHELF TRACKER (ST). 

As a relational database manager, ST has the following features: 

    * Inventory logging as well as author tracking.

    * CRUD operations for book and author records with data 
    validation and error handling.

    * Maintains consistency in bookstore records.

    * The ST database is called 'ebookstore'. The database structure 
    includes the tables 'book' and 'author'.

>> Important notes for new bookstore set-ups <<

    Every bookstore that uses the ST system carries copies of books in
    the African Author Stars (AAS) collection. To optimise setting up a
    new bookstore, the AAS collection and its authors are automatically
    added to a new database at set-up. 
    
    Additionally, the ST system is shipped with a full AAS book set as
    minimum start-up stock. These minimum quantities are also
    automatically populated in the system.
    
    Please verify your actual stock quantities received against the
    digital record and update the system if necessary.

"""


# === Import packages ===

import os
import sqlite3
from tabulate import tabulate


# === Helper function to insert new rows in any table ===


def insert_rows(db, table, columns, values_list, message=None):
    """
    A helper function to insert one or more new rows into any table.
    """

    try:
        cursor = db.cursor()
        placeholders = ', '.join(['?'] * len(columns))
        columns_data = ', '.join(columns)
        add_row = (
            f"INSERT INTO {table} ({columns_data}) VALUES ({placeholders})"
        )
        cursor.executemany(add_row, values_list)
        db.commit()

        if message:
            print(message)
        else:
            print(f"{len(values_list)} new row/s added to '{table}' table.")

    except sqlite3.IntegrityError:
        print(
            f"One or more records with ID already exists in '{table}' table."
        )

    except sqlite3.Error as error:
        print(f"An error occurred while adding the record: {error}.")


# === Define function to create the database ===


def database_initiator():
    '''
    To initialise ebookstore database if it is not already created
    or show that it already exists.
    '''

    db_exists = os.path.exists("ebookstore.db")

    try:
        db = sqlite3.connect("ebookstore.db")

        # To protect foreign key relationships:
        db.execute("PRAGMA foreign_keys = ON;")

        if db_exists:
            print("The database 'ebookstore.db' already exists.")
        else:
            print("A new database 'ebookstore.db' has been created.")
        return db
    
    except sqlite3.Error as error:
        print(f"An error occurred: {error}.")
        return None


# === Functions to create 'book' and 'author' tables ===

"""
PRIMARY KEYS

The following two attributes/columns have the same name but are 
distinct primary keys:
 
    * In table 'book', the primary key is 'id' (book.id).
    * In table 'author', the primary key is 'id' (author.id)

'book_id' and 'author_id' are used where necessary to 
differentiate them.

FOREIGN KEYS

'authorID' in the 'book' table (book.authorID) is a foreign key that 
creates a relationship with the 'author' table. Thus, book.authorID 
is the equivalent of author.id, stores the same data, and connects 
the two tables.
"""


def create_book_table(db):
    '''
    To create the table 'book' to store the book id numbers, titles,
    authors and quantities in stock.
    '''
    
    try:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY UNIQUE,
                title TEXT,
                authorID INTEGER,
                qty INTEGER,
                FOREIGN KEY (authorID) REFERENCES author(id)
            )
        ''')
        db.commit()
        print("The table 'book' has been created in the database.")
    
    except sqlite3.Error as error:
        print(
            f"An error occurred while creating 'book' table: {error}."
        )


def create_author_table(db):
    '''
    To create the table 'author' to store the author id number, name
    and country of origin.
    '''

    try:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS author (
                id INTEGER PRIMARY KEY UNIQUE,
                name TEXT,
                country TEXT
            )
        ''')
        db.commit()
        print("The table 'author' has been created in the database.")

    except sqlite3.Error as error:
        print(
            f"An error occurred while creating 'author' table: {error}."
        )


# === Function to populate records for new bookstore at start-up ===


def default_stock(db):
    '''
        To automatically populate a new ST ebookstore database at 
        start-up with default stock from the AAS collection.  
    '''

    aas_authors = [
        (101, "Michelle Nkamankeng", "South Africa"),
        (102, "Adaeze Atuegwu", "Nigeria"),
        (103, "Anisha Namutowe", "Zambia"),
        (104, "Novuyo Rosa Tshuma", "Zimbabwe"),
        (105, "Jack Mapanje", "Malawi")
    ]

    aas_books = [
        (20001, "Waiting for the Waves", 101, 10),
        (20002, "Fate", 102, 10),
        (20003, "Echoes of Betrayal", 103, 12),
        (20004, "Digging Stars", 104, 8),
        (20005, "And Crocodiles Are Hungry at Night", 105, 12)
    ]

    insert_rows(
        db, 'author', ('id', 'name', 'country'), aas_authors,
    )
    insert_rows(
        db, 'book', ('id', 'title', 'authorID', 'qty'), aas_books,
        message="African Author Stars collection start-up stock captured."
    )


# === User functions to add new entries to 'book' and 'author' tables ===


def new_book(db):
    """
    To input new book details as a row in the 'book' table. 
    Menu option 1.1.
    """

    try:
        book_id = int(input("Enter the new book ID: "))
        title = input("Enter the book's full title: ")
        author_id = int(input("Enter the author's ID: "))
        qty = int(input("Enter the quantity currently in stock: "))

         # Insert the new book with helper function 
        insert_rows(
            db,
            'book',
            ('id', 'title', 'authorID', 'qty'),
            [(book_id, title, author_id, qty)]
        )

    except ValueError:
        print(
            '''Please enter correct data types as follows:
                    - Book ID, Author ID and Quantity as digits only.
                    - Book title as alphabet characters only.
            '''
        )


def new_author(db):
    """
    To input new author details as a row in the 'author' table.
    Menu option 1.2.
    """

    try:
        author_id = int(input("Enter the new author ID: "))
        author_name = input("Enter the author's name: ")
        author_country = input("Enter the author's country of origin: ")

        insert_rows(
            db,
            'author',
            ('id', 'name', 'country'),
            [(author_id, author_name, author_country)]
        )
    except ValueError:
        print(
            '''Invalid input. Please enter correct data types as follows:
                   - Author ID as digits only.
                   - Author name and Country as alphabet characters only.
            '''
        )


# === Function to update stock ===


def update_stock(db):
    """
    Update the stock quantity of a book. Menu option 2.
    """

    try:
        book_id = int(input("Enter the Book ID to update stock: "))
        qty = int(input("Enter the new stock quantity: "))
        cursor = db.cursor()
        cursor.execute(
            "UPDATE book SET qty = ? WHERE id = ?",
            (qty, book_id)
        )
        db.commit()

        if cursor.rowcount:
            print("Stock quantity updated successfully.")

        else:
            print("No record was found with the input book ID.")

    except ValueError:
        print("Invalid input. Enter digits only for Book ID and Quantity.")

    except sqlite3.Error as error:
        print(f"An error occurred while updating the stock: {error}.")


# === Functions to update database entries ===


def edit_book(db):
    """
    To update book records if they contain errors. Menu option 3.1.
    User must enter the book ID to find the record to update. 
    """

    try:
        book_id = int(input("Enter the Book ID to update a book record: "))
        print("What part of the book record would you like to correct?")
        print("1. Book title ")
        print("2. Author ID ")
        print("3. Book title and Author ID ")
        choice = input("Enter your selection please: ").strip()

        cursor = db.cursor()

        if choice == "1":
            title = input("Enter the correct title: ")
            cursor.execute(
                "UPDATE book SET title = ? WHERE id = ?",
                (title, book_id)
            )

        elif choice == "2":
            author_id = int(input("Enter new author ID: "))
            cursor.execute(
                "UPDATE book SET authorID = ? WHERE id = ?",
                (author_id, book_id)
            )

        elif choice == "3":
            title = input("Enter new title: ")
            author_id = int(input("Enter new author ID: "))
            cursor.execute(
                "UPDATE book SET title = ?, authorID = ? WHERE id = ?",
                (title, author_id, book_id)
            )
        
        else:
            print("Invalid selection. Please try again.")
            return

        db.commit()
        print("The book record was updated successfully.")

    except ValueError:
        print(
            '''
            Invalid input. Please enter the correct data type:
                - Book ID and Author ID as digits only.
                - Book title as alphabet characters only.
            '''
        )

    except sqlite3.Error as error:
        print(f"An error occurred while updating the book: {error}.")


def edit_author(db):
    """
    Update author records if they contain errors. Menu option 3.2.

    """

    cursor = db.cursor()
    try:
        author_id = input("Enter the Author ID: ")
        cursor.execute("SELECT id, name, country FROM author WHERE id = ?", (author_id,))
        author = cursor.fetchone()
        if not author:
            print("Author not found.")
            return

        print(f"Current Name: {author[1]}")
        print(f"Current Country: {author[2]}")
        new_name = input(
            "Enter new name or leave blank to keep the current one: "
        )
        new_country = input(
            "Enter new country or leave blank to keep the current one: "
        )

        # Use current values if input is blank
        updated_name = new_name if new_name.strip() else author[1]
        updated_country = new_country if new_country.strip() else author[2]

        cursor.execute(
            "UPDATE author SET name = ?, country = ? WHERE id = ?",
            (updated_name, updated_country, author_id)
        )
        db.commit()
        print("Author details updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the author: {e}")


# === Function to delete book entries ===


def delete_book(db):
    """
    Delete a book from the database based on book ID. Menu option 4.
    Includes validation to check if the book exists and asks for 
    confirmation.
    """

    try:
        book_id = int(input("Enter the Book ID to delete: "))
        cursor = db.cursor()
        cursor.execute("SELECT title FROM book WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if not result:
            print("No record was found with the input Book ID.")
            return

        title = result[0]
        confirm = input(
            f"Are you sure you want to permanently delete '{title}'? (y/n): "
        ).strip().lower()
        if confirm != 'y':
            print("Deletion cancelled.")
            return

        cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
        db.commit()

        if cursor.rowcount:
            print("Book deleted successfully.")

        else:
            print("An error occurred. Book was not deleted.")

    except ValueError:
        print("Invalid input. Please enter a valid Book ID with digits only.")

    except sqlite3.Error as error:
        print(f"An error occurred while trying to delete an entry: {error}.")


# === Functions to search for a book, author or view all books ===


def search_books(db):
    """
    To search for books by book id, title, author id or author name. 
    Menu option 5.1. Allows full and partial matches for book titles
    and author names. 
    """
    
    print("Search for book by:")
    print("1. Book ID")
    print("2. Title")
    print("3. Author ID")
    print("4. Author name")
    choice = input("Enter your choice from 1 to 4: ").strip()

    query = ""
    pm = ()

    if choice == "1":
        book_id = input("Enter the book ID: ").strip()
        query = "SELECT * FROM book WHERE id = ?"
        pm = (book_id,)
    
    elif choice == "2":
        title = input(
            "Enter the book title. Partial matches are possible: "
        ).strip()
        query = "SELECT * FROM book WHERE title LIKE ?"
        pm = (f"%{title}%",)
    
    elif choice == "3":
        author_id = input("Enter the author ID: ").strip()
        query = "SELECT * FROM book WHERE authorID = ?"
        pm = (author_id,)

    elif choice == "4":
        author_name = input(
            "Enter the author name. Partial matches are possible: "
        ).strip()
        query = """
            SELECT book.id, book.title, book.authorID, book.qty
            FROM book
            JOIN author ON book.authorID = author.id
            WHERE author.name LIKE ?
        """
        pm = (f"%{author_name}%",)
    
    else:
        print("Invalid selection. Please try again.")
        return

    cursor = db.cursor()
    cursor.execute(query, pm)
    results = cursor.fetchall()

    if results:
        print("\nBook/s found:")

        # Format specifiers used to display returned data
        print("" \
        "{:<8} {:<40} {:<10} {:<8}".format("ID", "Title", "AuthorID", "Qty")
        )
        # Dashes as a visual separator
        print("-" * 70)
        for row in results:
            print(
                "{:<8} {:<40} {:<10} {:<8}".format(row[0], row[1], row[2], row[3])
            )

    else:
        print("No matching book/s found.") 


def search_authors(db):
    """
    Search for author by ID, name, or country. Menu option 5.2. 
    Allows full and partial matches for name and country.
    """

    print("Search for author by:")
    print("1. Author ID")
    print("2. Author name")
    print("3. Author country")
    choice = input("Enter your choice (1-3): ").strip()

    cursor = db.cursor()
    query = ""
    params = ()

    if choice == "1":
        author_id = input("Enter the author ID: ").strip()
        query = "SELECT id, name, country FROM author WHERE id = ?"
        params = (author_id,)

    elif choice == "2":
        name = input(
            "Enter the author name. Partial matches are possible: "
        ).strip()
        query = "SELECT id, name, country FROM author WHERE name LIKE ?"
        params = (f"%{name}%",)

    elif choice == "3":
        country = input(
            "Enter the author country. Partial matches are possible: "
        ).strip()
        query = "SELECT id, name, country FROM author WHERE country LIKE ?"
        params = (f"%{country}%",)

    else:
        print("Invalid selection. Please try again.")
        return

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        print("\nAuthor/s found:")
        print("{:<8} {:<30} {:<20}".format("ID", "Name", "Country"))
        print("-" * 60)
        for row in results:
            print("{:<8} {:<30} {:<20}".format(row[0], row[1], row[2]))
    else:
        print("No matching authors found.")


def all_books(db):
    """
    Display all book records at once with book id and title, author id,
    name and country, and quantity in stock. Menu option 6.
    """

    cursor = db.cursor()
    cursor.execute("""
        SELECT book.id, book.title, author.name, author.id, author.country, qty
        FROM book
        JOIN author ON book.authorID = author.id
        ORDER BY book.id
    """)

    records = cursor.fetchall()

    if not records:
        print("No books were found in the database.")
        return

    # Place records in individual blocks
    print("\nALL TITLES IN STOCK")
    for record in records:
        headers = [
            "Book ID", 
            "Title", 
            "Author Name", 
            "Author ID", 
            "Author Country", 
            "Quantity in Stock"
            ]
        
        print("+" + "-" * 60 + "+")  # Top border
        for header, value in zip(headers, record):
            print(f"| {header:<21}: {str(value):<36}|")  # Rows
        print("+" + "-" * 60 + "+\n")  # Bottom border


# === User menu functions ===


def show_menu():
    menu = [
        ["1", "Enter new book or author details"],
        ["2", "Update book stock record"],
        ["3", "Update a book or author record"],
        ["4", "Delete a book record"],
        ["5", "Search for a book or author"],
        ["6", "View details of all books"],
        ["0", "Exit"]
    ]
    print("Shelf Tracker Menu")
    print(
        tabulate(
            menu, headers=["Option", "Description"], tablefmt="fancy_grid"
            )
        )


def main():

    db = database_initiator()
    create_author_table(db)
    create_book_table(db)
    default_stock(db)
    print("SHELF TRACKER is ready to be used.")

    while True:
        show_menu()

        # Menu options and sub-choices
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\n1. Add new book")
            print("2. Add new author")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                new_book(db)
            elif sub_choice == "2":
                new_author(db)
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "2":
            update_stock(db)
        
        elif choice == "3":
            print("\n1. Edit details of a book record")
            print("2. Edit details of an author record")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                edit_book(db)
            elif sub_choice == "2":
                edit_author(db)
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "4":
            delete_book(db)

        elif choice == "5":
            print("\n1. Search for a book")
            print("2. Search for an author")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                search_books(db)
            elif sub_choice == "2":
                search_authors(db)
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "6":
            all_books(db)

        elif choice == "0":
            print("SHELF TRACKER is closed.")
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")


# === Run the program ===

main()



# === References ===

# GeeksforGeeks. (2024). Python String Formatting - How to format String?
# https://www.geeksforgeeks.org/string-formatting-in-python

# Geeks4Geeks. (2024). Python - Output Formatting.
# https://www.geeksforgeeks.org/python-output-formatting

# Holywell, S. (n.d.). SQL Style Guide. https://www.sqlstyle.guide 

# HyperionDev. (2025a). Databases: Task. Course materials. Private repository, 
# GitHub.

# HyperionDev. (2025b). Relational Databases: Task. Course materials. 
# Private repository, GitHub.

# Marasinghe, K. (2024). From SQL to Object-Oriented Databases: 
# Navigating the Evolution of Database Models. 
# https://dev.to/kaweeshamr/from-sql-to-object-oriented-databases-navigating-
# the-evolution-of-database-models-m80  

# Microsoft Learn. (2023). Sqlite database errors. https://learn.microsoft.com
# /en-us/dotnet/standard/data/sqlite/database-errors

# Mimo. (2025). Docstrings. https://mimo.org/glossary/python/docstrings

# Muralidhar, KSV. (2024). How to Merge Two Tables in SQL. Built-In.
# https://builtin.com/articles/sql-merge-two-tables

# Python Software Foundation. (2025). sqlite3 — DB-API 2.0 interface for 
# SQLite databases. https://docs.python.org/3/library/sqlite3.html

# SQLite Tutorial. (2015). SQLite Python: Inserting Data. 
# https://www.sqlitetutorial.net/sqlite-python/insert

# SQLite Tutorial. (2015). SQLite Foreign Key. 
# https://www.sqlitetutorial.net/sqlite-foreign-key

# Van Rossum, G., Warsaw, B. & Coghlan, N. (2001). PEP 8 – Style Guide for
# Python Code. Python Software Foundation. https://peps.python.org/pep-0008