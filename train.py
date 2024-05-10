import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_evaluate(file_path, lags=6):
    # Load data
    data = pd.read_csv(file_path)
    data_long = pd.melt(data, id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], var_name='Date', value_name='MedianPrice')
    data_long['Date'] = pd.to_datetime(data_long['Date'], format='%Y-%m-%d')

    # Create lag features
    for i in range(1, lags + 1):
        data_long[f'lag_{i}'] = data_long.groupby('RegionName')['MedianPrice'].shift(i)

    # Drop rows with NaN values created by shifting
    data_long.dropna(inplace=True)

    # Select the latest data point as test data
    latest_date = data_long['Date'].max()
    train_data = data_long[data_long['Date'] < latest_date]
    test_data = data_long[data_long['Date'] == latest_date]

    # Split features and target
    X_train = train_data[[f'lag_{i}' for i in range(1, lags + 1)]]
    y_train = train_data['MedianPrice']
    X_test = test_data[[f'lag_{i}' for i in range(1, lags + 1)]]
    y_test = test_data['MedianPrice']

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return rmse

# Example usage

