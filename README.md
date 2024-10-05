# House_Prices_Prediction
A machine learning model for predicting house prices using regression analysis(Ridge)

# Data cleaning
Filling missing values with mean and mode,for numerical and catagorical data respectively

# Checking multicollinearity and dropping multicollinear columns
Columns with numerical data type, check their correlation and visualize it with heatmap
columns with correlation value >=0.65 are dropped

# Drop columns based on their relation with the target variable
Columns with correlation range b/n -0.15 and 0.15 (with SalePrice)(are dropped

# Handling Outliers with clipping and skewness
In the training data set irregular distribution of data is noticeable(on Visualization and describe methode)
For the numerical columns the upper 1% is trimmed

# Catagorical data
Columns(object) with 2 unique values are transformed into binary

# Split
The training data set is splitted to 0.8(training data) and 0.2(validation data)

# Model
The Model is Ridge regression model

