import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("C:\\Users\\admin\\OneDrive\\Documents\\GitHub\\AI-Course\\WEEK 4 Assignments\\zameencom-property-data-By-Kaggle-Short.csv",
                 sep = None , index_col="property_id")
print(df)

print(df.info())
print(df.describe())
print(df.shape)
print(df.dtypes)

# Linear Regression relationship between variables

df.plot.scatter( x = "bedrooms" , y = "price" , title = "Relationship between bedrooms and price")
plt.show()

X = df.drop("price" , axis=1)
X = pd.get_dummies(X, drop_first=True)
y = df["price"]

# splitting data

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size=0.25 , random_state=42
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

def calculate_price(bedrooms, intercept, slope):
    return slope * bedrooms + intercept

sample_values = df["bedrooms"].head(3)

# Call function for each sample value
for val in sample_values:
    sale_amount = calculate_price(val, intercept, slope)
    print(f"bedrooms: {val} → price: {sale_amount}")

y_pred = regressor.predict(X_test)
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n--- Metric Analysis ---")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)