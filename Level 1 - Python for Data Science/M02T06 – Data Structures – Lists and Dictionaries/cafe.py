"""Create a stock-handling system for a cafe"""

# Create a list called menu of items sold in the cafe.
menu = ['Cupcake', 'Cake slice', 'Brownie', 'Giant cookie']

# Create a dictionary stock with the stock count for each item on your menu
stock = {'Cupcake': 6, 'Cake slice': 10, 'Brownie': 12, 'Giant cookie': 24}

# Create a dictionary for prices of each item 
price = {'Cupcake': 42, 'Cake slice': 49, 'Brownie': 28, 'Giant cookie': 30}

# Calculate the value of all stock currently held
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print("Total stock worth in the café: R", total_stock)