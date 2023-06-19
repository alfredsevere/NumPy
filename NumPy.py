# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Print the entire array
print("Array:", arr)

# Print the shape of the array
print("Shape:", arr.shape)

# Perform some operations on the array
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Squared:", arr ** 2)

# Create a 2D numpy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the 2D array
print("2D Array:\n", arr_2d)

# Access elements from the 2D array
print("First row:", arr_2d[0])
print("First column:", arr_2d[:, 0])
