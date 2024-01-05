import requests
import csv
from datetime import datetime

# Function to convert date to UNIX timestamp in milliseconds
def date_to_unix_timestamp(date_str):
    return int(datetime.strptime(date_str, '%Y-%m-%d').timestamp())

# List of coin IDs to loop through
original_coin_ids = [
'bitcoin', 'amp-token', 'ethereum', 'student-coin', 'dogecoin', 'tether', 'chainlink', 
'dogelon-mars', 'aave', 'kyber-network-crystal', 'rally-2', 'joe', 'ripple', 'cardano', 
'polkadot', 'everscale', 'near', 'qtum', 'safepal', 'zcash', 'digibyte', 'safe-coin-2', 
'litecoin', 'request-network', 'ac-milan-fan-token', 'raydium', 'mask-network', 'tron', 
'arcblock', 'defit', 'perpetual-protocol', 'etha-lend', 'dai', 'safemars', 'orao-network', 
'vechain', 'gemini-dollar', 'ethereum-classic', 'decentraland', 'monero', 'boson-protocol', 
'cere-network', 'uniswap', 'casper-network', 'oasis-network', 'refinable', 'husd', 'chronicle', 
'shiba-inu', 'flow', 'pancakeswap-token', 'hot-cross', 'cow-protocol', 'centrifuge', 'maker', 
'apenft', 'republic-protocol', 'chiliz', 'solana', 'algorand', 'swarm-bzz', 'human-protocol', 
'audius', 'metis-token', 'thorchain', 'the-sandbox', 'gala', 'yield-guild-games', 
'bitcoin-cash-sv', 'palgold', 'dydx', 'matic-network', 'avalanche-2', 'polymath', 'coin98', 
'iotex', 'tenup', 'siacoin', 'serum', 'wax', 'fantom', 'terra-luna-2', 'paxos-standard', 
'demole', 'arweave', 'internet-computer', 'okb', 'celo', 'ontology', 'omisego', 'boba-network', 
'coin98', 'radio-caca', 'shiba-inu', 'moonriver', 'harmony', 'zilliqa', 'convex-finance', 
'tribe-2', 'yin-finance', 'thorchain', 'guild-of-guardians', 'helium', 'loopring', 'pirate-chain', 
'symbol', 'zencash', 'velas', 'ultra', 'kadena', 'the-sandbox', 'syscoin', 'filecoin', 
'ocean-protocol', 'kusama', 'bitcoin-cash', 'bittorrent', 'secret', 'multichain', 'moonbeam', 
'telos', 'klay-token', 'dash', 'osmosis', 'zencash', 'fx-coin', 'serum', 'frax-share', 'frax', 
'my-neighbor-alice', 'true-usd', 'aragon', 'pax-gold', 'nexo', 'stellar', 'gnosis', 'livepeer', 
'safemoon-2', 'quant-network', 'kava', 'wrapped-bitcoin', 'filecoin', 'livepeer', 
'compound-governance-token', 'ravencoin', 'ecash', 'coti', 'ultra', 'tezos', 'quant-network', 
'syscoin', 'icon', 'liquity-usd', 'polymath', 'lido-dao', 'enjincoin', 'fetch-ai', 'aurora-near', 
'the-open-network', 'illuvium', 'storj', 'hive', 'cartesi', 'dent', 'neo', 'xdce-crowd-sale', 
'astar', 'everscale', 'theta-token', 'holotoken', 'blockstack', 'telos', 'vechain', 'celer-network', 
'klay-token', 'woo-network', 'yearn-finance', 'ecash', 'sapphire', 'wemix-token', 'chia', 'hex', 
'rocket-pool', 'nem', 'bitdao', 'swissborg', 'mobilecoin', 'kok', 'golem', 'wazirx', 'conflux-token', 
'tether-gold', 'bitcoin-bep2', 'digitalbits', 'swissborg', 'skale', 'nervos-network']

coin_ids = ['bitcoin', 'ethereum', '0x', 'zcash', 'yearn-finance', 'uniswap', 
'uma', 'havven', 'chainlink', 'kyber-network-crystal'] 

vs_currency = 'usd'
start_date = '2021-01-01' 
end_date = '2023-11-24'
count = 0
# Open the CSV file once and write data for each coin
with open('CoinGecko.csv', 'w', newline='') as file:
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