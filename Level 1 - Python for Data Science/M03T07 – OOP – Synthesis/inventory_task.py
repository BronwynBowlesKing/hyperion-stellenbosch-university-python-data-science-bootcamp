#========NIKE SHOE INVENTORY MANAGEMENT SYSTEM==========

"""
Underlying functions and a user menu to access a product inventory 
management system.
"""

#========Preparation steps==========

# Import packages
import os
from tabulate import tabulate


# Check the working directory and if the file is accessible 
# for the program
if os.path.exists("inventory.txt"):
    print("The file is available in the working directory.")
    
else:
    print("The file was not found in the working directory:", os.getcwd())
    

#========The beginning of the class==========


class Shoe:
    """
    Initialise the object attributes and data display structures
    for the product inventory management system.  
    """

    def __init__(self, country, code, product, cost, quantity):  
    # Create constructor for the class with critical object variables
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):  
    # Defines how objects are represented as a string when printed. 
        return (f"Country: {self.country}, \nCode: {self.code}," 
                f"\nProduct: {self.product}, \nCost: {self.cost}," 
                f"\nQuantity: {self.quantity}")


#=============Shoe list===========
"""
To store a list of objects of the class Shoe.
"""
shoe_list = []


#==========Functions outside the class==============


def read_shoes_data():
    '''
    This function will open the file inventory.txt and read the data 
    from this file, then create a shoes object with this data and
    append this object into the shoes list. One line in this file 
    represents data to create one object of shoes. 
    '''
    
    try:
        with open("inventory.txt", "r", encoding = "utf-8") as f:
            next(f)  # Skip the header line
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
                else:
                    print(
                        f"Skipped line (wrong format): {line.strip()}"
                    )
    except Exception as error:
        print(f"An error occurred: {error}")
      

# Menu option 1

def view_all():
    '''
    This function will iterate over the shoes list and print the 
    details of the shoes returned from the __str__ function. 
    It organises the data in a table format with the tabulate module.
    '''

# Create a table for the user to view all products in stock
    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    for shoe in shoe_list:
        table.append(
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        )
    print("All products currently in stock are listed below")
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid"))
    

# Menu option 2

def capture_shoes():
    '''
    This function will allow a user to capture data about a shoe and 
    use this data to create a shoe object and append this object 
    inside the shoe list.
    '''

    country = input("What is the country you wish to capture data for? ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    cost = int(input("Enter the product cost: "))
    quantity = int(input("Enter the product quantity: "))
    
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    
    # Below, the file is updated with a special approach to get to a 
    # new line (\n) using seek and tell commands, which move the cursor 
    # for writing to the correct place. 
             
    last_char = ""
    try:
        with open("inventory.txt", "r", encoding = "utf-8") as f:
            f.seek(0, 2)
            if f.tell() > 0:
                f.seek(0)
                content = f.read()
                last_char = content[-1]
    except FileNotFoundError:
        print("Check if the correct file is in the folder.")

    # Now, the program checks for a new line or adds one so that the new  
    # data is not written immediately after the previous data on the same 
    # line

    try:
        with open("inventory.txt", "a", encoding = "utf-8") as f:
            if last_char and last_char != "\n":  
            # Add a new line if needed before writing
                f.write("\n") 
            # Add new line after writing to prevent similar problems    
            f.write(f"{country},{code},{product},{cost},{quantity}\n")  
            print("Stock record updated.")
    except Exception as error:
        print("The file could not be updated. Please try again.")


# Menu option 3

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. It asks the user if 
    they want to add this quantity of shoes and then update it. This 
    quantity is updated on the file. A complex function created to 
    handle restocking for multiple products.
    ''' 
	
	# Find lowest quantity product/s
    min_quantity = min(shoe.quantity for shoe in shoe_list)
    
    # Show all shoes with this low quantity in a table to make it easier 
    # to read
    lowest_quan = [
        shoe for shoe in shoe_list if shoe.quantity == min_quantity
    ]
    print(f"Product/s with the lowest quantity ({min_quantity}):")
    
    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    
    for shoe in lowest_quan:
        table.append(
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        )
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid"))

    # Ask user which product/s to restock based on unique product code.
    if len(lowest_quan) > 1:
        code = input(
            "Enter the product code of the shoe you want to restock: "
        ).strip()
        selected_shoe = next(
            (shoe for shoe in lowest_quan if shoe.code == code), None
        )
        if not selected_shoe:
            print("Invalid code. No restock performed.")
            return
    else:
        selected_shoe = lowest_quan[0]

    # Restock the products
    new_stock = input(
        "Do you want to add stock for this product? (y/n): "
    ).strip().lower()
    if new_stock == "y":
        try:
            add_quan = int(
                input("How many more pairs have arrived as new stock? ")
            )
            selected_shoe.quantity += add_quan
            print(f"Updated quantity: {selected_shoe.quantity}")

            # Update the file based on unique product code. 
            # Both "r" and "w" are used in two separate commands to 
            # read and write to the file here as this turned out to 
            # the safest way to add data without unwanted overwriting.            
            try:
                with open("inventory.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                with open("inventory.txt", "w", encoding="utf-8") as f:
                    for line in lines:
                        parts = line.strip().split(",")
                        if len(parts) == 5 and parts[1] == str(selected_shoe.code):
                            f.write(
                                f"{selected_shoe.country},{selected_shoe.code}," 
                                f"{selected_shoe.product},{selected_shoe.cost},"
                                f"{selected_shoe.quantity}\n"
                            )
                        else:
                            f.write(line)
                print("Stock record updated.")
            except Exception as error:
                print(f"Error updating file: {error}")
        except ValueError:
            print("Invalid quantity entered. Please try again.")
    else:
        print("No stock update has been done on the inventory system.")                          


# Menu option 4

def search_shoe():
    '''
     This function will search for a shoe from the list with the
     shoe code and return this object to be printed.
    '''

    try:
        code = input("Enter the product code to search for: ")
        for shoe in shoe_list:
            if shoe.code == code:
                print(f"Product details found: \n{shoe}")
                return shoe
        print("No product with that code was found.")
        return None  
    except Exception as error:
        print("An error occurred: ", error)
        return None


# Menu option 5
    
def value_per_item():
    '''
    This function will calculate the total value for each item and
    print this information on the console for all stock.
    '''

    table = []
    headers = [
        "Country", "Code", "Product", "Cost", "Quantity", "Total Value"
    ]
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        table.append([
            shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity, total_value
        ])
    print("The value for all stock is listed below")
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid"))
    

# Menu option 6

def highest_qty():
    '''
    Function to determine the product with the highest quantity and
    print this shoe as being for sale. The function handles cases 
    of multiple products. 
    '''

    # Find the highest quantity stock first.
    max_quantity = max(shoe.quantity for shoe in shoe_list)
    
    # Display all shoes with highest quantity 
    highest_quan = [
        shoe for shoe in shoe_list if shoe.quantity == max_quantity
    ]
    print(
        f"The following product/s should go on sale due to high stock level:"
    )
    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    for shoe in highest_quan:
        table.append(
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
            )
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid"))
    

#==========Main Menu=============


def main_menu():
    '''
    A menu that executes the functions above using a while loop.
    '''

    read_shoes_data()  # Load all data at the start.

    while True:
        print("----- NIKE INVENTORY -----")
        print("1. View all products")
        print("2. Add a new product")
        print("3. Restock lowest quantity product")
        print("4. Search for a product by code")
        print("5. View the current total stock value per product")
        print("6. Show product with highest quantity for sale purposes")
        print("0. Exit")
        choice = input("Enter your choice (1 to 6) or 0 to exit: ").strip()

        if choice == "1":
            view_all()
        
        elif choice == "2":
            capture_shoes()
        
        elif choice == "3":
            re_stock()
            
        elif choice == "4":
            search_shoe()
            
        elif choice == "5":
            value_per_item()
            
        elif choice == "6":
            highest_qty()
            
        elif choice == "0":
            print("Thank you for using the Nike Inventory system")
            break
        
        else:
            print("Invalid choice. Please try again.")


# Finally, run the program.

main_menu()



# References

# Firzod, S. (2023). Create a python menu to run various commands.
# https://medium.com/@firozkaif27/create-a-python-menu-to-run-various
# -commands-7be4d70cc127

# Geeks4Geeks. (2025). List Comprehension in Python. 
# https://www.geeksforgeeks.org/python-list-comprehension

# PyPI. (2022). tabulate 0.9.0. https://pypi.org/project/tabulate

# Shaibu, S. (2024). Python New Line: Methods for Code Formatting. 
# https://www.datacamp.com/tutorial/python-new-line

# Stack Overflow. (2023). Writing string to a file on a new line every time.
# https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a
# -new-line-every-time

# Study Tonight. (2021). How to Read a File from Line 2 or Skip the 
# Header Row? https://www.studytonight.com/python-howtos/how-to-read-a-file-
# from-line-2-or-skip-the-header-row

# Van Rossum, G., Warsaw, B. & Coghlan, N. (2001). PEP 8 – Style Guide for 
# Python Code. Python Software Foundation. https://peps.python.org/pep-0008


# Notes on assistance

# My friend Petrus assisted in finding examples of similar code and 
# explaining how lines such as:

# if len(parts) == 5 and parts[1] == str(selected_shoe.code)

# work as I struggled to figure out the right approach in such cases 
# and exactly how certain code works.
