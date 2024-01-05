import pandas as pd
import numpy as np
import itertools
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import pickle

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / (y_true + 1e-6))) * 100

# Load the best models from file
with open('sent_nodiff_arimax_models.pkl', 'rb') as f:
    best_models = pickle.load(f)

df = pd.read_csv('clean_nodiff_sentiment.csv', index_col='timestamp')
df.index = pd.to_datetime(df.index)

# Define the exogenous features
exog_features = ["Market Cap", 'open', 'high', 'low', '2yr_yield', '5yr_yield', '7yr_yield', 'positive', 'negative', 'neutral']

# Define the proportion of the data used for training
train_proportion = 0.8

# Store residuals
residuals_df = pd.DataFrame()

# Iterate over each cryptocurrency for test predictions
for coin_id in best_models.keys():
    coin_data = df[df['coin_id'] == coin_id]

    # Resample to daily frequency
    coin_data = coin_data.resample('D').first() 
    coin_data.index.freq = 'D'

    train_size = int(len(coin_data) * train_proportion)
    test_data = coin_data.iloc[train_size:]
    
    y_test = test_data['close']
    X_test = test_data[exog_features]

    # Load the model
    model = best_models[coin_id]['model']

    if model is not None:
        # Generate predictions
        predictions = model.get_forecast(steps=len(y_test), exog=X_test).predicted_mean
        error = mean_absolute_percentage_error(y_test, predictions)
        # Append error results to the file
        with open('sent_nodiff_arimax_model_testerror.txt', "a") as file:
            error_str = f'Prediction error for {coin_id}: {error}\n'
            file.write(error_str)
    else:
        print(f'No model available for {coin_id}')

    # Calculate residuals for best model 
    residuals = y_test - predictions

    # Append residuals to the DataFrame
    residuals_df = residuals_df.append(pd.DataFrame({
        'Date': test_data.index,
        'Coin': coin_id,
        'actual': y_test,
        'predicted': predictions,
        'Residual': residuals
    })) 

# Save residuals to a CSV file
residuals_df.to_csv('test_residuals_nodiff_sent.csv', index=False)