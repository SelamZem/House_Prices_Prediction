X = data.drop('SalePrice', axis=1)
y = data['SalePrice']

# Split the data into training and validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)