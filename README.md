# Body Fat % Prediction Model
[![scikit-learn](https://img.shields.io/badge/scikit_learn-Machine%20Learning-orange)](https://scikit-learn.org)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-green)](https://numpy.org)
[![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-red)](https://pandas.pydata.org)

- Created a tool that predicts a person's body fat (MAE ~ 3.3%) to help people better understand their health and caloric needs
- Collected and preprocessed Kaggle Data Set of 253 data points
- Performed an exploratory data analysis to understand correlations in data and created visualizations
- Feature engineered to only include easy-to-obtain inputs for user convenience
- Built ***Linear regression***, ***Random Forest Regressors***, and ***Support Vector Regression*** models and optimized using GridsearchCV to reach the best model.
- Created a client-facing API using flask and built an interactive front-end display with HTML, CSS, and JS. 


Languages: Python, HTML, JS, CSS

Packages: pandas, numpy, sklearn, matplotlib, seaborn, flask

# Project Steps
## 1. Data Collection and Preprocessing
Gathered a dataset containing physical attributes (such as Age, Weight, Height, Neck circumference, etc.) and corresponding body fat percentages.
Performed data preprocessing tasks, including handling missing values and ensuring data consistency.
## 2. Exploratory Data Analysis (EDA)
I looked at the distributions of the data and explored the correlation of different attributes and body fat statistics. Below are some highlights of the visualizations I created.

![Image Alt Text](/CorrelationTable.png)
![Image Alt Text](/BodyFat.png)
![Image Alt Text](/Abdomen.png)

## 3. Feature Engineering
Split the dataset into predictor variables (attributes) and the target variable (body fat percentage).
Also dropped the density attribute from my experiment to avoid multicollinearity and to improve the user's ease of use. I want the user to be able to obtain an accurate BF% estimate with as little as a tape measure. 
## 4. Model Selection
First, I  split the data into train and test sets with a test size of 20%.

I then tried three different models and evaluated them using Mean Absolute Error, Mean Squared Error, and R^2 Score. 
I tried three different models:

Linear Regression – Baseline for the model

Random Forest Regressor – Because it's great at finding patterns in complex data, which is important since body fat can be influenced by various factors.

Support Vector Regression – explored Support Vector Regression to capture intricate relationships in the data, as body fat can be influenced by both linear and nonlinear factors, and SVR can handle such complexity.
## 4. Hyperparameter Tuning and Model Performance

Used GridSearchCV for hyperparameter tuning. By defining a grid of hyperparameters, I was able to systematically explore various combinations and identify the best parameters that optimize the model's performance. Through cross-validation, GridSearchCV evaluated each combination of hyperparameters, returning the set that produced the most accurate predictions. This method not only streamlined the hyperparameter tuning process but also helped in enhancing the overall performance of the model.

Performance after Optimization:

- Linear Regression : MAE = 3.32925
- Random Forest: MAE = 3.39829
- Support Vector Regression: MAE = 3.45777

In this case, Linear Regression outperformed both Random Forest and Support Vector Regression, likely for the following reasons:
1) Underlying relationships between attributes
2) Overfitting in complex models
3) Simplicity and efficiency

## 5. Model productionization
Developed a user-friendly web application for body fat prediction using Flask API, HTML, JS, and CSS.
Integrated the trained model into the web application to enable users to input their physical attributes and receive a predicted body fat percentage.

![Image Alt Text](/Client_Side.jpeg)
![Image Alt Text](/Prediction.jpeg)

# Summary
The Body Fat Prediction project aimed to create a user-friendly tool for estimating body fat percentages based on various physical attributes. The project covered data preprocessing, exploratory data analysis, feature engineering, model selection, and creation of a web application. The application allows users to input their personal attributes and receive an estimated body fat percentage, providing valuable insights for individuals interested in monitoring their health and fitness levels.
