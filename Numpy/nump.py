import numpy as np 

# Creation of Numpy Array from List

array1 = np.array([10,20,30])

print(array1)

array2 = np.array([5,-7.4,'a',7.2])

print(array2)

array3 = np.array([[2.4,3],[4.91,7],[0,-1]])

print(array3)

# Attributes of NumPy Array

# ndarray.ndim

print(array1.ndim) #1

# ndarray.shape

print(array3.shape) #(3,2)

# ndarray.size

print(array3.size) # 6

# ndarray.dtype

print(array1.dtype) #int64

# ndarray.itemsize

print(array2.itemsize) #128 memory allocated to string

# np.Zeros

array5 = np.zeros((3,4))

print(array5)

"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
 """

 # np.arange

array6 = np.arange(6)

array7 = np.arange(-2,24,4)

print(array6)

#[0 1 2 3 4 5]

print(array7)

#[-2  2  6 10 14 18 22]

# Indexing and Slicing Same as Python Normal

# Operation on Arrays

"""
Arithmetic Operations
Addition - '+'
Subtraction - '-'
Multiplication - '*'
Matrix Multiplication - '@'
Exponentiation - '**'
Division - '/'
"""

# Transpose

array8 = np.array([[10,-7,0,20],[-5,1,200,40],[30,1,-1,4]])

print(array8.transpose())

"""
[[ 10  -5  30]
 [ -7   1   1]
 [  0 200  -1]
 [ 20  40   4]]
"""

# Sorting 

array9 = np.array([1,0,2,-3,6,8,4,7])

array9.sort()

print(array9)

#[-3  0  1  2  4  6  7  8]

# Concatenating 

array10 = np.array([[10,20],[-30,40]])
array11 = np.zeros((2,3),dtype=array1.dtype)

print(array11)

"""
[[0 0 0]
 [0 0 0]]
"""

print(np.concatenate((array10,array11),axis=1))

"""
[[ 10  20   0   0   0]
 [-30  40   0   0   0]]
"""

# Reshaping Arrays

array12 = np.arange(10,22)

print(array12.reshape(3,4))

"""
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
"""

# Splitting Arrays

array13 = np.array([[10,-7,0,20],[-5,1,200,40],[30,1,-1,4],[1,2,0,4],[0,1,0,2]])

first,second,third = np.split(array13,[1,3])

print(first)

# Statistical Opertion on Arrays

# max()

arrayA = np.array([1,0,2,-3,6,8,4,7])

print(arrayA.max())
print(arrayA.min())
print(arrayA.sum())
print(arrayA.mean())
print(arrayA.std())
print(arrayA.std(axis=0))

"""
8
-3
25
3.125
3.550968177835448  
3.550968177835448
"""

# Loading Array from Files

# NumPy.loadtxt()

studentdata = np.loadtxt('C:/NCERT/data.txt',skiprows=1,delimiter=',',dtype=int)

print(studentdata)

"""
[[ 1, 36, 18, 57],
[ 2, 22, 23, 45],
[ 3, 43, 51, 37],
[ 4, 41, 40, 60],
[ 5, 13, 18, 27]]
"""

rollno,mks1,mks2,mks3 = np.loadtxt('C:/NCERT/data.txt',skiprows=1,delimiter=',',unpack=True,dtype=int)

# NumPy.genfromtxt()

dataarray = np.genfromtxt('C:/NCERT/dataMissing.txt',skip_header=1,delimiter = ',')

"""
([[ 1., 36., 18., 57.],
[ 2., nan, 23., 45.],
[ 3., 43., 51., nan],
[ 4., 41., 40., 60.],
[ 5., 13., 18., 27.]]
"""

# Saving Numpy Arrays in Files on Disk

np.savetxt('C:/NCERT/testout.txt',studentdata,delimeter=',',fmt='%i')