def find_largest_num(list):
    if len(list) == 1:
        return list[0]  # Base case is defined for a list with just one number   
    max_num = find_largest_num(list[1:])  # Recursive case comparing rest of list and eventually find max_num 
    return list[0] if list[0] > max_num else max_num

# [1:] is all elements of the list except the first one. Function calls itself to check this smaller list until only one element is left (the base case).
# The final result is max_num.

print(f"The largest number in the list [6, 4, 5, 3] is: {find_largest_num([6, 4, 5, 3])}.")

print(f"The largest number in the list [3, 1, 6, 8, 2, 4, 5] is: {find_largest_num([3, 1, 6, 8, 2, 4, 5])}.")