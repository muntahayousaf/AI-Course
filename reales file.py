import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("realestateV1_data.csv" , delimiter= "," )
print(df)

lp = sns.lineplot( data= df , x="house_size" , y="price")
plt.show()

wait = input("wait")