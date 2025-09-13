# Question 2.1 - 2.16 

# Question 2.1 

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 
'Kevin', 'Jonas'], 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

# DataFrame Basic Summary Information

df = pd.DataFrame(exam_data , index=labels)

print(df.info())
print(df.shape)
print(df.index)
print(df.columns)
print()

#Question 2.2  [ Same DataFrame as Question 2] 

#Selecting the First 3 Rows
print("First 3 rows :" , "\n")
print(df.head())
print()

#Question 2.3  [ Same DataFrame as Question 2] 

#Selecting 'name' and 'score' Columns - Write a Pandas program to select the 'name' and 'score' columns 
#from the following DataFrame.

print("Selected Columns :" , "\n")
df1 = pd.DataFrame(exam_data , columns=['name' , 'score'])
print(df1 , "\n")

#Question 2.4  -  [ Same DataFrame as Question 2]
 
#Selecting Specific Columns and Rows - Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the given 
#data frame. 

print("Selected Rows and columns are :" , "\n")
selected_rows = df.iloc[[1, 3, 5, 6]][['name', 'score']]
print(selected_rows)

#Question 2.5 [ Same DataFrame as Question 2] 

#Write a Pandas program to select the rows where the number of attempts in the examination is 
#greater than 2

print('No of attempts greater than 2 :' , "\n")
print(df[df['attempts'] > 2])

#Question 2.6 [ Same DataFrame as Question 2] 

#Write a Pandas program to count the number of rows and columns of a DataFrame.

rows , columns = df.shape

print("Total number of rows :" , rows)
print("Total number of columns :" , columns)

#Question 2.7 [ Same DataFrame as Question 2] 

#Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

print("Filtered Dataframe :" , "\n")
filtered_df = df[(df['score'] >= 15) & (df['score'] <= 20)]
print(filtered_df)
print()

#Question 2.8 [ Same DataFrame as Question 2] 
#Write a Pandas program to select the rows where number of attempts in the examination is less than 2 
#and score greater than 15.

filtered_df1 = df[(df['attempts'] < 2) & (df['score'] > 15)]
print(filtered_df1)
print()

#Question 2.9 [ Same DataFrame as Question 2] 
#Write a Pandas program to change the score in row 'd' to 11.5.

df.at['d', 'score'] = 11.5
print(df.loc['d'])
print

#Question 2.10 [ Same DataFrame as Question 2] 
#Write a Pandas program to calculate the mean of all students' scores. Data is stored in a dataframe. 

mean_score = df['score'].mean()
print("Mean of all students :" , mean_score)
print()

#Question 2.11 [ Same DataFrame as Question 2] 

#Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now 
#delete the new row and return the original DataFrame.

new_row = pd.Series({'name': 'Zara', 'score': 15.0, 'attempts': 2, 'qualify': 'yes'}, name='k')
df = pd.concat([df, pd.DataFrame([new_row])])


print("DataFrame after adding row 'k':")
print(df)

df = df.drop('k')

print("\n DataFrame after deleting row 'k':")
print(df)

#Question 2.12 [ Same DataFrame as Question 2] 

#Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in 
#ascending order.

sorted_data = df.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sorted Data :" , sorted_data)
print()

#Question 2.13[ Same DataFrame as Question 2] 

#Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and 
#False.

df['qualify'] = df['qualify'].replace({'yes': True, 'no': False})
print("Replaced dataframe :" , df)
print()

#Question 2.14 [ Same DataFrame as Question 2] 

#Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame. 

df['name'] = df['name'].replace({'James':'Suresh'})
print("new name :" , df)
print()

#Question 2.15 [ Same DataFrame as Question 2] 

#Write a Pandas program to delete the 'attempts' column from the DataFrame.

df = df.drop('attempts', axis=1)
print(df)
print()

#Question 2.16 [ Same DataFrame as Question 2] 
#Write a Pandas program to write a DataFrame to CSV file using tab separator.

df.to_csv('exam_data_tab.csv')
print("csv file")
print("End")