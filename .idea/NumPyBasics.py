#This program is made by Bryan Liem. This program should answer 10 problems listed in
#the assignment.
#Imports the NumPy module as np.
import numpy as np

#Prints the current NumPy verrsion number.
print(np.__version__)

#Creates a 1D array filled with 10 zeros and prints it.
array1 = np.zeros(10)
print(array1)
#Uses array slicing to set the 5th and 7th elements to 5 and prints it.
array1[4:7] = 5
print(array1)

#Creates a 1D array with elemnts from 11 to 99 and prints it.
array2 = np.arange(11, 100, 1)
print(array2)

#Creates a 1D array with 10 elements with random values from 11 to 99 and prints it.
array3 = np.random.randint(11, 100, size=10)
print(array3)

#Creates and reshapes 3*3 matrix with ordered numbers from 0 to 8 and prints it.
array4 = np.arange(0, 9, 1).reshape(3, 3)
print(array4)

#Creates an array and prints out the indices where its value is not 0.
array5 = np.array([1, 2, 0, 0, 4, 0])
print(np.where(array5 > 0))

#Creates a 3*3 identity matrix and prints it.
array6 = np.eye(3)
print(array6)

#Creates a 5*5 matrix of 0s and prints it.
array7 = np.zeros([5, 5])
print(array7)
#Changes the first column and last row of the matrix to be filled with 5s and prints it.
array7[:4, :1] = 5
array7[4] = 5
print(array7)

#Creates an 8*8 matrix and fills it with a checkerboard pattern and prints it.
array8 = np.zeros([8, 8])
i = 1
#Using variable i as an indicator for each row, changes the contents to an alternating 1
#pattern depending on if the row is odd or even.
for row in array8:
    if i % 2 == 1:
        row[[1, 3, 5, 7]] = 1
    else:
        row[[0, 2, 4, 6]] = 1
    i += 1
print(array8)

#Creates a 1D array with 25 elements ranging from 1 to 99 and prints it.
array9 = np.random.randint(1, 100, size=10)
print(array9)
#Sorts that 1D array of 25 elements in ascending order and prints it. 
array9.sort()
print(array9)
