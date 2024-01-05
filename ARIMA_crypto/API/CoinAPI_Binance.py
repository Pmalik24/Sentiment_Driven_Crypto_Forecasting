#'BINANCEFTSC_FTS_BTC_USD_221230'
#'BINANCEFTSC_FTS_ETH_USD_230331'
#'BINANCEFTSC_FTS_LTC_USD_231229'
import requests
import json
import csv
from datetime import datetime

def date_to_iso8601(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').isoformat()

# List of metrics
metrics = [
    "DERIVATIVES_FUNDING_RATE_CURRENT",
    "DERIVATIVES_MARK_PRICE",
    "LIQUIDATION_PRICE",
    "LIQUIDATION_AVERAGE_PRICE",
    "LIQUIDATION_ORDER_LAST_FILLED_QUANTITY",
    "LIQUIDATION_FILLED_ACCUMULATED_QUANTITY",
    "LIQUIDATION_ORDER_TRADE_TIME, LIQUIDATION_TIME_IN_FORCE"
]

# List of symbols
symbols = [
    'BINANCEFTSC_FTS_BTC_USD_221230',
    'BINANCEFTSC_FTS_ETH_USD_230331',
    'BINANCEFTSC_FTS_LTC_USD_231229'
]

# API Endpoint and Parameters
url = "https://rest.coinapi.io/v1/metrics/symbol/history"
headers = {'X-CoinAPI-Key': '4DA7BD7D-AD8D-4FDB-AE99-F52210995350'}  # Replace with your actual API key

# Prepare to write to CSV
with open('CoinAPI_BinanceFTSC.csv', 'w', newline='') as file:
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
                writer.writerow([metric, symbol, json.dumps(data)])  # Write data to CSV
            else:
                print(f"Failed to fetch data for {metric} with {symbol}")

# Inform when the script has finished running
print("Data fetching and saving to CSV completed.")
