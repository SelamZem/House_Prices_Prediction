def clean(filepath):
    # read data
    data = pd.read_csv(filepath, index_col="Id")

    # drop columns which more than half of the data is lost
    data = data.drop(["PoolQC", "MiscFeature", "Alley", "Fence", "MasVnrType","FireplaceQu"], axis=1)

    # fill missing values with mean(for numberical data) and mode(for catagorical data)
    # numerical columns
    data.fillna(data.select_dtypes(include='number').mean().round(2), inplace=True)
    # categorical columns
    categorical_cols = data.select_dtypes(include='object').columns
    for col in categorical_cols:
        data[col].fillna(data[col].mode()[0], inplace=True)

    #Drop multicollinear columns
    data = data.drop(["GarageArea","GarageYrBlt","TotRmsAbvGrd","1stFlrSF","2ndFlrSF","BsmtFullBath"], axis=1)

    #Drop columns based on their relation with the SalePrice(Which the correlatin is b/n -0.15 and 0.15 and BsmtUnfSF is highly skewed)
    data = data.drop(['MSSubClass','OverallCond','BsmtFinSF2','LowQualFinSF','BsmtHalfBath','KitchenAbvGr','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold','YrSold', "BsmtUnfSF"],axis=1)


    #covering 99% of the data(clipping the outliers)
    numerical_features = data.select_dtypes(include='number').columns
    for feature in numerical_features:
        cap_value = data[feature].quantile(0.99)  
        data[feature] = data[feature].clip(upper=cap_value)  

    #Skewness
    high_skewness_features = ['LotArea', 'MasVnrArea', 'GrLivArea', 'WoodDeckSF', 'OpenPorchSF']
    for feature in high_skewness_features:
        data[feature] = np.log1p(data[feature])

    #label encoding binary features
    binary_features=['Street', 'Utilities', 'CentralAir']
    le = LabelEncoder()
    # Apply label encoding to each binary column
    for col in binary_features:
        data[col] = le.fit_transform(data[col]) 

    
    return data