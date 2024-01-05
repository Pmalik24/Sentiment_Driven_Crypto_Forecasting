import requests

def find_full_names(coin_symbols):
    # Define the API endpoint for CoinGecko
    coin_list_url = "https://api.coingecko.com/api/v3/coins/list"

    # Requesting the list of all coins from CoinGecko API
    response = requests.get(coin_list_url)
    all_coins = response.json()

    # Function to find the id of the cryptocurrency from its name
    def find_full_name(name, coins):
        name_lower = name.lower()  # Convert name to lowercase
        for coin in coins:
            if coin['name'].lower() == name_lower:  # Compare name
                return coin['id']
        return None

    # Creating a dictionary to map symbols to their full names
    coin_name_mapping = {name: find_full_name(name, all_coins) for name in coin_name}
    coin_list = [find_full_name(name, all_coins) for name in coin_name if find_full_name(name, all_coins) is not None]
    return coin_name_mapping, coin_list

# List of cryptocurrency symbols
coin_symbols = ['btc', 'amp', 'eth', 'stc', 'doge', 'usdt', 'link', 'usd', 'elon',
       'zrx', 'aave', 'knc', 'rly', 'joe', 'xrp', 'ada', 'dot', 'ever',
       'near', 'win', 'qtum', 'sfp', 'zec', 'dgb', 'safe', 'ltc', 'gt',
       'request', 'acm', 'ramen', 'ray', 'mask', 'binance', 'huobi',
       'trx', 'arc', 'bnt', 'belt', 'tara', 'defit', 'perp', 'etha',
       'dai', 'safemars', 'orao', 'ven', 'gusd', 'cook', 'etc', 'mana',
       'xmr', 'boson', 'cere', 'uni', 'cspr', 'rose', 'usdc', 'fine',
       'husd', 'busd', 'krypto', 'xnl', 'shib', 'wec', 'flow', 'cake',
       'latte', 'hotcross', 'cow', 'cfg', 'less', 'mkr', 'nft', 'ren',
       'safebtc', 'chz', 'sol', 'itgr', 'algo', 'bzz', 'hmt', 'audio',
       'metis', 'metisdao', 'rune', 'sushi', 'sand', 'gala', 'ygg', 'bnb',
       'bsv', 'palg', 'dydx', 'matic', 'avax', 'poly', 'coin98', 'iotx',
       'tup', 'sc', '1inch', 'serum', 'waxp', 'ftm', 'spell', 'mpt',
       'luna', 'usdp', 'dmz', 'ar', 'egld', 'icp', 'forex', 'hbar', 'okb',
       'celo', 'ont', 'atom', 'omg', 'boba', 'c98', 'raca', 'shiba',
       'movr', 'harmony', 'zil', 'cvx', 'crv', 'dana', 'tribe', 'cosmos',
       'tex', 'yin', 'thorchain', 'gog', 'hnt', 'lrc', 'pyr', 'arrr',
       'rndr', 'symbol', 'zen', 'vlx', 'uos', 'kda', 'cro', 'sandbox',
       'ust', 'sys', 'kucoin', 'fil', 'ocean', 'ksm', 'sxp', 'bch', 'btt',
       'scrt', 'secret', 'anyswap', 'glmr', 'tlos', 'klaytn', 'cel',
       'dash', 'osmo', 'horizen', 'fx', 'srm', 'fxs', 'frax', 'usdn',
       'alice', 'hedera', 'tusd', 'ant', 'paxg', 'nexo', 'ceek', 'xlm',
       'gno', 'lpt', 'bat', 'safemoon', 'quant', 'kava', 'wbtc', 'snx',
       'steth', 'filecoin', 'livepeer', 'comp', 'rvn', 'ecash', 'coti',
       'ultra', 'inj', 'mina', 'xtz', 'qnt', 'syscoin', 'icx', 'lusd',
       'polymath', 'ldo', 'ftt', 'enj', 'twt', 'fet', 'aurora', 'toncoin',
       'ilv', 'storj', 'hive', 'ctsi', 'dent', 'neo', 'xdc', 'astar',
       'everscale', 'ankr', 'theta', 'hot', 'stx', 'telos', 'vet', 'celr',
       'klay', 'woo', 'yfi', 'xec', 'nft1', 'sapphire', 'wemix', 'xch',
       'hex', 'rpl', 'xem', 'bitdao', 'chsb', 'mob', 'kok', 'glm', 'wrx',
       'eos', 'uma', 'fei', 'conflux', 'xaut', 'leo', 'btcb', 'skl',
       'xdb', 'ckb', 'digitalbits', 'swissborg', 'audius', 'xyo',
       'loopring', 'mxc', 'vgx', 'powr', 'omi', 'flux', 'persistence',
       'deso', 'golem', 'dcr']
coin_name = [
    "bitcoin", "amp", "ethereum", "student coin", "dogecoin", "tether", "chainlink",
    "united states dollar", "dogelon mars", "0x", "aave", "kyber network crystal",
    "rally", "joe", "xrp", "cardano", "polkadot", "everscale", "near protocol",
    "wink", "qtum", "safepal", "zcash", "digibyte", "safecoin", "litecoin",
    "gatetoken", "request", "ac milan fan token", "ramenswap", "raydium",
    "mask network", "binance coin", "huobi token", "tron", "arcblock",
    "bancor network token", "belt finance", "taracoin", "digital fitness",
    "perpetual protocol", "etha lend", "dai", "safemars", "orao network",
    "vechain", "gemini dollar", "cook protocol", "ethereum classic",
    "decentraland", "monero", "boson protocol", "cere network", "uniswap",
    "casper network", "oasis network", "usd coin", "refinable", "husd",
    "binance usd", "krypto", "chronicle", "shiba inu", "wechain coin", "flow",
    "pancakeswap", "latteswap", "hot cross", "cow protocol", "centrifuge",
    "less network", "maker", "apenft", "ren", "safebtc", "chiliz", "solana",
    "integraded", "algorand", "swarm", "human protocol", "audius", "metis",
    "metisdao", "thorchain", "sushiswap", "the sandbox", "gala", "yield guild games",
    "bitcoin sv", "palgold", "dydx", "polygon", "avalanche", "polymath", "coin98",
    "iotex", "tenup", "siacoin", "1inch network", "serum", "wax", "fantom",
    "spell token", "metal packaging token", "terra", "pax dollar", "demole",
    "arweave", "elrond", "internet computer", "handle.forex", "hedera hashgraph",
    "okb", "celo", "ontology", "cosmos", "omg network", "boba network", "coin98",
    "radio caca", "shiba inu", "moonriver", "harmony", "zilliqa", "convex finance",
    "curve dao token", "danaos", "tribe", "cosmos", "texochat", "yin finance",
    "thorchain", "guild of guardians", "helium", "loopring", "vulcan forged pyr",
    "pirate chain", "render token", "symbol", "horizen", "velas", "ultra", "kadena",
    "crypto.com coin", "the sandbox", "terrausd", "syscoin", "kucoin token",
    "filecoin", "ocean protocol", "kusama", "swipe", "bitcoin cash", "bittorrent",
    "secret", "multichain", "moonbeam", "telos", "klaytn", "celsius", "dash",
    "osmosis", "horizen", "function x", "serum", "frax share", "frax", "neutrino usd",
    "my neighbor alice", "hedera hashgraph", "trueusd", "aragon", "pax gold", "nexo",
    "ceek vr", "stellar", "gnosis", "livepeer", "basic attention token", "safemoon",
    "quant", "kava", "wrapped bitcoin", "synthetix", "lido staked eth", "filecoin",
    "livepeer", "compound", "ravencoin", "ecash", "coti", "ultra", "injective protocol",
    "mina", "tezos", "quant", "syscoin", "icon", "liquity usd", "polymath", "lido dao",
    "ftx token", "enjin coin", "trust wallet token", "fetch.ai", "aurora", "toncoin",
    "illuvium", "storj", "hive", "cartesi", "dent", "neo", "xdc network", "astar",
    "everscale", "ankr", "theta network", "holo", "stacks", "telos", "vechain", 
    "celer network", "klaytn", "woo network", "yearn.finance", "ecash", "sapphire",  # Both NFT1 and SAPPHIRE map to Sapphire
    "wemix", "chia", "hex", "rocket pool", "nem", "bitdao", "swissborg", "mobilecoin", 
    "kok", "golem", "wazirx", "electro-optical system", "universal market access", 
    "fei protocol", "conflux", "tether gold", "unus sed leo", "bitcoin bep2", 
    'digitalbits', 'swissborg', 'skale', 'xdb chain', 'nervos network'
    ]

coin_name_mapping, coin_list = find_full_names(coin_symbols)
print(coin_name_mapping)