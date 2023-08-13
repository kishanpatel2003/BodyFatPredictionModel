# Body Fat % Prediction Tool: Support Vector Regression Model
In this project, I developed a tool for predicting body fat percentage using machine learning techniques. The primary objective was to create an accurate predictive model to help individuals estimate their body fat percentage based on various physical attributes. The project encompassed data preprocessing, exploratory data analysis (EDA), feature engineering, model selection (chose between regression, random forest regressor, and support vector regression model**), and creation of a full-stack prediction web application.

# Project Steps
## 1. Data Collection and Preprocessing
Gathered a dataset containing physical attributes (such as Age, Weight, Height, Neck circumference, etc.) and corresponding body fat percentages.
Performed data preprocessing tasks, including handling missing values and ensuring data consistency.
## 2. Exploratory Data Analysis (EDA)
![Image Alt Text](/Correlation Table.png)
![Image Alt Text](/BodyFat.png)

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



## 5. Model productionization
Developed a user-friendly web application for body fat prediction using Flask, HTML, and CSS.
Integrated the trained model into the web application to enable users to input their physical attributes and receive a predicted body fat percentage.
Code and Resources Used
Python Version: (Your Python version)

Packages: pandas, numpy, sklearn, matplotlib, seaborn, flask

GitHub Repository: (Link to your GitHub repository for the project, if applicable)

Web Deployment Tutorial: (Any resources or tutorials you followed to deploy the Flask web application)

# Summary
The Body Fat Prediction project aimed to create a user-friendly tool for estimating body fat percentage based on various physical attributes. The project covered data preprocessing, exploratory data analysis, feature engineering, model selection, and deployment of a web application. The application allows users to input their personal attributes and receive an estimated body fat percentage, providing valuable insights for individuals interested in monitoring their health and fitness levels.
