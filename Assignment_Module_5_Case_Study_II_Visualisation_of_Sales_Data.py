'''
Case Study II - Visualisation of Sales Data

Domain – Retail

Focus – Visualize the sales data

Business challenge/requirement :
BigMart is one of the biggest retailer of Europe and has operations across multiple countries.
You are a data analyst in IT team of BigMart. Invoice and SKU wise Sales Data for Year 2011 is shared with you.
You need to prepare meaningful charts to show case the various sales trends for 2011 to top management.

Key issues :
Data should be displayed pictorially to capture the attention of top management

Considerations :
NONE

Data volume :
Approx 500K records–file BigMartSalesData.csv

Additional information :
NA

Business benefits :
This exercise is an annual exercise and BigMart makes important investment decision based on trends

Approach to Solve :
You have to use fundamentals of Matplotlib covered in module 5 and plot following 4 chart/graph

1. Plot Total Sales Per Month for Year 2011.  How the total sales have increased over months in Year 2011.
   Which month has lowest Sales?
2. Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to visualize than Simple Plot?
3. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
   In which range most of the invoice amounts are concentrated.

Enhancements for code :
You can try these enhancements in code

1. Change the bar chart to show the value of bar
2. In Pie Chart Play With Parameters shadow=True, startangle=90 and see how different the chart looks
3. In scatter plot change the color of Scatter Points

'''

print('Answer for Case Study II - Visualisation of Sales Data Begins ')

import pandas as pd
import matplotlib.pyplot as plt

df_BigMartSalesData=pd.read_csv('BigMartSalesData.csv')

is_2011 =df_BigMartSalesData['Year']==2011

df_sales_month_2011=df_BigMartSalesData[['Amount','Month']][is_2011]

# Point 1 - Simple plot

df_sales_month_2011_sum=df_sales_month_2011.groupby('Month')['Amount'].sum().plot()
plt.yscale('log')
plt.xlabel('Month (2011)')
plt.ylabel('Total Sales')
plt.title('Answer 1 : Simple Plot ')
plt.show()

# Point 2 - Bar Chart

df_sales_month_2011_sum=df_sales_month_2011.groupby('Month')['Amount'].sum().reset_index()
df_sales_month_2011_sum.plot(kind='bar',x='Month',y='Amount',color='red')
Month = df_sales_month_2011_sum['Month'].to_list()
Amount = df_sales_month_2011_sum['Amount'].to_list()
plt.yscale('log')
plt.xlabel('Month (2011)')
plt.ylabel('Total Sales')

for a,b in zip(Month, Amount):
    plt.text(a,b, str(int(b)))

plt.title('Answer 2 : Bar Chart ')
plt.show()

# Point 3 - Pie Chart

df_sales_country_2011=df_BigMartSalesData[['Amount','Country']][is_2011]
df_sales_country_2011_sum=df_sales_country_2011.groupby('Country')['Amount'].sum().reset_index()

Country = df_sales_country_2011_sum['Country'].to_list()
Amount = df_sales_country_2011_sum['Amount'].to_list()

fig = plt.figure(figsize =(20, 10))
plt.pie(Amount, labels = Country, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Answer 3 : Pie Chart ')
plt.tight_layout()
plt.show()

# Point 4 - Scatter Plot

df_amount_count=df_BigMartSalesData.groupby('Amount')['StockCode'].count().reset_index()
Amount = df_amount_count['Amount'].to_list()
StockCode = df_amount_count['StockCode'].to_list()

plt.plot(Amount,StockCode, 'o', color='black')
plt.title('Answer 4 : Scatter Plot ')
plt.ylabel('Count of Items')
plt.xlabel('Amount')
plt.show()

print('\n')