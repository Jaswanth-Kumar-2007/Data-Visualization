import matplotlib.pyplot as plt
import pandas as pd # From Example 3 Onwards
import numpy as np # From Example 8 Onwards

# Example 1
"""
date = ["25/12","26/12","27/12"]
temp = [8.5,10.5,6.8]

plt.plot(date,temp) #date --> X-axis , #temp --> Y-axis

plt.show()
"""

# Example 2
"""
date = ["25/12","26/12","27/12"]
temp = [8.5,10.5,6.8]

plt.plot(date,temp)

plt.xlabel("Date")
plt.ylabel("Temperature")

plt.title("Date wise Temperature")

plt.grid(True)
plt.yticks(temp)

plt.show()
"""

# Example 3
"""
height = [121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight = [19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]

df = pd.DataFrame({"height":height,"weight":weight})

plt.xlabel("Weight in Kg")
plt.ylabel("Height in cm")
plt.title("Average weight with respect to average height")

plt.plot(df.weight,df.height,marker="*",markersize=10,color="green",linewidth=2,linestyle="dashdot")

plt.show()
"""

# Example 4
"""
df = pd.read_csv("C:\Projects\JK Projects\Data-Visualization\Data-Visualize\MatPlotLib\MelaSales.csv",sep="\t") #default = sep=","
df.plot(kind="line",color=['red','blue','brown'])
plt.title('Mela Sales Report')
plt.xlabel('Days')
plt.ylabel('Sales in Rs')
plt.show()
"""

# Example 5
"""
df = pd.read_csv("C:\Projects\JK Projects\Data-Visualization\Data-Visualize\MatPlotLib\MelaSales.csv",sep="\t") #default = sep=","
df.plot(kind="line",color=['red','blue','brown'],marker="*",markersize=10,linewidth=3,linestyle="--")
plt.title('Mela Sales Report')
plt.xlabel('Days')
plt.ylabel('Sales in Rs')

ticks = df.index.tolist()
plt.xticks(ticks)

plt.show()
"""

# Example 6
"""
df = pd.read_csv("C:\Projects\JK Projects\Data-Visualization\Data-Visualize\MatPlotLib\MelaSales.csv",sep="\t") #default = sep=","
df.plot(kind="bar",color=['red','blue','yellow'],edgecolor="green",linewidth=3,linestyle="--")
plt.title('Mela Sales Report')
plt.xlabel('Days')
plt.ylabel('Sales in Rs')
plt.show()
"""

# Example 7
"""
data = {'Name':['Arnav', 'Sheela', 'Azhar','Bincy','Yash',
'Nazar'],
'Height' : [60,61,63,65,61,60],
'Weight' : [47,89,52,58,50,47]}
df=pd.DataFrame(data)

df.plot(kind='hist',edgecolor='Green',linewidth=2,linestyle=':',fill=False,hatch='o')

plt.show()
"""

# Example 8
"""
discount= np.array([10,20,30,40,50])
saleInRs=np.array([40000,45000,48000,50000,100000])
size=discount*10
plt.scatter(x=discount,y=saleInRs,s=size,color='red',linewidth=3,marker='*',edgecolor='blue')
plt.title('Sales Vs Discount')
plt.xlabel('Discount offered')
plt.ylabel('Sales in Rs')
plt.show()
"""

# Example 9
"""
data= pd.read_csv(r'C:\Projects\JK Projects\Data-Visualization\Data-Visualize\MatPlotLib\compareresort.csv')
df= pd.DataFrame(data)
df[['SunnyBunnyResort','HappyLuckyResort','BreezyWindyResort']].plot(kind='box') # Important Without these it wont work
 #vert = False to change Direction

plt.xlabel('Resorts')
plt.ylabel('Rating (5 years)')

plt.show()
"""

# Example 10
"""
df=pd.DataFrame({'GeoArea':[83743,78438,22327,22429,21081,16579,10486],'ForestCover':[67353,27692,17280,17321,19240,13464,8073]},index=['Arunachal Pradesh','Assam','Manipur','Meghalaya', 'Mizoram','Nagaland','Tripura'])
exp=[0.1,0,0,0,0.2,0,0] #explode the first wedge to .1 level and fifth to level 2

c=['r','g','m','c','brown','pink','purple']

df.plot(kind='pie',y='ForestCover',title='Forest cover of NorthEastern states', legend=False, explode=exp, autopct="%.2f",colors=c)
plt.show()
"""