import pandas as pd

df = pd.read_csv("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/Python Data Science projects/Startup Growth Investment project/startup_growth_investment_data.csv" , delimiter= ",")

print(df)
print("df - Data Type" , df.dtypes)
print("df.info():" , df.info())

print("Last three rows:")
print(df.tail(3))

print("First three rows:")
print(df.head(3))
print()

print("Summary of statistics of dataframe:" , df.describe())

print("Total rows and coloumns in dataframe:" , df.shape)
print()

# for one coloumn
Industry = df['Industry']
print("Access the name coloumn :")
print(Industry)
print()

# access multiple coloumns
fund_country = df[['Funding Rounds' , 'Country']]
print("Access multiple coloumns :")
print(fund_country)
print()

# .loc operations
single_row = df.loc[2]
print("single row:" , single_row)

multiple_rows = df.loc[[1,3]]
print("Multiple ros:" , multiple_rows)

rows_1 = df.loc[1:5]
print("Rows from 1 to 5 :" , rows_1)

rows_2 = df.loc[df['Country'] == "Germany"]
print("Conditional selection of rows :" , rows_2)

rows_3 = df.loc[:1, 'Country']
print("selecting single coloumn:" , rows_3)

rows_4 = df.loc[:2 ,['Country' , 'Year Founded']]
print("selecting multiple coloumns:" , rows_4)

rows_5 = df.loc[:1 , 'Country' : 'Year Founded']
print("selecting slice of coloumns :" , rows_5)

rows_6 = df.loc[df['Country'] == "Germany" , 'Industry' : 'Year Founded']
print("Combined row and coloumn selection :" , rows_6)
print()

# CASE 2 : using .loc with index_col

df_index_col = pd.read_csv("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/Python Data Science projects/Startup Growth Investment project/startup_growth_investment_data.csv" , delimiter= ",")

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

row_1 = df_index_col.loc[5]
print("Selecting a single row :" , row_1)

# CASE 3 : using .iloc

row_1 = df_index_col.iloc[1]
print("Single row using iloc :" , row_1)

row_2 = df_index_col.iloc[[2 , 3 , 5]]
print("Selecting multiple rows :" , row_2)

row_3 = df_index_col.iloc[1 : 3]
print("Selecting a slice of rows :" , row_3)

row_4 = df_index_col.iloc[: , 3]
print("Selecting single coloumn :" , row_4)

row_5 = df_index_col.iloc[: , [2 , 4]]
print("Selecting multiple coloumns :" , row_5)

row_6 = df_index_col.iloc[: , 3 : 5]
print("Selecting a slice of coloumns :" , row_6)

row_7 = df_index_col.iloc[[2 , 3 , 4] , 1 : 5]
print("Combined rows and coloumns :" , row_7)

# Next Run

# add a new row
#Startup_5,EdTech,9,1645080294.64,6887965942.865217,48,India,2011,192.0

df.loc[len(df.index)] = ["Startup_5" , "EdTech " , 9 , 1645080294.64
                          , 6887965942.865217 , 48 , "India" , 2011 , 192.0]  

print("Modified DataFrame :")  
print(df)
print()

# Remove rows/coloumns from pandas DataFrame

# delete row with index 2
df.drop(2 , axis=0 , inplace=True)
# delete row with index 3
df.drop(index=3 , inplace=True)
# delete row with index 3 & 5
df.drop([1 , 5] , axis=0 , inplace=True)
print("Modified Dataframe Delete Rows :" , df)

# delete city coloumn
df.drop('Country' , axis=1 , inplace=True)
# delete keys coloumn
df.drop(columns='Valuation (USD)' , inplace=True)
print("Modified Data Frame :")
print(df)

# Rename labels in a DataFrame
df.rename(columns={'Country' : 'Country_name'} , inplace=True)
# Rename multiple coloumns
df.rename(mapper={'Industry' : 'Industry_name' , 'Year Founded' : 'new_Year Founded'} , axis=1 , inplace=True)
print("Modified DataFrame :")
print(df)

# Rename rows in a DataFrame
df.rename(index={1 : 5} , inplace=True)
# Rename multiple rows in DataFrame
df.rename(mapper={2 : 6 , 3 : 7} , axis=0 , inplace=True)
print("Modified DataFrame :")
print(df)

# query() to select data
selected_rows = df.loc[(df['Number of Investors'] == 50) | (df['Industry_name'] == 'EdTech')]
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='Number of Investors')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['Growth Rate (%)' , 'Number of Investors'])
print(df1.to_string(index=False))   

# group by operations 
grouped = df.groupby('Number of Investors')['Investment Amount (USD)'].sum()
print(grouped.to_string())
print("grouped :" , len(grouped))

# PANDAS DATA CLEANING
df_cleaned = df.dropna()
print("Cleaned Data : \n" , df_cleaned)

df.fillna(0 , inplace=True)
print("Data after filling NaN with 0 : \n" , df)

# create a list named data
data = [3 ,4 ,5 ,6]
array1 = pd.array(data)
print(array1)

int_array  = pd.array([1 , 2 , 3 , 4 , 5] , dtype='int')
print(int_array)
print()