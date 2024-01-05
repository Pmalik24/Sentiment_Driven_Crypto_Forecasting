import requests
import csv
from datetime import datetime

# Function to convert date to UNIX timestamp in milliseconds
def date_to_unix_timestamp(date_str):
    return int(datetime.strptime(date_str, '%Y-%m-%d').timestamp())

# List of coin IDs to loop through

coin_ids = ['wrapped-bitcoin', 'kyber-network-crystal', 'dai', 'filecoin', 'ethereum-classic', 'cosmos', 'algorand', 'aave','bitcoin', 'ethereum', '0x', 'zcash', 'yearn-finance', 'uniswap', 
'uma', 'havven']

vs_currency = 'usd'
start_date = '2021-01-01' 
end_date = '2023-11-24'
count = 0
# Open the CSV file once and write data for each coin
with open('CoinGecko2.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write the headers to the CSV file
    csv_writer.writerow(['coin_id', 'timestamp', 'Market Cap'])

    for coin_id in coin_ids:
        # Constructing the API URL
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
        params = {
            'vs_currency': vs_currency,
            'from': date_to_unix_timestamp(start_date),
            'to': date_to_unix_timestamp(end_date)
        }

        # Making the API call
        response = requests.get(url, params=params)
        data = response.json()


        # Initialize a variable to store the last seen date
        last_seen_date = ""

        # Check if 'market_caps' key is in the response
        if 'market_caps' in data:
            # Loop through each entry in the market_caps
            for entry in data['market_caps']:
                # Convert timestamp to a date string
                date = datetime.fromtimestamp(entry[0]/1000).strftime('%Y-%m-%d')

                # Check if this entry is for a new day
                if date != last_seen_date:
                    market_cap = entry[1]
                    csv_writer.writerow([coin_id, date, market_cap])
                    last_seen_date = date  # Update the last seen date
            print(f'End of Day Market Cap data for {coin_id} has been written to CoinGecko.csv')
        else:
            count += 1
            print(f"Market cap data not available for {coin_id}")

    print(count)