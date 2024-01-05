import pandas as pd
import numpy as np
import itertools
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import pickle
import json

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / (y_true + 1e-6))) * 100

df = pd.read_csv('clean_final.csv', index_col='timestamp')
df.index = pd.to_datetime(df.index)

# Define the p, d, and q range from EDA
p = d = q = range(0, 4)

# d is 0 because we manually differenced  
pdq_combinations = list(itertools.product(p, [0], q)) 

# Dictionary to store the best model details for each coin
best_models = {}

# Define the proportion of the data to use for training
train_proportion = 0.8

# Iterate over each cryptocurrency
for coin_id in df['coin_id'].unique():
    # Prepare target for this coin
    coin_data = df[df['coin_id'] == coin_id]
    coin_data = coin_data.resample('D').first()  # Resample to daily frequency
    coin_data.index.freq = 'D'  # Now it's safe to set frequency to 'D'
    
    # Split the data into training and testing sets
    train_size = int(len(coin_data) * train_proportion)
    train_data = coin_data[:train_size]
    
    y_train = train_data['close_diff']
    
    best_aic = np.inf
    best_bic = np.inf
    best_order = None
    best_model = None
    best_error = np.inf
    
    # Grid search over pdq combinations
    for combination in pdq_combinations:
        try:
            # Fit ARIMA model (no exogenous variables)
            model = sm.tsa.ARIMA(endog=y_train, order=combination)
            results = model.fit()

            # Forecast on training set for error calculation
            predictions = results.predict(start=0, end=len(y_train)-1)
            error = mean_absolute_percentage_error(y_train, predictions)
            
            # if better accuracy Compare AIC and BIC
            if error < best_error and (results.aic < best_aic or results.bic < best_bic):
                best_aic = results.aic
                best_bic = results.bic
                best_order = combination
                best_model = results
                best_error = error
                
        except Exception as e:
            # combination not valid or model fails to converge
            print(f"An error occurred for {coin_id} with order {combination}: {e}")
            continue  
    
    # Store best model info
    best_models[coin_id] = {
        'order': best_order,
        'aic': best_aic,
        'bic': best_bic,
        'error': best_error,
        'model': best_model
    }
    
best_models_summary = {
    coin: {
        'order': model_info['order'],
        'aic': model_info['aic'],
        'bic': model_info['bic'],
        'error': model_info['error']
    } for coin, model_info in best_models.items()
}

# Append results to the file
with open('best_arima_models.txt', "a") as file:
    file.write("Features used:\n")
    file.write("Close_diff Time Series" + "\n")
    file.write("Best Models:\n")
    for coin, model_info in best_models.items():
        error_str = f'{coin}: Error = {model_info["error"]}\n'
        file.write(error_str)

print(best_models)