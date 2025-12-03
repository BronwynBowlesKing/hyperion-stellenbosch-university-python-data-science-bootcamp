import numpy as np

## i. Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)
## create a two-dimensional array? Rewrite it correctly. 

# () are used instead of [] to create a list.  dtype=float is also 
# in the wrong place. It should be outside the lists.

# Correction:

np_array1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype = float)
print(f"np_array1: \n{np_array1}")

# Print array:
# np_array1: 
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


## ii. What is the difference between a = np.array([0, 0, 0]) and 
## a = np.array([[0, 0, 0]])?

# np.array([[0, 0, 0]]) (np_array3) with double [] is a nested list
# and np.array([0, 0, 0]) (np_array2) is simple list. This gives 
# np_array2 below one dimension and np_array3 two dimensions. 

# We can show this with .ndim:

np_array2 = np.array([0, 0, 0])
np_array3 = np.array([[0, 0, 0]]) 
print(f'np_array2 dimensions: {np_array2.ndim}')
print(f'np_array3 dimensions: {np_array3.ndim}')


## iii. Create a 3 by 4 by 4 array using the following code: 
## array = np.linspace(1, 48, 48).reshape(3, 4, 4).

np_array4 = np.linspace(1, 48, 48).reshape(3, 4, 4)

print(f"np_array4: \n{np_array4}")

    # Understanding this array:

    # np.linspace(1, 48, 48) creates an array of 48 numbers from 1 to
    # 48. It includes the last number because np.linspace is designed 
    # that way.

    # reshape(3, 4, 4) reshapes the 1D array into a 3D one. 
    # (3, 4, 4) gives 3 groups of 4 rows each to make the second
    # dimension. Each row has 4 columns as the third dimension.


## iv. Index or slice this array to obtain the following:

## 1. 20.0

print(
f'''
np_array4[1, 0, 3] = {np_array4[1, 0, 3]}
'''
)


## 2. [ 9. 10. 11. 12.]

print(
f'''
np_array4[0, 2] = {np_array4[0, 2]}
'''
)


## 3. [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] 
# [45. 46. 47. 48.]]

print(
f'''
np_array4[2] = 
{np_array4[2]}
'''
)


## 4. [[5. 6.] [21. 22.] [37. 38.]]

print(
f'''
np_array4[0, 1, 0:2] [1, 1, 0:2] [2, 1, 0:2] = 
{np_array4[0, 1, 0:2]} {np_array4[1, 1, 0:2]} {np_array4[2, 1, 0:2]}
'''
)


## 5. [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]

print(
f''' 
np_array4[2, 0, -2:] [2, 1, -2:]; [2, 2, -2:] [2, 3, -2:] =
{np_array4[2, 0, -2:]} {np_array4[2, 1, -2:]} 
{np_array4[2, 2, -2:]} {np_array4[2, 3, -2:]}
'''
)


## 6. [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]

print(
f''' 
np_array4[0, :, 0][::-1] [1, :, 0][::-1] [2, :, 0][::-1] = 
{np_array4[0, :, 0][::-1]} {np_array4[1, :, 0][::-1]} 
{np_array4[2, :, 0][::-1]}
'''
)


## 7. [[1. 4.] [45. 48.]]

print(
f''' 
np_array4[0, 0, [0, -1] [2, 3, [0, -1]] = 
{np_array4[0, 0, [0, -1]]} {np_array4[2, 3, [0, -1]]} 
'''
)


## 8. [[25. 26. 27. 28.] [29. 30. 31. 32.] [33. 34. 35. 36.]
# [37. 38. 39. 40.]]

print(
f''' 
np_array4[1, 2:4] [2, 0:2] = 
{np_array4[1, 2:4]} {np_array4[2, 0:2]} 
'''
)



# References 

# HyperionDev. (2025). Data Structures – Lists and Dictionaries. 
# Course materials. Private repository, GitHub.

# HyperionDev. (2025). NumPy Basics. Course materials. 
# Private repository, GitHub.

# HyperionDev. (2025). The String and Numerical Data Types. 
# Course materials. Private repository, GitHub.