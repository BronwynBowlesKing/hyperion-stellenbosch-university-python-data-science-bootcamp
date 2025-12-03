## Sequential/linear search and example
# This approach is used when the elements are in a random order, such as a list of prices entered at random that need to be sorted from highest to lowest.

def linear_search(target, items): 
    
    # Iterate over the list. If we find the target item, return its index 
    for index in range(len(items)): 
        if items[index] == target: 
            return index 
        # If the target item is not found, return None
    return None 

num_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9
result = linear_search(target_item, num_list)

if result is not None: 
    print(f"Item {target_item} found at index {result}.") 
else: 
    print(f"Item {target_item} not found in the list.")


## Insertion sort function and example

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        # Move elements of numbers[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

# Uses num_list above again
sorted_list = insertion_sort(num_list)
print(sorted_list)  


## Binary search function and example
# The binary search is suitable when a list is sorted and one has some idea of where the target element is. Splitting the list up and searching around the midpoint is a suitable approach here and is used on sorted_list. This can be used when searching an alphabetical dictionary in Python.

def binary_search(target, items): 
    low, high = 0, len(items) - 1 

    # Keep iterating until the low and high cross 
    while high >= low: 
        # Find midpoint 
        mid = (low + high) // 2 

        # If item is found at midpoint, return its index 
        if items[mid] == target: 
            return mid 
        # Else, if item at midpoint is less than target, search the second half of the list 
        elif items[mid] < target: 
            low = mid + 1 
        # Else, search the first half 
        else: high = mid - 1 
        # Returns None if item not found 
        
    return None 

# Uses sorted_list from above
target_item = 9 
result = binary_search(target_item, sorted_list)

if result is not None: 
    print(f"Item {target_item} found at index {result}.") 
else: 
    print(f"Item {target_item} not found in the list.")
