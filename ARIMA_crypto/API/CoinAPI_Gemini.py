import requests
import csv
from datetime import datetime

def date_to_iso8601(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').isoformat()

# Define your list of metrics and symbols
metrics = [
    "AUCTION_LOWEST_ASK",
    "AUCTION_PRICE",
    "AUCTION_RESULT",
    "AUCTION_COLLAR_PRICE",
    "AUCTION_QUANTITY",
    "AUCTION_HIGHEST_BID"
]

symbols = ["GEMINI_SPOT_BTC_USD", "GEMINI_SPOT_ETH_USD", "GEMINI_SPOT_LTC_USD"]  # Replace with your desired symbols

# API Endpoint and Parameters
url = "https://rest.coinapi.io/v1/metrics/symbol/history"
headers = {'X-CoinAPI-Key': 'YOUR_API_KEY'}  # Replace with your actual API key

# Prepare to write to CSV
with open('CoinAPI_Gemini.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Metric", "Symbol", "Data"])  # Writing header

    for metric in metrics:
        for symbol in symbols:
            params = {
                'metric_id': metric,
                'symbol_id': symbol,
                'time_start': date_to_iso8601('2021-08-01'),
                'time_end': date_to_iso8601('2021-08-30'),
                'time_format': 'unix_sec',
            }

            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                writer.writerow([metric, symbol, data])  # Write data to CSV
            else:
                print(f"Failed to fetch data for {metric} and {symbol}")

# Inform when the script has finished running
print("Data fetching and saving to CSV completed.")
