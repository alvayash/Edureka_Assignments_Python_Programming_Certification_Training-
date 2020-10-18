'''
Module 6–Data Manipulation

From the data provided on Hollywood movies:

1. Find the highest rated movie in the “Quest” story type.
'''

import pandas as pd
import matplotlib.pyplot as plt

df_movies=pd.read_csv('HollywoodMovies.csv')
pd.set_option('display.max_columns', None)

df_quest=df_movies.loc[:,['AudienceScore','Movie']][df_movies.Story.str.upper() == "QUEST"]

df_quest_sorting=df_quest.sort_values(by='AudienceScore',ascending=False,inplace=True)

df_quest_sorting_movie=df_quest['Movie'].iloc[:1]
print('The highest rated movie in the “Quest” story type is : \n',df_quest_sorting_movie)

'''
2. Find the genre in which there has been the greatest number of movie releases
'''
df_movies['Genre'] = df_movies['Genre'].str.upper()
df_genre=df_movies[['Genre','TheatersOpenWeek']].groupby('Genre').count().sort_values(by='TheatersOpenWeek',ascending=False)
df_genre=df_genre.reset_index()

print('Genre with greatest number of movie releases is :\n ',df_genre['Genre'].iloc[:1])

'''
3. Print the names of the top five movies with the costliest budgets.
'''

df_movie_budget=df_movies[['Movie','Budget']].sort_values(by='Budget',ascending=False).iloc[:5]
print('Top 5 movies with the costliest budget \n',df_movie_budget)

'''
4. Is there any correspondence between the critics’ evaluation of a movie and its acceptance 
   by the public? Find out, by plotting the net profitability of a movie against the ratings it
   receives on Rotten Tomatoes
'''

df_movies_RT_Profit=df_movies[['RottenTomatoes','Profitability']].dropna()

x_RottenTomatoes=df_movies_RT_Profit['RottenTomatoes'].to_list()
y_Profitability=df_movies_RT_Profit['Profitability'].to_list()

plt.plot(x_RottenTomatoes,y_Profitability, 'o', color='black')
plt.title('Correspondence between the critics’ evaluation of a movie and its acceptance by the public')
plt.ylabel('Profitability')
plt.xlabel('RottenTomatoes')
plt.show()
print('\n')

'''
5. Perform Operations on Files

5.1: From the raw data below create a data frame
	'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
	'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
	'age': [42, 52, 36, 24, 73], 
	'preTestScore': [4, 24, 31, ".", "."],
	'postTestScore': ["25,000", "94,000", 57, 62, 70]
'''
import pandas as pd

df_create_df_dict={
'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df_create_df=pd.DataFrame.from_dict(df_create_df_dict)
print('Dataframe from Dictionary is :')
print(df_create_df)
print('\n')

'''
5.2: Save the dataframe into a csv file as example.csv
'''
df_create_df.to_csv('example.csv', index=False)
print('\n')

'''
5.3: Read the example.csv and print the data frame
'''
df_example=pd.read_csv('example.csv')
print('Data after loading into Dataframe is : \n')
print(df_example)
print('\n')

'''
5.4: Read the example.csv without column heading
'''
df_example_wo_header=pd.read_csv('example.csv',header=None,skiprows=1)
print(df_example_wo_header)
print('\n')

'''
5.5: Read the example.csv an make the index columns as 'First Name’ and 'Last Name'
'''
df_example_index_change=pd.read_csv('example.csv')
df_example_index_change.set_index(['first_name','last_name'], inplace=True)
print('Dataframe after changing index to first_name & last_name :\n')
print(df_example_index_change)
print('\n')

'''
5.6: Print the data frame in a Boolean form as True or False.  
     True for Null/NaN values and false for non - null values
'''

df_example_bool=pd.read_csv('example.csv')
print('Dataframe output in Boolean form is :\n')
print(df_example_bool.notnull())
print('\n')

'''
5.7: Read the dataframe by skipping first 3 rows and print the data frame
'''
df_example_skip=pd.read_csv('example.csv',skiprows=[1,2,3])
print('Dataframe after skipping first 3 rows are :')
print(df_example_skip)
print('\n')

'''
5.8: Load a csv file while interpreting "," in strings around numbers as thousands seperators.
     Check the raw data 'postTestScore' column has, as thousands separator.
     Comma should be ignored while reading the data. It is default behaviour, 
     but you need to give argument to read_csv function which makes sure commas are ignored.
'''
df_data=pd.read_csv('example.csv', index_col=4).filter(regex='\d{4}')
print('Output after ignoring commas are :')
print(df_data)
print('\n')


'''
6. Perform Operations on Files

6.1: From the raw data below create a Pandas Series
	 'Amit','Bob','Kate','A','b',np.nan,'Car','dog','cat'

a) Print all elements in lower case
'''
import numpy as np
import pandas as pd

my_series=pd.Series(['Amit','Bob','Kate','A','b',np.nan,'Car','dog','cat'])
print('Pandas series in lowercase is :\n')
print(my_series.str.lower())
print('\n')
'''
b) Print all the elements in upper case
'''
print('Pandas series in uppercase is :\n')
print(my_series.str.upper())
print('\n')

'''
c) Print the length of all the elements
'''
print('Pandas series lengths are :\n')
print(my_series.str.len())
print('\n')

'''
6.2: From the raw data below create a Pandas Series
     ' Atul','John ',' jack ', 'Sam'

a) Print all elements after stripping spaces from the left and right
b) Print all the elements after removing spaces from the left only
c) Print all the elements after removing spaces from the right only
'''
pd_raw_data_series=pd.Series(['    Atul','John ',' jack ','Sam'])
print('Stripping all spaces from left & right are :\n')
print(pd_raw_data_series.str.strip(' '))
print('\n')
print('Stripping all spaces from left are :\n')
print(pd_raw_data_series.str.lstrip(' '))
print('\n')
print('Stripping all spaces from right are :\n')
print(pd_raw_data_series.str.rstrip(' '))
print('\n')

''''
6.3: Create a series from the raw data below
    'India_is_big','Population_is_huge',np.nan,'Has_diverse_culture'

a) split the individual strings wherever ‘_’ comes and create a list out of it.
b) Access the individual element of a list
c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
'''

from pandas.core.common import flatten
series_split=pd.Series(['India_is_big','Population_is_huge',np.nan,'Has_diverse_culture']).dropna()
new_list=series_split.str.split('_').to_list()
new_list_2=list(flatten((new_list)))
for element in new_list_2:
    print(element)
print('\n')
'''
6.4: Create a series and replace either X or dog with XX-XX
    'A','B','C','AabX','BacX','',np.nan,'CABA','dog','cat'
'''
series_x=pd.Series(['A','B','C','AabX','BacX','',np.nan,'CABA','dog','cat']).dropna()
print(series_x.str.replace('X|dog', 'XX-XX ', case=False))
print('\n')
'''
6.5: Create a series and remove dollar from the numeric values
    '12','-$10','$10,000'
'''
series_dollar=pd.Series(['12','-$10','$10,000'])
print('Output after removing dollare is:\n')
print((series_dollar.str.replace('$','')))
print('\n')
'''
6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
    '1','2','1a','2b','2003c'
'''
series_alnum=pd.Series(['1','2','1a','2b','2003c']).dropna()
print('Output to check if series is alphanumeric or not is:\n')
print(series_alnum.str.isalnum())
print('\n')

'''
6.8: Create pandas series and print true if value is containing ‘A’
	'1','2','1a','2b','America','VietnAm','vietnam','2003c'
'''
series_check_A=pd.Series(['1','2','1a','2b','America','VietnAm','vietnam','2003c'])
print('Output to check if series contains A is :\n')
print(series_check_A.str.contains('A'))
print('\n')
