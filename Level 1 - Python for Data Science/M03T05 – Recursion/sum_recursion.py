def adding_up_w_recursion(list, index):
    if index == 0:
        return list[0]  # Base case for index 0 to return first number
    else:
        return list[index] + adding_up_w_recursion(list, index - 1)  # Bring in recursion by returning previous number plus the sum up to previous index

print(f"Recursion result for list of 1 to 10 up to index 9 (10th value): {adding_up_w_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)}")

print(f"Recursion result for list [1, 4, 5, 3, 12, 16] up to index 4 (fifth value): {adding_up_w_recursion([1, 4, 5, 3, 12, 16], 4)}") 

print(f"Recursion result for list [4, 3, 1, 5] up to index 1 (second value): {adding_up_w_recursion([4, 3, 1, 5], 1)}")