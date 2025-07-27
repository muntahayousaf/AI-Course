import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/Python Data Science projects/FastFood Restaurant Project/FastFoodRestaurantsV2.csv" , delimiter= ",")

sns.set_theme(style='darkgrid')
sns.lineplot(x='longitude' , y='city' , data=df)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='longitude' , y='city' , data=df)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='longitude' , y='city' , data=df)
plt.show()

# customizing themes
sns.set_theme(style='darkgrid' , rc={'axes.facecolor' : 'white' , 'grid.color' : 'grey'})
sns.lineplot(x='longitude' , y='city' , data=df)
plt.show()

print(df.dtypes)
dffilter = df.head(10)
dffilter21 = df.head(21)

# kind = 'hist'
g = sns.displot(data=dffilter , x='longitude' , y='city' , hue='latitude' , kind='hist')
g.figure.suptitle("sns.displot(data=dffilter , x='longitude' , y='city' , hue='latitude' , kind='hist')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g = sns.displot(data=dffilter , x='longitude' , y='latitude' , kind='kde')
g.figure.suptitle("sns.displot(data=dffilter , x='longitude' , y='city' , kind='kde')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g=sns.kdeplot(data=dffilter , x='latitude')
g.figure.suptitle("sns.kdeplot(data=dffilter , x='latitude')")
g.figure.show()
read = input("Wait for me.....")

g = sns.histplot(data=dffilter , x='longitude' , y='city' , hue='latitude' ,  multiple='stack')
g.figure.suptitle("sns.histplot(data=dffilter , x='longitude' , y='city' , hue='latitude' ,  multiple='stack')")
g.figure.show()
read = input("Wait for me.....")

g = sns.scatterplot(data=dffilter , x='longitude' , y='city')
g.figure.suptitle("sns.scatterplot(data=dffilter , x='longitude' , y='city')")
g.figure.show()
read = input("Wait for me.....")

# line plot with possibility of several semantic group

g = sns.lineplot(data=dffilter , x='longitude' , y='city')
g.figure.suptitle("sns.lineplot(data=dffilter , x='longitude' , y='city')")
g.figure.show()
read = input("Wait for me.....")

# show point estimates and errors as rectangular bars

g = sns.barplot(data=dffilter , x='longitude' , y='city' , legend=False)
g.figure.suptitle("sns.barplot(data=dffilter , x='longitude' , y='city' , legend=False)")
g.figure.show()
read = input("Wait for me.....")

# Figour level interface for drawing categorical plots onto a FaceGrid

g = sns.catplot(data=dffilter , x='longitude' , y='city')
g.figure.suptitle("sns.catplot(data=dffilter , x='longitude' , y='city')")
g.figure.show()
read = input("Wait for me.....")

# Plot rectangular data as a color - encoded matric

glue = dffilter.pivot(columns="city" , values="longitude")
g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(columns=city , values=longitude)")
g.figure.show()
read = input("Wait for me.....")
