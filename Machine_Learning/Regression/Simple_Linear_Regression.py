###################################################################################################
#################################### Simples Linear Regression ####################################
###################################################################################################
##################################### Run on Jupyter Notebook #####################################
###################################################################################################

# Importing the Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

# For .csv data on the same code's folder, otherwise you will have to specify the file address.
# The dataset have to be in format: | ID COLUMN | FEATURE COLUMNS | LABEL COLUMN |
# Just set YOUR_DATA.csv in read_csv pandas function and see what happens

dataset = pd.read_csv('YOUR_DATA.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Linear Regression to the Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results

y_pred = regressor.predict(X_test)

# Try printing y_pred, y_test and observe the results

# Visualizing the Training set results

plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_pred, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()