import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("C:\\Users\\admin\\OneDrive\\Documents\\GitHub\\AI-Course\\ml-projects\\real-estate dataset\\Real_Estate_Sales_2001-2022_GL-Short.csv",
                 index_col="Serial Number")

print(df.head(3))
print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

# Linear Regression relationship between variables

df.plot.scatter(x = "Assessed Value" , y = "Sale Amount" , 
                title = "Relationship between Assessed value and Sale Amount")

plt.show()

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))


# convert dataframe created above to array format , that is suited to sk learn

X = df[["Assessed Value"]].to_numpy()
y = df["Sale Amount"].to_numpy()

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X , y,test_size= 0.1 ,random_state=42
)

# Training Linear Regression model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train , y_train)

# print intercept & slope

intercept = regressor.intercept_
print(intercept)

slope = regressor.coef_
print(slope)

def calculate_sale_amount(assessed_value, intercept, slope):
    return slope * assessed_value + intercept

sample_values = df["Assessed Value"].head(3)

# Call function for each sample value
for val in sample_values:
    sale_amount = calculate_sale_amount(val, intercept, slope)
    print(f"Assessed Value: {val} → Sale Amount: {sale_amount}")

y_pred = regressor.predict(X_test)
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n--- Metric Analysis ---")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
