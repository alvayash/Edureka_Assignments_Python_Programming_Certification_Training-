'''
Module 5 – Data Visualisation

Case Study

1. You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring in the United States
   along the coast of the Atlantic

   Load the data from the dataset into your program and plot a Bar Graph of the data, taking the Year as the
   x-axis and the number of hurricanes occurring as the Y-axis.
'''

print('Answer for Question 1 Begins ')

import pandas as pd
import matplotlib.pyplot as plt

df_Hurricane=pd.read_csv("Hurricanes.csv")

df_Hurricane.plot(kind='bar',x='Year',y='Hurricanes',color='k')
plt.ylabel('No. of Hurricanes')
plt.xlabel('Year')

plt.show()
print('\n')

'''
2. The dataset given, records data of city temperatures over the years 2014 and 2015. 
   Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
'''

'''
2. The dataset given, records data of city temperatures over the years 2014 and 2015.
   Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
'''

print('Answer for Question 2 Begins ')

import pandas as pd
import matplotlib.pyplot as plt

df_CityTemps=pd.read_csv("CityTemps.csv")
df_CityTemps["Period"] = df_CityTemps["Year"].astype(str) + '-' + df_CityTemps["Month"].astype(str)
df_CityTemps.drop(['Year', 'Month'], axis = 1 ,inplace = True)

df_Moscow=df_CityTemps[['Period','Moscow']]
df_Melbourne=df_CityTemps[['Period','Melbourne']]
df_San_Francisco=df_CityTemps[['Period','San Francisco']]

df_Moscow.plot.hist(grid=True, bins=30, rwidth=0.9, color='r')
df_Melbourne.plot.hist(grid=True, bins=30, rwidth=0.9, color='b')
df_San_Francisco.plot.hist(grid=True, bins=30, rwidth=0.9, color='y')

plt.title('City Temperature')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.show()

print('\n')

'''
3. Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide.
   Also mention the name of the manufacture with the largest releases.
'''

print('Answer for Question 3 Begins ')

import pandas as pd
import matplotlib.pyplot as plt

df_cars= pd.read_csv("Cars2015.csv")

##Removing spaces from rows

df_cars['Make']=df_cars['Make'].str.strip()

series_model_count=df_cars['Make'].value_counts()

total_sold=[]

series_model_count.plot.pie(label="", title="Total Model sold by Manufacturers")

plt.show(block=True)

print('\n')

'''
4. Create csv file from the data below and read in pandas data frame
   Phase 1 - Reading Data
   Phase 2 – Describe the data. Describe the data on the unit price
   Phase 3 – Filter the data. Create new dataframe having columns 'name','net_price','date'
             and group all the records according to name
   Phase 4 – Plotting graph. Plot the graph after calculating total sales by each customer.
             Customer name should be on x axis and total sales in y axis.
'''

print('Answer for Question 4 Begins ')

import pandas as pd
import matplotlib.pyplot as plt

##Phase 1

df_sales=pd.read_csv('sample-salesv2.csv')

##Phase_2
print(df_sales['unit price'].describe())

##Phase_3

df_sales['date'] = pd.to_datetime(df_sales['date']).dt.date
df_sales.drop(['account_number','item_code','category','quantity','unit price'], axis = 1 , inplace=True)
df_name_price=df_sales.groupby(['name'])['net_price'].sum()

##Phase_4

df_name_price.plot.bar(rot=15, title="Total Sales by Customer",edgecolor='blue',color='r')
plt.ylabel('Sales')
plt.xlabel('Customer_Name')
plt.show(block=True)

print('\n')

'''

5. Let the x axis data points and y axis data points are
	X = [1,2,3,4]
	y = [20, 21, 20.5, 20.8]

5.1: Draw a Simple plot

5.2: Configure the line and markers in simple plot

5.3: configure the axes

5.4: Give title of Graph & labels of x axis and y axis

5.5: Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1]

5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100

5.7: Give a font size of 14

5.8: Draw a scatter graph of any 50 random values of x and y axis

5.9: Create a dataframe from following data
	'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
	'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
	'female': [0, 1, 1, 0, 1],
	'age': [42, 52, 36, 24, 73], 
	'preTestScore': [4, 24, 31, 2, 3],
	'postTestScore': [25,94, 57, 62, 70]
	
	Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age

5.10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore
    with the size = 300 and the color determined by sex
'''

print('Answer for Question 5 Begins ')

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Answers to 5.1 # 5.2 # 5.3 # 5.4 # 5.6 # 5.7
x = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]

# plot the data
fig = plt.figure(figsize=(4,5), dpi=100, facecolor='y', edgecolor='k')
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, color ='tab:red')

ax.set_xlim([1, 5])
ax.set_ylim([20, 21])
plt.rcParams.update({'font.size': 14})

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Distribution X vs Y ')

plt.show()

# Answer to 5.8
import random

x_axis = [random.randint(0,51) for i in range(50)]
y_axis = [random.randint(0,51) for j in range(50)]
plt.title('Scatter Graph for Question 5.8 ')
plt.scatter(x_axis,y_axis)
plt.show()

# Answer to 5.9

first_name = ['Jason', 'Molly', 'Tina', 'Jake', 'Amy']
last_name = ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze']
female = [0, 1, 1, 0, 1]
age = [42, 52, 36, 24, 73]
preTestScore = [4, 24, 31, 2, 3]
postTestScore = [25, 94, 57, 62, 70]

final_df = pd.DataFrame(list(zip(first_name,last_name,female,age,preTestScore,postTestScore)),
                        columns =['first_name','last_name','female','age','preTestScore','postTestScore'])

plt.scatter(preTestScore,postTestScore,s=age)
plt.title('Scatter Graph for Question 5.9 ')
plt.xlabel('Pre Test Score')
plt.ylabel('Post Test Score')
plt.show()

# Answer to 5.10
import numpy as np

my_color=[]

for i in range(len(female)):
    if female[i]==0:
        my_color.append('Blue')
    else:
        my_color.append('Red')

final_colour = np.asarray(my_color)

plt.scatter(preTestScore,postTestScore,s=300,color=final_colour )

plt.title('Scatter Graph for Question 5.10 ')
plt.xlabel('Pre Test Score')
plt.ylabel('Post Test Score')
plt.show()

print('\n')