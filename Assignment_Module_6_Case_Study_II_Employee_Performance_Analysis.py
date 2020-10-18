'''
Module 6 : Data Manipulation Case Study II - Employee Performance Analysis

Domain : HR

Focus : Insights from data

Business challenge/requirement :
SFO Public Department - referred to as SFO has captured all the salary data of its employees from year 2011-2014.
Now we are in year 2015 and the organization is facing some financial crisis.
As first step HR wants to rationalize employee cost to save payroll budget.
You have to do data manipulation and analysis on the salary data to answer specific questions for cost savings.

Key issues :
Cost can be saved by figuring out the key pockets of high salaries

Considerations : NONE

Data volume : Approx 150K records across files

Additional information : NA

Business benefits :
Save at least 10% of employee cost by identifying and letting them go

Approach to Solve :
You have to use fundamentals of Pandas covered in module 6 and answer following 5 Questions

1. Compute how much total salary cost has increased from year 2011 to 2014
2. Which Job Title in Year 2014 has highest mean salary?
3. How much money could have been saved in Year 2014 by stopping OverTimePay?
4. Which are the top 5 common job in Year 2014 and how much do they cost SFO ?
5. Who was the top earning employee across all the years?

Enhancements for code :
You can try these enhancements in code

1. Which are the last 5 common job in Year 2014 and how much do they cost SFO?
2. In year 2014 OverTimePay was what percentage of TotalPayBenefits
3. Which Job Title in Year 2014 has lowest mean salary?

'''

import pandas as pd
print('\n')
pd.options.display.float_format = '{:.2f}'.format

df_salaries=pd.read_csv('Salaries.csv',dtype={"Status": "string"})
df_Sal=df_salaries[['TotalPayBenefits','Year']]
df_Sal_Year=df_Sal.groupby('Year')['TotalPayBenefits'].sum().reset_index()
percent_inc_wrt_2014=[]
for element in range(len(df_Sal_Year)):
    percent_inc_wrt_2014.append(((df_Sal_Year.TotalPayBenefits.loc[element]/df_Sal_Year.TotalPayBenefits.loc[0])-1)*100.0)
percent_inc_wrt_2014=pd.DataFrame(percent_inc_wrt_2014,columns=['%_Increase_wrt_2014'])
df_Sal_Year=pd.concat([df_Sal_Year,percent_inc_wrt_2014],axis=1)
print('The percentage increase of salary compared to 2014 for every year is :\n')
print(df_Sal_Year)
print('\n')

df_salaries_Pay=df_salaries[['JobTitle','TotalPayBenefits']][df_salaries.Year.eq(2014)].groupby('JobTitle')['TotalPayBenefits'].mean().reset_index().sort_values(by='TotalPayBenefits',ascending=False).reset_index().drop(['index'],axis=1)
print('Job Title with highest mean salary in the year 2014 is :',df_salaries_Pay.loc[0]['JobTitle'])
print('\n')

v_TotalPay_2014=df_Sal_Year.loc[3]['TotalPayBenefits']
v_overtime_pay_2014=df_salaries['OvertimePay'][df_salaries.Year.eq(2014)].sum()
print('Total Money the company would have saved by stopping Overtime Pay is :',v_overtime_pay_2014)
print('The Overtime Pay in 2014 is :',round((v_overtime_pay_2014/v_TotalPay_2014)*100.0,2),'% of the Total Pay in 2014')
print('\n')

df_common_jobs=df_salaries[['JobTitle','TotalPayBenefits']][df_salaries.Year.eq(2014)].groupby('JobTitle').TotalPayBenefits.agg(['count','sum']).reset_index().sort_values(by='count',ascending=False).reset_index().drop(['index'],axis=1)
print('Top 5 Common Jobs in 2014 are :\n')
for element in range(5):
    print(df_common_jobs.loc[element]['JobTitle'])
print('And the total cost for SFO is :',df_common_jobs.loc[:4]['sum'].sum())
print('\n')

df_least_common=df_common_jobs.sort_values(by='count',ascending=True).reset_index().drop(['index'],axis=1)
print('Top 5 Least Common Jobs in 2014 are :\n')
for element in range(5):
    print(df_least_common.loc[element]['JobTitle'])
print('And the total cost for SFO is :',df_least_common.loc[:4]['sum'].sum())
print('\n')

v_top_employee=df_salaries[['EmployeeName','TotalPayBenefits']].groupby('EmployeeName')['TotalPayBenefits'].sum().reset_index().sort_values(by='TotalPayBenefits',ascending=False).reset_index().drop(['index'],axis=1).loc[0]['EmployeeName']
print('Top earning employee across all years is :',v_top_employee)
print('\n')

print('JobTitle in 2014 with the lowest mean salary is :',df_salaries_Pay.sort_values(by='TotalPayBenefits',ascending=True).reset_index().drop(['index'],axis=1).loc[0]['JobTitle'])
print('\n')