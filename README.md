Linear Regression Project 1
This project involves building a simple linear regression model to predict sales based on advertising budgets across different media channels (TV, Radio, Newspaper). The goal is to explore the relationship between the advertising budget and sales, and to build a predictive model using TV advertising data.

Table of Contents
Project Overview
Installation
Data Inspection
Data Cleaning
Exploratory Data Analysis
Model Building
Saving and Testing the Model
Project Overview
This project follows these steps:

Data Inspection: Load and inspect the data for basic statistics and structure.
Data Cleaning: Identify and handle missing values, if any.
Exploratory Data Analysis (EDA): Analyze the data to understand relationships between variables.
Model Building: Build a linear regression model to predict sales based on TV advertising budgets.
Saving and Testing the Model: Save the trained model and test it using a web service.
Installation
To run this project, you will need the following Python packages:

numpy
pandas
matplotlib
seaborn
scikit-learn
pickle
requests
You can install them using pip:

bash
Copy code
pip install numpy pandas matplotlib seaborn scikit-learn pickle-mixin requests
Data Inspection
First, load and inspect the data to understand its structure and basic statistics.

python
Copy code
import pandas as pd

advertising = pd.read_csv("advertising.csv")
print(advertising.head())
print(advertising.shape)
print(advertising.info())
print(advertising.describe())
Data Cleaning
Count the number of TV advertisements with a budget greater than 150 and check for missing values.

python
Copy code
def count_tv_above_150(advertising):
    count = advertising[advertising['TV'] > 150]['TV'].count()
    return count

print(count_tv_above_150(advertising))
print(advertising.isnull().sum() * 100 / advertising.shape[0])
Exploratory Data Analysis
Visualize the data to understand the relationships between the variables.

python
Copy code
import matplotlib.pyplot as plt
import seaborn as sns

# Outlier Analysis
plt.figure(figsize=(5, 5))
plt.boxplot(advertising.drop('Sales', axis=1))
plt.legend(advertising.drop('Sales', axis=1).columns)
plt.grid()
plt.show()

# Scatter plots and heatmap
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.scatter(advertising['TV'], advertising['Sales'])
plt.title('TV vs Sales')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.grid()

plt.subplot(1, 3, 2)
plt.scatter(advertising['Newspaper'], advertising['Sales'])
plt.title('Newspaper vs Sales')
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.grid()

plt.subplot(1, 3, 3)
plt.scatter(advertising['Radio'], advertising['Sales'])
plt.title('Radio vs Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.grid()
plt.show()

sns.heatmap(advertising.corr(), annot=True)
plt.show()
Model Building
Build a simple linear regression model using TV as the predictor variable.

python
Copy code
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

X = advertising['TV']
y = advertising['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=40)

model_1 = LinearRegression()
model_1.fit(X_train.values.reshape(-1, 1), y_train.values)

y_pred_val = model_1.predict(X_test.values.reshape(-1, 1))
print(f"Model Coefficients: {model_1.coef_}, Intercept: {model_1.intercept_}")
print(f"Predicted Values: {y_pred_val}")

plt.scatter(X_test, y_test)
plt.scatter(X_test, y_pred_val)
plt.plot(X_test, model_1.intercept_ + model_1.coef_ * X_test, 'r')
plt.legend(['Observed data', 'Predicted line'])
plt.show()

print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_val))}")
Saving and Testing the Model
Save the model using pickle and test it with a sample request.

python
Copy code
import pickle as pkl

pkl.dump(model_1, open('model_1.pkl', 'wb'))

import requests
import json

url = 'http://127.0.0.1:5000/predict'
json_1 = {'TV': 50}
data = json.dumps(json_1)
response = requests.post(url, data)
print(response.json())
This README provides a comprehensive overview of the steps taken in this linear regression project, from data inspection to model building and testing. Follow these steps to replicate the analysis and understand the relationship between advertising budgets and sales.
