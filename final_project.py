import os
import requests
import pandas as pd
import json
from datetime import datetime
from alpaca_trade_api.rest import REST, TimeFrame

# Load API keys from environment variables
ALPACA_API_KEY = os.getenv('PKIRUMZTTO3TPTXO80XE')
ALPACA_SECRET_KEY = os.getenv('N38PJgF3Uk88RJU33kMLbCjduNWE1vT7BAKImEdy')
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

api = REST('PKIRUMZTTO3TPTXO80XE', 'N38PJgF3Uk88RJU33kMLbCjduNWE1vT7BAKImEdy', "https://paper-api.alpaca.markets")

CRYPTOCURRENCIES = ["BTC/USD", "ETH/USD", "LTC/USD", "DOGE/USD", "SOL/USD", "MATIC/USD"]

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join([c.split("/")[0].lower() for c in CRYPTOCURRENCIES]),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    prices = {}
    for pair in CRYPTOCURRENCIES:
        symbol = pair.split("/")[0].lower()
        prices[pair] = data.get(symbol, {}).get("usd", 0)
    return prices

def load_previous_prices():
    prices = {}
    try:
        files = [f for f in os.listdir("final_project/data") if f.endswith(".csv")]
        if not files:
            return prices
        latest_file = sorted(files)[-1]
        df = pd.read_csv(f"final_project/data/{latest_file}")
        for index, row in df.iterrows():
            prices[row['currency']] = row['price']
    except Exception as e:
        print(f"Error loading previous prices: {e}")
    return prices

def save_prices(prices):
    today = datetime.now().strftime("%Y-%m-%d")
    df = pd.DataFrame([{'currency': key, 'price': value} for key, value in prices.items()])
    df.to_csv(f"final_project/data/prices_{today}.csv", index=False)

def place_order(symbol, side, qty=1):
    try:
        api.submit_order(
            symbol=symbol.replace("/", ""),  # remove slash
            side=side,
            type="market",
            qty=qty,
            time_in_force="gtc"
        )
        print(f"Order placed: {side} {qty} of {symbol}")
    except Exception as e:
        print(f"Failed to place order: {e}")

def main():
    if not os.path.exists("final_project/data"):
        os.makedirs("final_project/data")

    previous_prices = load_previous_prices()
    current_prices = get_crypto_prices()

    trades = []
    for pair in CRYPTOCURRENCIES:
        prev_price = previous_prices.get(pair)
        curr_price = current_prices.get(pair)

        if prev_price:
            change_percent = (curr_price - prev_price) / prev_price * 100
            print(f"{pair}: {change_percent:.2f}% change")

            if change_percent > 5:
                place_order(pair, "buy")
                trades.append({"currency": pair, "action": "buy", "change_percent": change_percent})
            elif change_percent < -5:
                place_order(pair, "sell")
                trades.append({"currency": pair, "action": "sell", "change_percent": change_percent})

    save_prices(current_prices)

    with open("final_project/results.json", "w") as f:
        json.dump(trades, f, indent=4)

if __name__ == "__main__":
    main()




