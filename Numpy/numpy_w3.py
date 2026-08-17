import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr1 = np.array([[1,2,3,4],[5,6,7,8]])

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2]) 

newarr1 = arr.reshape(3, 4)

print("Print Array",newarr1) 

newarr2 = arr2.reshape(-1)

print("Print Flatten",newarr2)

print(arr)
print(arr.ndim)
print(type(arr))
print("Shape of arr",arr.shape)

print(arr1)
print(arr1.ndim)
print("Shape of arr1",arr1.shape)

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[0:2, 2]) 

# Data Types in Numpy

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

print(arr3.dtype)

arr4 = np.array([1.1, 2.1, 3.1])

newarr = arr4.astype('i')

print(newarr)
print(newarr.dtype) 

arr5 = np.array([1, 2, 3, 4, 5])
x = arr5.copy()
arr5[0] = 42

# The copy SHOULD NOT be affected by the changes made to the original array.
print(arr5)
print(x) 


arr6 = np.array([1, 2, 3, 4, 5])
x = arr6.view()
arr6[0] = 42

# The view SHOULD be affected by the changes made to the original array.
# The original array SHOULD be affected by the changes made to the view.
print(arr6)
print(x) 