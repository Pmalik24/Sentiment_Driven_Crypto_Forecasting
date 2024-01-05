const axios = require('axios');
const fs = require('fs');

// Function to add months to a date
function addMonths(date, months) {
    const d = new Date(date);
    d.setMonth(d.getMonth() + months);
    return d;
}

// List of product IDs you want to retrieve data for
const productIds = [
    'BTC-USD', 'AMP-USD', 'ETH-USD', 'STC-USD', 'DOGE-USD', 
    'USDT-USD', 'LINK-USD', 'USD-USD', 'ELON-USD', 'ZRX-USD', 
    'AAVE-USD', 'KNC-USD', 'RLY-USD', 'JOE-USD', 'XRP-USD', 
    'ADA-USD', 'DOT-USD', 'EVER-USD', 'NEAR-USD', 'WIN-USD', 
    'QTUM-USD', 'SFP-USD', 'ZEC-USD', 'DGB-USD', 'SAFE-USD', 
    'LTC-USD', 'GT-USD', 'REQUEST-USD', 'ACM-USD', 'RAMEN-USD', 
    'RAY-USD', 'MASK-USD', 'BINANCE-USD', 'HUOBI-USD', 'TRX-USD', 
    'ARC-USD', 'BNT-USD', 'BELT-USD', 'TARA-USD', 'DEFIT-USD', 
    'PERP-USD', 'ETHA-USD', 'DAI-USD', 'SAFEMARS-USD', 'ORAO-USD', 
    'VEN-USD', 'GUSD-USD', 'COOK-USD', 'ETC-USD', 'MANA-USD', 
    'XMR-USD', 'BOSON-USD', 'CERE-USD', 'UNI-USD', 'CSPR-USD', 
    'ROSE-USD', 'USDC-USD', 'FINE-USD', 'HUSD-USD', 'BUSD-USD', 
    'KRYPTO-USD', 'XNL-USD', 'SHIB-USD', 'WEC-USD', 'FLOW-USD', 
    'CAKE-USD', 'LATTE-USD', 'HOTCROSS-USD', 'COW-USD', 'CFG-USD', 
    'LESS-USD', 'MKR-USD', 'NFT-USD', 'REN-USD', 'SAFEBTC-USD', 
    'CHZ-USD', 'SOL-USD', 'ITGR-USD', 'ALGO-USD', 'BZZ-USD', 
    'HMT-USD', 'AUDIO-USD', 'METIS-USD', 'METISDAO-USD', 'RUNE-USD', 
    'SUSHI-USD', 'SAND-USD', 'GALA-USD', 'YGG-USD', 'BNB-USD', 
    'BSV-USD', 'PALG-USD', 'DYDX-USD', 'MATIC-USD', 'AVAX-USD', 
    'POLY-USD', 'COIN98-USD', 'IOTX-USD', 'TUP-USD', 'SC-USD', 
    '1INCH-USD', 'SERUM-USD', 'WAXP-USD', 'FTM-USD', 'SPELL-USD', 
    'MPT-USD', 'LUNA-USD', 'USDP-USD', 'DMZ-USD', 'AR-USD', 
    'EGLD-USD', 'ICP-USD', 'FOREX-USD', 'HBAR-USD', 'OKB-USD', 
    'CELO-USD', 'ONT-USD', 'ATOM-USD', 'OMG-USD', 'BOBA-USD', 
    'C98-USD', 'RACA-USD', 'SHIBA-USD', 'MOVR-USD', 'HARMONY-USD', 
    'ZIL-USD', 'CVX-USD', 'CRV-USD', 'DANA-USD', 'TRIBE-USD', 
    'COSMOS-USD', 'TEX-USD', 'YIN-USD', 'THORCHAIN-USD', 'GOG-USD', 
    'HNT-USD', 'LRC-USD', 'PYR-USD', 'ARRR-USD', 'RNDR-USD', 
    'SYMBOL-USD', 'ZEN-USD', 'VLX-USD', 'UOS-USD', 'KDA-USD', 
    'CRO-USD', 'SANDBOX-USD', 'UST-USD', 'SYS-USD', 'KUCOIN-USD', 
    'FIL-USD', 'OCEAN-USD', 'KSM-USD', 'SXP-USD', 'BCH-USD', 
    'BTT-USD', 'SCRT-USD', 'SECRET-USD', 'ANYSWAP-USD', 'GLMR-USD', 
    'TLOS-USD', 'KLAYTN-USD', 'CEL-USD', 'DASH-USD', 'OSMO-USD', 
    'HORIZEN-USD', 'FX-USD', 'SRM-USD', 'FXS-USD', 'FRAX-USD', 
    'USDN-USD', 'ALICE-USD', 'HEDERA-USD', 'TUSD-USD', 'ANT-USD', 
    'PAXG-USD', 'NEXO-USD', 'CEEK-USD', 'XLM-USD', 'GNO-USD', 
    'LPT-USD', 'BAT-USD', 'SAFEMOON-USD', 'QUANT-USD', 'KAVA-USD', 
    'WBTC-USD', 'SNX-USD', 'STETH-USD', 'FILECOIN-USD', 'LIVEPEER-USD', 
    'COMP-USD', 'RVN-USD', 'ECASH-USD', 'COTI-USD', 'ULTRA-USD', 
    'INJ-USD', 'MINA-USD', 'XTZ-USD', 'QNT-USD', 'SYSCOIN-USD', 
    'ICX-USD', 'LUSD-USD', 'POLYMATH-USD', 'LDO-USD', 'FTT-USD', 
    'ENJ-USD', 'TWT-USD', 'FET-USD', 'AURORA-USD', 'TONCOIN-USD', 
    'ILV-USD', 'STORJ-USD', 'HIVE-USD', 'CTSI-USD', 'DENT-USD', 
    'NEO-USD', 'XDC-USD', 'ASTAR-USD', 'EVERSCALE-USD', 'ANKR-USD', 
    'THETA-USD', 'HOT-USD', 'STX-USD', 'TELOS-USD', 'VET-USD', 
    'CELR-USD', 'KLAY-USD', 'WOO-USD', 'YFI-USD', 'XEC-USD', 
    'NFT1-USD', 'SAPPHIRE-USD', 'WEMIX-USD', 'XCH-USD', 'HEX-USD', 
    'RPL-USD', 'XEM-USD', 'BITDAO-USD', 'CHSB-USD', 'MOB-USD', 
    'KOK-USD', 'GLM-USD', 'WRX-USD', 'EOS-USD', 'UMA-USD', 
    'FEI-USD', 'CONFLUX-USD', 'XAUT-USD', 'LEO-USD', 'BTCB-USD', 
    'SKL-USD', 'XDB-USD', 'CKB-USD', 'DIGITALBITS-USD', 'SWISSBORG-USD', 
    'AUDIUS-USD', 'XYO-USD', 'LOOPRING-USD', 'MXC-USD', 'VGX-USD', 
    'POWR-USD', 'OMI-USD', 'FLUX-USD', 'PERSISTENCE-USD', 'DESO-USD', 
    'GOLEM-USD', 'DCR-USD'
]; // Add more product IDs as needed

// Define the start and end dates for the entire range
const overallStartDate = new Date('2021-01-01T00:00:00.000Z');
const overallEndDate = new Date('2023-11-23T00:00:00.000Z');

// Write the CSV header to the file
fs.writeFileSync('coinbase.csv', 'product_id,timestamp,low,high,open,close,volume\n', 'utf8');

// Function to fetch and process data for a given product ID
async function fetchDataForProduct(productId) {
    let startDate = overallStartDate;
    let endDate = addMonths(startDate, 6);

    while (startDate < overallEndDate) {
        // Log the current date range being processed
        console.log(`Fetching data for ${productId}: Start Date - ${startDate.toISOString()}, End Date - ${endDate.toISOString()}`);

        let config = {
            method: 'get',
            url: `https://api.exchange.coinbase.com/products/${productId}/candles?start=${startDate.toISOString()}&end=${endDate.toISOString()}&granularity=86400`,
            headers: {
                'Content-Type': 'application/json'
            }
        };

        await axios(config)
            .then((response) => {
                const data = response.data;

                // Append data to a string to be written to the file
                let dataString = '';
                data.forEach(row => {
                    dataString += `${productId},${row.join(',')}\n`;
                });

                // Append the data string to the file
                fs.appendFileSync('coinbase.csv', dataString, 'utf8');
            })
            .catch((error) => {
                console.log(`Error fetching data for ${productId} starting ${startDate.toISOString()}: ${error}`);
            });

        // Move to the next period
        startDate = endDate;
        endDate = addMonths(startDate, 6);
        if (endDate > overallEndDate) {
            endDate = overallEndDate;
        }
    }
}

// Main function to loop over product IDs and fetch data
async function main() {
    for (const productId of productIds) {
        await fetchDataForProduct(productId);
    }

    console.log("Data fetching complete.");
}

// Run the main function
main();

