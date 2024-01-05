import requests
import csv
from datetime import datetime

# Function to convert date to timestamp in milliseconds
def date_to_milliseconds(date_str):
    return int(datetime.strptime(date_str, '%Y-%m-%d').timestamp()) * 1000

startdate = date_to_milliseconds("2020-12-30")
enddate = date_to_milliseconds("2021-12-31")
# API call
url = "https://api.coincap.io/v2/assets/bitcoin/history?interval=d1"
#"interval": "d1",
#"start": date_to_milliseconds("2021-08-01"),  # Converted to timestamp
#"end": date_to_milliseconds("2021-08-30")  # Converted to timestamp


response = requests.get(url) #params=params)
data = response.json()
print(data)

'''# Extracting data
rows = []
for entry in data.get('data', []):
    rows.append({
        'date': entry['date'],
        'supply': entry['supply'],
        'maxSupply': entry['maxSupply'],
        'marketCapUsd': entry['marketCapUsd']
    })

# Writing to CSV
csv_file = "CoinCap.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["date", "supply", "maxSupply", "marketCapUsd"])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"Data saved to {csv_file}")'''
