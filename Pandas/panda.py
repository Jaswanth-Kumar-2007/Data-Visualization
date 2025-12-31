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


