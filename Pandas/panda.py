import pandas as pd 
import numpy as np

# Creation of Series from Scalar Values

series1 = pd.Series([10,20,30])

print(series1)

"""
0    10
1    20
2    30
dtype: int64
"""

# Creation of Series from NumPy Arrays

array1 = np.array([1,2,3,4])
series2 = pd.Series(array1)

print(series2)

"""
0    1
1    2
2    3
3    4
dtype: int64
"""

# Creation of Series from Dictionary

dict1 = {'India':'NewDelhi','UK':'London','Japan':'Tokyo'}

series3 = pd.Series(dict1)

print(series3)

"""
India    NewDelhi
UK         London
Japan       Tokyo
dtype: object
"""

# Accessing Elements of a Series

seriesMnths = pd.Series([2,3,4],index=["Feb","Mar","Apr"])

print(seriesMnths["Mar"]) # 3

print(seriesMnths[[2,1]])

"""
Apr    4
Mar    3
dtype: int64
"""

# Slicing

seriesCapCntry = pd.Series(['NewDelhi', 'WashingtonDC', 'London','Paris'], index=['India', 'USA', 'UK', 'France'])

print(seriesCapCntry[1:3])

"""
USA    WashingtonDC
UK           London
dtype: object
"""

# We can Modify the Value of Series using Slicing

# Attributes of Pandas Series

seriesCapCnt = pd.Series({'India':'NewDelhi','UK':'London','Japan':'Tokyo'})

"""
seriesCapCnt.name = 'Capitals'

seriesCapCnt.index.name = 'Countries'

seriesCapCnt.values #-> print

seriesCapCnt.size # -> print

seriesCapCnt.empty # -> print False
"""

seriesTenTwenty=pd.Series(np.arange( 10,20, 1 ))

print(seriesTenTwenty.head(2)) # default head() takes first 5 values

"""
0    10
1    11
dtype: int64
"""

print(seriesTenTwenty.count()) # 20

print(seriesTenTwenty.tail(2))

"""
8    18
9    19
dtype: int64
"""

# Mathematical Operation on Series

"""
Addition of two Series
-> seriesA + seriesB
-> seriesA.add(seriesB,fill_value=0)

Subtraction of two Series
-> seriesA - seriesB
-> seriesA.sub(seriesB,fill_value=1000)

Multiplication of two Series
-> seriesA * seriesB
-> seriesA.mul(seriesB,fill_value=0)

Divison of two Series
-> seriesA/seriesB
"""

"""
DataFrames
"""

# Creation of an empty DataFrame

dFrameEmt = pd.DataFrame()

print(dFrameEmt)

"""
Empty DataFrame
Columns: []
Index: []
"""

# Creation of DataFrame from Numpy ndarrays

array1 = np.array([10,20,30])
array2 = np.array([100,200,300])
array3 = np.array([-10,-20,-30,-40])

dFrame4 = pd.DataFrame(array1)

print(dFrame4)

"""
    0
0  10
1  20
2  30
"""

dFrame5 = pd.DataFrame([array1, array3,array2], columns=[ 'A', 'B', 'C', 'D'])

print(dFrame5)

"""
     A    B    C     D
0   10   20   30   NaN
1  -10  -20  -30 -40.0
2  100  200  300   NaN
"""

# Creation of Dataframe from List of Dictionaries

listDict = [{'a':10, 'b':20}, {'a':5,'b':10, 'c':20}]

dFrameListDict = pd.DataFrame(listDict)

print(dFrameListDict)

"""
    a   b     c
0  10  20   NaN
1   5  10  20.0
"""

# Creating of DataFrame from Dictionary of Lists

dictForest = {'State': ['Assam', 'Delhi','Kerala'],'GArea': [78438, 1483, 38852] ,'VDF' : [2797, 6.72,1663]}

dFrameForest = pd.DataFrame(dictForest)

print(dFrameForest)

"""
    State  GArea      VDF
0   Assam  78438  2797.00
1   Delhi   1483     6.72
2  Kerala  38852  1663.00
"""

# Creation of DataFrame from Series

seriesA = pd.Series([1,2,3,4,5],index = ['a', 'b', 'c', 'd', 'e'])

dFrame6 = pd.DataFrame(seriesA)

print(dFrame6)

"""
   0
a  1
b  2
c  3
d  4
e  5
"""

# Creation of DatFrame from Dictionary of Series

ResultSheet={
'Arnab': pd.Series([90, 91, 97],index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']),
'Samridhi': pd.Series([89, 91, 88],index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']),
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}

ResultDF = pd.DataFrame(ResultSheet)

print(ResultDF)

"""
         Arnab  Ramit  Samridhi  Riya  Mallika
Maths       90     92        89    81       94
Science     91     81        91    71       95
Hindi       97     96        88    67       99
"""

# Operations on Rows and Columns in DataFrames

# Adding a new Column to a DataFrame

ResultDF['Preeti']=[89,78,76]

print(ResultDF)

"""
         Arnab  Ramit  Samridhi  Riya  Mallika  Preeti
Maths       90     92        89    81       94      89
Science     91     81        91    71       95      78
Hindi       97     96        88    67       99      76
"""

# Adding New Row to a DataFrame

ResultDF.loc['English'] = [85, 86, 83, 80, 90, 89]

print(ResultDF)

"""
         Arnab  Ramit  Samridhi  Riya  Mallika  Preeti
Maths       90     92        89    81       94      89
Science     91     81        91    71       95      78
Hindi       97     96        88    67       99      76
English     85     86        83    80       90      89
"""

"""
DataFrame.loc[] method can also be used to change data values of a row

ResultDF[: ] = 0

# Set all Values in ResultDF to 0
"""

# Deleting Rows or Columns from a DataFrame

# Deleting Row

ResultDF = ResultDF.drop('Science',axis=0)

# Deleting Column

ResultDF = ResultDF.drop(['Samridhi','Ramit','Riya'], axis=1)

# Renaming Row labels of a DataFrame

ResultDF=ResultDF.rename({'Maths':'Sub1','Science':'Sub2','English':'Sub3','Hindi':'Sub4'}, axis='index')

# Renaming Columns of a DataFrame

ResultDF=ResultDF.rename({'Arnab':'Student1','Ramit':'Student2','Samridhi':'Student3','Mallika':'Student4'},axis='columns')

# Accessing DataFrames Element through Indexing

# Label Based Indexing

ResultDF.loc['Science']

"""
Arnab 91
Ramit 81
Samridhi 91
Riya 71
Mallika 95
Name: Science, dtype: int64
"""

# Boolean Indexing

ResultDF.loc['Maths'] > 90

"""
Arnab False
Ramit True
Samridhi False
Riya False
Mallika True
Name: Maths, dtype: bool
"""

# Accessing DataFrames Element through Slicing

ResultDF.loc['Maths': 'Science', 'Arnab']

"""
Maths 90
Science 91
Name: Arnab, dtype: int64
"""

ResultDF.loc[[True, False, True]]

"""
Arnab Ramit Samridhi Riya Mallika
Maths 90 92 89 81 94
Hindi 97 96 88 67 99
"""

# Joining , Merging and Concatenation of DataFrames

# Joining

dFrame1=pd.DataFrame([[1, 2, 3], [4, 5],[6]], columns=['C1', 'C2', 'C3'], index=['R1','R2', 'R3'])

"""
C1 C2 C3
R1 1 2.0 3.0
R2 4 5.0 NaN
R3 6 NaN NaN
"""

dFrame2=pd.DataFrame([[10, 20], [30], [40,50]], columns=['C2', 'C5'], index=['R4', 'R2','R5'])

"""
C2 C5
R4 10 20.0
R2 30 NaN
R5 40 50.0
"""

dFrame1 = dFrame1.append(dFrame2)

"""
C1 C2 C3 C5
R1 1.0 2.0 3.0 NaN
R2 4.0 5.0 NaN NaN
R3 6.0 NaN NaN NaN
R4 NaN 10.0 NaN 20.0
R2 NaN 30.0 NaN NaN
R5 NaN 40.0 NaN 50.0
"""

# Attributes of DataFrames

"""
DataFrame.index
DataFrame.columns
DataFrame.dtypes
DataFrame.values
DataFrame.shape
DataFrame.size
DataFrame.T #Transpose
DataFrame.head(n)
DataFrame.tail(n)
"""

# Importing a CSV file to a DataFrame

marks = pd.read_csv("C:/NCERT/ResultData.csv",sep =",", header=0)

"""
RollNo Name Eco Maths
0 1 Arnab 18 57
1 2 Kritika 23 45
2 3 Divyam 51 37
3 4 Vivaan 40 60
4 5 Aaroosh 18 27
"""

# Exporting a DataFrame to a CSV File

ResultDF.to_csv( 'C:/NCERT/resultonly.txt',sep = '@', header = False, index= False)

"""
Remaining Extra Pandas Functions can Be Get from Informatics Practices Chapter-3 Data Handling using Pandas-II
"""



