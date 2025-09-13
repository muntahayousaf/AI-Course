import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\OneDrive\\Documents\\GitHub\\AI-Course\\Pandas-Numpy-Seaborn practice\\Startup Growth Investment project\\startup_growth_investment_data.csv" , delimiter= ",")

sns.set_theme(style='darkgrid')
sns.lineplot(x='Industry' , y='Growth Rate (%)' , data=df)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='Industry' , y='Growth Rate (%)' , data=df)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='Industry' , y='Growth Rate (%)' , data=df)
plt.show()

# customizing themes
sns.set_theme(style='darkgrid' , rc={'axes.facecolor' : 'white' , 'grid.color' : 'grey'})
sns.lineplot(x='Industry' , y='Growth Rate (%)' , data=df)
plt.show()

print(df.dtypes)
dffilter = df.head(10)
dffilter21 = df.head(21)

# kind = 'hist'
g = sns.displot(data=dffilter , x='Industry' , y='Growth Rate (%)' , hue='Number of Investors' , kind='hist')
g.figure.suptitle("sns.displot(data=dffilter , x='Industry' , y='Growth Rate (%)' , hue='Number of Investors' , kind='hist')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g = sns.displot(data=dffilter , x='Number of Investors' , y='Growth Rate (%)' , kind='kde')
g.figure.suptitle("sns.displot(data=dffilter , x='Industry' , y='Growth Rate (%)' , kind='kde')")
g.figure.show()
read = input("Wait for me.....")

# kind = 'kde'
g=sns.kdeplot(data=dffilter , x='Investment Amount (USD)')
g.figure.suptitle("sns.kdeplot(data=dffilter , x='Industry')")
g.figure.show()
read = input("Wait for me.....")

g = sns.histplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)' , hue='Valuation (USD)' ,  multiple='stack')
g.figure.suptitle("sns.histplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)' , hue='Valuation (USD)' ,  multiple='stack')")
g.figure.show()
read = input("Wait for me.....")

g = sns.scatterplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')
g.figure.suptitle("sns.scatterplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')")
g.figure.show()
read = input("Wait for me.....")

# line plot with possibility of several semantic group

g = sns.lineplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')
g.figure.suptitle("sns.lineplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')")
g.figure.show()
read = input("Wait for me.....")

# show point estimates and errors as rectangular bars

g = sns.barplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)' , legend=False)
g.figure.suptitle("sns.barplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)' , legend=False)")
g.figure.show()
read = input("Wait for me.....")

# Figour level interface for drawing categorical plots onto a FaceGrid

g = sns.catplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')
g.figure.suptitle("sns.catplot(data=dffilter , x='Investment Amount (USD)' , y='Growth Rate (%)')")
g.figure.show()
read = input("Wait for me.....")

# Plot rectangular data as a color - encoded matric

glue = dffilter.pivot(columns="Investment Amount (USD)" , values="Growth Rate (%)")
g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(columns=Investment Amount (USD) , values=Growth Rate (%))")
g.figure.show()
read = input("Wait for me.....")
