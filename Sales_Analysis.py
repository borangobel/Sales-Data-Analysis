import pandas as pd
import os
import matplotlib.pyplot as plt

#Merging 12 months dales data into a single CSV File
def create_all_data ():
    df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')

    files = [file for file in os.listdir('./Sales_Data')]

    all_months_data = pd.DataFrame()

    for file in files:
        df = pd.read_csv("./Sales_Data/"+file)
        all_months_data = pd.concat([all_months_data,df])

    all_months_data.to_csv("all_data.csv",index = False)


all_data = pd.read_csv('all_data.csv')
# print(all_data.head())


#Adding Column

all_data['Month'] = all_data['Order Date'].str[0:2]

month_map = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

all_data['Month'] = all_data['Month'].map(month_map)

    
    


#Data Cleaning
all_data.isna().sum()

all_data.dropna(how='all',inplace = True)
all_data.head()

all_data[all_data['Month'].isna()]

all_data.dropna(subset = ['Month'],inplace = True)
all_data.isna().sum()

all_data.info()

### EDITING DATA TYPES
all_data['Order ID'] = all_data['Order ID'].astype(int)
all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(int)
all_data['Price Each'] = all_data['Price Each'].astype(float)
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

all_data.dtypes

### Question 1 : WHAT IS THE BEST SALES MONTH ?
all_data['Month'].value_counts()

best_sales_month = all_data.groupby('Month').apply(lambda x: (x['Quantity Ordered'] * x['Price Each']).sum())
best_sales_month

plt.figure(figsize = (10,6))
best_sales_month.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Month')
plt.xlabel('Month')
plt.ylabel('Total Sales ($) Million')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


###  Question #2: What city sold the most product?
all_data.head(15)


all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1].strip())
all_data.head()

city_sales = all_data.groupby('City').apply(lambda x: (x['Quantity Ordered'] * x['Price Each']).sum())
city_sales

plt.figure(figsize = (10,6))
city_sales.plot(kind='bar', color = 'purple')
plt.ylabel('Total Sales ($) Million')
plt.xticks(rotation = 45)
plt.title('City Sales USA')
plt.show()
           
