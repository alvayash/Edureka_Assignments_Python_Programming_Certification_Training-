'''
Case Study I - Operations on Pandas
'''

import pandas as pd
import numpy as np

'''
1.  Create a pandas dataframe having following structure
      float_col int_col str_col
0         0.1      1       a
1         0.2      2       b
2         0.2      6      None
3         10.1     8       c
4         NaN     -1       a
'''

print('Answer for Question 1 Begins ')

test_data=[[0.1,1,'a'],[0.2,2,'b'],[0.2,6,None],[10.1,8,'c'],[np.nan,-1,'a']]
final_dataframe=pd.DataFrame(test_data,columns=['float_col','int_col','str_col'])
print('Output of Dataframe is : ','\n',final_dataframe)
print('\n')

'''
2.  Filter  the  columns  'float_col',  'int_col'  from  the  dataframe  in  one  query.  
    Hint-use  ix method of dataframes. Also print without using ix method
'''

'''Please Note : Since ix method is deprecated, we are going to using iloc method '''

print('Answer for Question 2 Begins ')

ans2_1 =final_dataframe.iloc[:,:2]
print('Output of Dataframe using iloc method is : ','\n',ans2_1)

ans2_2=final_dataframe[['float_col','int_col']]
print('Output of Dataframe without using iloc method is : ','\n',ans2_2)
print('\n')

'''
3.  Filter the records from float_col having value greater than 0.15 and 
    in separate query filter float_col value equal to 0.1
'''

print('Answer for Question 3 Begins ')
print('Records from float_col having value greater than 0.15 : ')
print(final_dataframe.loc[final_dataframe['float_col']>0.15])
print('\n')

print('Records from float_col having value equal to 0.1 : ')
print(final_dataframe.loc[final_dataframe['float_col']==0.1])
print('\n')

'''
4.  Filter the records from DataFrame which satisfies both the conditions float_col 
    greater than 0.1 and int_col greater than 2
'''

print('Answer for Question 4 Begins ')
print('Records from DataFrame which satisfies both the conditions float_col greater than 0.1 and int_col greater than 2 : ')
print(final_dataframe.loc[(final_dataframe['float_col']>0.1) & (final_dataframe['int_col']>2)])
print('\n')

'''
5.  Filter  the  records  from  data  frame  which  satisfies  both  the  conditions  float_col 
    greater than 0.1 or int_col greater than 2
'''

print('Answer for Question 5 Begins ')
print('Records from DataFrame which satisfies both the conditions float_col greater than 0.1 or int_col greater than 2 : ')
print(final_dataframe.loc[(final_dataframe['float_col']>0.1) | (final_dataframe['int_col']>2)])
print('\n')

'''
6.  Filter the records from data frame which satisfies the conditions float_col not 
    greater than 0.1
'''

print('Answer for Question 6 Begins ')
print('Records from DataFrame which satisfies which satisfies the conditions float_col not greater than 0.1 : ')
print(final_dataframe.loc[final_dataframe['float_col']<0.1])
print('\n')

'''
7.  Create a new data frame in which column int_col is renamed to new_name.
'''
print('Answer for Question 7 Begins ')

new_final_dataframe=final_dataframe.copy()
new_final_dataframe.rename(columns={'int_col':'new_name'}, inplace=True)
print('New DataFrame in which column int_col is renamed to new_name :')
print(new_final_dataframe)
print('\n')

'''
8.  Modify the existing data frame and rename the column int_col to new_name.
'''
print('Answer for Question 8 Begins ')

final_dataframe.rename(columns={'int_col':'new_name'}, inplace=True)
print('Old existing DataFrame in which column int_col is renamed to new_name :')
print(final_dataframe)
print('\n')

'''
9.  Drop the rows where any value is missing from the data frame.
'''
print('Answer for Question 9 Begins ')
index_names_to_be_dropped=final_dataframe[(final_dataframe['str_col'].isnull()) | (final_dataframe['float_col'].isnull()) | (final_dataframe['new_name'].isnull()) ].index
final_dataframe.drop(index_names_to_be_dropped,inplace=True)
final_dataframe=final_dataframe.reset_index(drop=True)
print('Old existing DataFrame after dropping rows where any value is missing :')
print(final_dataframe)
print('\n')

'''
10. Change the missing value in column float_col as mean value of the float_col
'''
print('Answer for Question 10 Begins ')
new_final_dataframe['float_col']=new_final_dataframe['float_col'].fillna(new_final_dataframe['float_col'].mean())
print('New DataFrame after changing the missing value in column float_col as mean value of the float_col')
print(new_final_dataframe)
print('\n')

'''
11. Change all the values of str_col with new value and drop the missing values. New 
    value should have prefix map_ and original value. Eg map_a, map_b
'''
print('Answer for Question 11 Begins ')
index_names_to_be_dropped=new_final_dataframe[(new_final_dataframe['str_col'].isnull())].index
new_final_dataframe.drop(index_names_to_be_dropped,inplace=True)
new_final_dataframe=new_final_dataframe.reset_index(drop=True)
for (index_label, row_series) in new_final_dataframe.iterrows():
   new_final_dataframe.at[index_label, 'str_col'] = 'map_'+row_series['str_col']
print('DataFrame after dropping missing values under str_col column and changing all values under it with a prefix map_ and existing value :')
print(new_final_dataframe)
print('\n')

'''
12. Group  all  the  values  of  str_col  and  find  the  mean  of  float_col  in  all  the  groups 
    respectively.
'''
print('Answer for Question 12 Begins ')
print('Output of dataframe after taking mean of float_col for groups under str_col :')
print(new_final_dataframe.groupby(['str_col'])['float_col'].agg('mean'))
print('\n')

'''
13. Find the covariance of float_col and int_col
'''
print('Answer for Question 13 Begins ')
print(new_final_dataframe.cov())
print('\n')

'''
14. Find the correlation of float_col and int_col
'''
print('Answer for Question 14 Begins ')
column_1 = new_final_dataframe["new_name"]
column_2 = new_final_dataframe["float_col"]
correlation = column_1.corr(column_2)
print(correlation)
print('\n')

'''
15. Create a data frame ‘other’ having columns some_val and str_col having values given below :
    some_val str_col
0       1       a
1       2       b 

Perform inner join, outer join, left join and right join with data frame x
'''

print('Answer for Question 15 Begins ')
new_data=[[1,'a'],[2,'b']]
other=pd.DataFrame(new_data,columns=['some_val','str_col'])
print('Output of other Dataframe is : ','\n',other)
print('\n')

print('Inner Join output is :')
print(pd.merge(final_dataframe,other,on='str_col'))
print('\n')

print('Outer Join output is :')
print(pd.merge(final_dataframe,other,on='str_col',how='outer'))
print('\n')

print('Left Join output is :')
print(pd.merge(final_dataframe,other,on='str_col',how='left'))
print('\n')

print('Right Join output is :')
print(pd.merge(final_dataframe,other,on='str_col',how='right'))
print('\n')


'''
16. When we want to send the same invitations to many people, the body of the mail 
    does not change. Only the name (and maybe address) needs to be changed.
    Mail merge is a process of doing this. Instead of writing each mail separately, 
    we have a template for body of the mail and a list of names that we merge together to form all the mails.

    Create a text file “names.txt” having the names.
    Anil
    sunita
    suman
    lokesh
    Sumita
    John
    Johny

    Create a text file “body.txt” having the body of email.

    I am going to Delhi. Lets meet on 7th Jan 2018.
    Have a great day
    Regards
    Team Victory

    Write  a  program  which  should  create  separate  files  Anil.txt,  sunita.txt,  suman.txt etc 
    after picking names from names.txt. Content of these files looks like –

    Anil.txt
    -----------------------
    Hello Anil 
    I am going to Delhi. Lets meet on 7th Jan 2018
    Have a great day
    Regards
    Team Victory
    ------------------------

    sunita.txt
    -----------------------
    Hello Sunita 
    I am going to Delhi. Lets meet on 7th Jan 2018
    Have a great day
    Regards
    Team Victory
    ------------------------
'''
print('Answer for Question 16 Begins\n')

file1 = open("names.txt","w")
list_of_names = ["Anil \n","sunita \n","suman \n","lokesh \n","Sumita \n","John \n","Johny \n"]
file1.writelines(list_of_names)
file1.close()
print('Names.txt successfully written')

file2 = open("body.txt","w")
body = ["I am going to Delhi. Lets meet on 7th Jan 2018 \n","Have a great day \n","Regards \n","Team Victory"]
file2.writelines(body)
file2.close()
print('body.txt successfully written')


file2=open("body.txt")
body_content=file2.read()
file2.close()

with open('names.txt','r') as file1:
    for line1 in file1:
        name = line1.strip()
        filename = "%s.txt" % name
        file3 = open(filename, "w")
        file3.writelines(filename)
        file3.writelines('\n-----------------------\n')
        file3.writelines('Hello '+line1)
        file3.writelines(body_content)
        file3.writelines('\n-----------------------')
        file3.close()

print('All files have been successfully written')
print('\n')