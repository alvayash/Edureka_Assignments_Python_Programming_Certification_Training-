'''
Module 4 : Introduction to NumPy & Pandas Case Study

Case Study I

1. Extract data from the given CSV file and store the data from each column in a separate NumPy array

'''

print('Answer for Question 1 Begins ')

import numpy as np
import pandas as pd

df_csv = pd.read_csv('SalaryGender.csv')

arr_salary=(df_csv['Salary'].to_numpy())
arr_gender=(df_csv['Gender'].to_numpy())
arr_age=(df_csv['Age'].to_numpy())
arr_phd=(df_csv['PhD'].to_numpy())

print('Data of each column have been separated as NumPy array')

print('\n')

'''
2.
Find:
1. The number of men with a PhD
2. The number of women with a PhD
'''
print('Answer for Question 2 Begins ')

v_no_of_men=df_csv['Gender']==1
v_no_of_women=df_csv['Gender']==0
v_no_of_PhD=df_csv['PhD']==1
df_men_with_PhD=df_csv[v_no_of_men & v_no_of_PhD]
df_women_with_PhD=df_csv[v_no_of_women & v_no_of_PhD]

print('The Total men with PhD are :',len(df_men_with_PhD.index))
print('The Total women with PhD are :',len(df_women_with_PhD.index))

print('\n')

'''
3.
Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD
'''
print('Answer for Question 3 Begins ')

df_Age_PhD=df_csv[['Age','PhD']]

df_Age_PhD=df_Age_PhD.drop(df_Age_PhD[df_Age_PhD['PhD']==0].index)

print('Data of Age & PhD columns have been stored & people who don''t have PhD have been deleted')

print('\n')

'''
4.
Calculate the total number of people who have a PhD degree.
'''
print('Answer for Question 4 Begins ')

df_no_of_PhD=df_csv[v_no_of_PhD]

print('The Total number of people with PhD are :',len(df_no_of_PhD.index))

print('\n')

'''
5.
How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) 
which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.
'''
print('Answer for Question 5 Begins ')

list_of_int=[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]

numpy_list=[]

for i in list_of_int:
    numpy_list.append(list_of_int.count(i))

print('Output is :',np.array(numpy_list))

print('\n')

'''
6.
Create a numpy array [[0, 1, 2],
                     [ 3, 4, 5],
                     [ 6, 7, 8],
                     [ 9,10, 11]]) 
and filter the elements greater than 5.
'''

print('Answer for Question 6 Begins ')

numpy_array=np.array([[0, 1, 2],
                     [ 3, 4, 5],
                     [ 6, 7, 8],
                     [ 9,10, 11]])

numpy_array_gt_5_filter=[]

for element in numpy_array:
    for inner_element in element:
        if inner_element<=5:
            numpy_array_gt_5_filter.append(inner_element)
        else:
            pass

print('Filtered array is :',np.array(numpy_array_gt_5_filter))

print('\n')

'''
7.
Create a numpy array having NaN (Not a Number) and print it.
array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
Print the same array omitting all elements which are nan
'''

print('Answer for Question 7 Begins ')

nan_array=np.array([np.NaN,1,2,np.NaN,3,4,5])

without_nan_array=[]

for element in nan_array:
    if np.isnan(element)==True:
        pass
    else:
        without_nan_array.append(element)

print('Array with NaN is    :',nan_array)
print('Array without NaN is :',np.array(without_nan_array))

print('\n')

'''
8.
Create a 10x10 array with random values and find the minimum and maximum values.
'''
print('Answer for Question 8 Begins ')

rand_array = np.random.randint(1000,size=(10,10))

v_1d_rand_array=rand_array.ravel()

rand_array_list=v_1d_rand_array.tolist()

v_min_array_value=np.random.choice(rand_array_list)
v_max_array_value=np.random.choice(rand_array_list)

for element in rand_array:
    for inner_element in element:
        if inner_element<=v_min_array_value:
            v_min_array_value=inner_element
        elif inner_element>=v_max_array_value:
            v_max_array_value=inner_element
        else:
            pass

print('Randomly generated array of 10 x 10 is : ')
print(rand_array)
print('\n')
print('Minimum Value in the randomly generated array is :',v_min_array_value)
print('Maximum value in the randomly generated array is :',v_max_array_value)
print('\n')

'''
9.
Create a random vector of size 30 and find the mean value
'''

print('Answer for Question 9 Begins ')

rand_array_30 = np.random.randint(1000,size=(6,5))

print('Random vector of size 30 is :')
print(rand_array_30)
print('Mean of the above vector is :',np.mean(rand_array_30))

print('\n')

'''
10.
Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
'''

print('Answer for Question 10 Begins ')
np_array_0_10=np.arange(11)
np_array_0_10_output=[]

for element in np_array_0_10:
    if element>=3 and element<=9:
        np_array_0_10_output.append(element*-1)
    else:
        np_array_0_10_output.append(element)

print('Original Array is :',np_array_0_10)
print('Array output after negating numbers between 3 & 9 are :',np.array(np_array_0_10_output))
print('\n')

'''
11.
Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column
'''
print('Answer for Question 11 Begins ')

rand_array_3_x_3 = np.random.randint(1000,size=(3,3))

print('Original array is :')
print(rand_array_3_x_3)
print('Sorted array along column is :')
print(np.sort(a=rand_array_3_x_3,axis=0))
print('\n')

'''
12.
Create a four dimensions array get sum over the last two axis at once.
'''

print('Answer for Question 12 Begins ')

np_records = np.arange(72)

np_4d_array = np.reshape(np_records, (4,3,2,3))

print('The 4D array is :')
print(np_4d_array)
print('Array Dimension is',np_4d_array.ndim)
print("Sum of last two axis :")
print(np.sum(np_4d_array, axis=(2, 3)))
print('\n')

'''
13.
Create a random array and swap two rows of an array.
'''
print('Answer for Question 13 Begins ')

rand_array_2_x_2 = np.random.randint(100,size=(2,2))
print('Random array is :')
print(rand_array_2_x_2)

rand_array_2_x_2[[0, 1]] = rand_array_2_x_2[[1, 0]]

print('Random array after swapping is :')
print(rand_array_2_x_2)
print('\n')

'''
14.
Create a random matrix and Compute a matrix rank.
'''

print('Answer for Question 14 Begins ')

x_rand_matrix = np.random.randint(100,size=(3,3))

print('Random Matrix is :')
print(x_rand_matrix)
print('Rank of the matrix is :',np.linalg.matrix_rank(x_rand_matrix))
print('\n')

'''

15.

Analyse various school outcomes in Tennessee using pandas. Suppose you are a public school administrator.Some schools
in your state of Tennessee are performing below average academically. Your superintendent, under pressure from
frustrated parents and voters, approached you with the task of understanding why these schools are under-performing.
To improve school performance, you need to learn more about these schools and their students, just as a business needs
to understand its own strengths and weaknesses and its customers. Though you are eager to build an impressive
explanatory model, you know the importance of conducting preliminary research to prevent possible pitfalls or
blind spots. Thus, you engages in a thorough exploratory analysis, which includes: a lit review, data collection,
descriptive and inferential statistics, and data visualization.

Phase 1 - Data Collection

Here is a data of every public school in middle Tennessee. The data also includes various demographic,school faculty,
and income variables. You need to convert the data into useful information.

• Read the data in pandas data frame
• Describe the data to find more details

Phase 2 -Group data by school ratings

Chooses indicators that describe the student body (for example,reduced_lunch) or school administration (stu_teach_ratio)
hoping they will explain school_rating. reduced_lunch is a variable measuring the average percentage of students per
school enrolled in a federal program that provides lunches for students from lower-income households.
In short, reduced_lunch is a good proxy for household income.Isolates ‘reduced_lunch’ and groups the data
by ‘school_rating’ using pandas groupby method and then uses describe on the re-shaped data

Phase 3 – Correlation analysis

Find the correlation between ‘reduced_lunch’
and ‘school_rating’. The values in the correlation matrix table will be between -1 and 1.
A value of -1 indicates the strongest possible negative correlation, meaning as one variable decreases the other
increases. And a value of 1 indicates the opposite

Phase 4 –Scatter Plot

Find the relationship between school_rating and reduced_lunch, Plot a graph with the two variables on a scatter plot.
Each dot represents a school. The placement of the dot represents that school's rating (Y-axis) and the percentage of
its students on reduced lunch (x-axis). The downward trend line shows the negative correlation between school_rating
and reduced_lunch (as one increases, the other decreases). The slope of the trend line indicates how much school_rating
decreases as reduced_lunch increases. A steeper slope would indicate that a small change in reduced_lunch has a big
impact on school_rating while a more horizontal slope would indicate that the same small change in reduced_lunch has a
smaller impact on school_rating.

Phase 5 –Correlation Matrix

An efficient graph for assessing relationships is the correlation matrix, as seen below;
its color- coded cells make it easier to interpret than the tabular correlation matrix above.
Red cells indicate positive correlation; blue cells indicate negative correlation; white cells indicate no correlation.
The darker the colors, the stronger the correlation (positive or negative) between those two variables.
Draw a graph of correlation matrix having all important fields of data frame.

'''
import seaborn as sn
import matplotlib.pyplot as plt

print('Output of phase 1 :')
tn_school_complete_data=pd.read_csv('middle_tn_schools.csv')
print('Data after reading file into dataframe is ;')
print(tn_school_complete_data)

print('Output after describing the file is :')
print(tn_school_complete_data.describe())

print('Output of phase 2 :')

reduced_lunch_gb=tn_school_complete_data.groupby(['reduced_lunch', 'school_rating']).size().reset_index(name='counts')
reduced_lunch_gb.drop(['counts'], axis=1,inplace=True)
print('Output of file with reduced lunch & school rating is :')
print(reduced_lunch_gb)

print('Output after describing the file with reduced lunch & school rating is :')
print(reduced_lunch_gb.describe())
print('\n')

print('Output of phase 3 :')
reduced_lunch_gb_corr_matrix=reduced_lunch_gb.corr()
print('Correlation Analysis :')
print(reduced_lunch_gb_corr_matrix)
print('\n')

print('Output of phase 4 :')

reduced_lunch_gb.plot(x ='reduced_lunch', y='school_rating', kind = 'scatter')
print('Scatterplot is complete')
plt.show()

print('\n')

print('Output of phase 5 :')
sn.heatmap(reduced_lunch_gb_corr_matrix,annot=True)
plt.show()
print('Correlation Matrix is complete')
print('\n')