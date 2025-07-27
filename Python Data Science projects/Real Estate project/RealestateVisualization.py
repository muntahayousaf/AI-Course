import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/Python Data Science projects/Real Estate Project/realestateV1_data.csv" , delimiter= ",")

sns.set_theme(style='darkgrid')
sns.lineplot(x='house_size' , y='price' , data=df)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='house_size' , y='price' , data=df)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='house_size' , y='price' , data=df)
plt.show()

# customizing themes
sns.set_theme(style='darkgrid' , rc={'axes.facecolor' : 'white' , 'grid.color' : 'grey'})
sns.lineplot(x='house_size' , y='price' , data=df)
plt.show()

print(df.dtypes)
dffilter = df.head(10)
dffilter21 = df.head(21)

# kind = 'hist'
g = sns.displot(data=dffilter , x='house_size' , y='price' , hue='acre_lot' , kind='hist')
g.figure.suptitle("sns.displot(data=dffilter , x='house_size' , y='price' , hue='acre_lot' , kind='hist')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g = sns.displot(data=dffilter , x='acre_lot' , y='price' , kind='kde')
g.figure.suptitle("sns.displot(data=dffilter , x='acre_lot' , y='price' , kind='kde')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g=sns.kdeplot(data=dffilter , x='acre_lot')
g.figure.suptitle("sns.kdeplot(data=dffilter , x='acre_lot')")
g.figure.show()
read = input("Wait for me.....")

g = sns.histplot(data=dffilter , x='acre_lot' , y='price' , hue='bed' ,  multiple='stack')
g.figure.suptitle("sns.histplot(data=dffilter , x='acre_lot' , y='price' , hue='bed' ,  multiple='stack')")
g.figure.show()
read = input("Wait for me.....")

g = sns.scatterplot(data=dffilter , x='acre_lot' , y='price')
g.figure.suptitle("sns.scatterplot(data=dffilter , x='acre_lot' , y='price')")
g.figure.show()
read = input("Wait for me.....")

# line plot with possibility of several semantic group

g = sns.lineplot(data=dffilter , x='acre_lot' , y='price')
g.figure.suptitle("sns.lineplot(data=dffilter , x='acre_lot' , y='price')")
g.figure.show()
read = input("Wait for me.....")

# show point estimates and errors as rectangular bars

g = sns.barplot(data=dffilter , x='acre_lot' , y='price' , legend=False)
g.figure.suptitle("sns.barplot(data=dffilter , x='acre_lot' , y='price' , legend=False)")
g.figure.show()
read = input("Wait for me.....")

# Figour level interface for drawing categorical plots onto a FaceGrid

g = sns.catplot(data=dffilter , x='acre_lot' , y='price')
g.figure.suptitle("sns.catplot(data=dffilter , x='acre_lot' , y='price')")
g.figure.show()
read = input("Wait for me.....")

# Plot rectangular data as a color - encoded matric

glue = dffilter.pivot(columns="acre_lot" , values="price")
g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(columns=acre_lot , values=price)")
g.figure.show()
read = input("Wait for me.....")
