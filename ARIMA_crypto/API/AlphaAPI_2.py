import requests
import pandas as pd

def fetch_data(function, interval, maturity=None, apikey='YOUR_API_KEY'):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': function,
        'interval': interval,
        'apikey': apikey
    }
    if maturity:
        params['maturity'] = maturity
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_response = response.json()
        if 'data' in json_response:
            return json_response['data']
        else:
            print("Unexpected JSON structure:", json_response)
            return []
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return []

# List of maturities for treasury yield
maturities = ['3month', '2year', '5year', '7year', '10year', '30year']

# API Key
apikey = 'UMQIMYBO5YHGCMNE'

# Initialize DataFrame
yield_data = None

# Fetch and process Treasury Yield data
for maturity in maturities:
    data = fetch_data('TREASURY_YIELD', 'daily', maturity, apikey)
    if data:
        df = pd.DataFrame(data)
        if yield_data is None:
            yield_data = df[['date', 'value']].rename(columns={'value': f'y_{maturity}'})
        else:
            df = df.rename(columns={'value': f'y_{maturity}'})
            yield_data = pd.merge(yield_data, df, on='date', how='outer')

# Fetch and process Federal Funds Rate data
federal_funds_data = fetch_data('FEDERAL_FUNDS_RATE', 'daily', apikey=apikey)
if federal_funds_data:
    federal_funds_df = pd.DataFrame(federal_funds_data)
    federal_funds_df.rename(columns={'value': 'federal_funds_rate'}, inplace=True)
    yield_data = pd.merge(yield_data, federal_funds_df, on='date', how='left')

# Convert 'date' to datetime and filter data for the year 2021
yield_data['date'] = pd.to_datetime(yield_data['date'])
filtered_data = yield_data[(yield_data['date'] >= '2021-01-01') & (yield_data['date'] <= '2023-11-23')]

# Save to CSV
filtered_data.to_csv('Alpha_interest_yield_daily.csv', index=False)

print("Data fetching and saving to CSV completed.")

