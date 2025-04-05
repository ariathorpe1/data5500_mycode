import requests
import networkx as nx
from itertools import permutations

# CoinGecko API configuration
coin_ids = ['ethereum', 'bitcoin', 'litecoin', 'ripple', 'cardano', 'bitcoin-cash', 'eos']
tickers = ['eth', 'btc', 'ltc', 'xrp', 'ada', 'bch', 'eos']
id_to_ticker = dict(zip(coin_ids, tickers))

# Get live prices from CoinGecko API
def fetch_exchange_rates():
    ids = ','.join(coin_ids)
    vs_currencies = ','.join(tickers)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currencies}"
    response = requests.get(url)
    return response.json()

# Create graph from exchange data
def build_graph(data):
    g = nx.DiGraph()
    for coin in coin_ids:
        from_currency = id_to_ticker[coin]
        for to_currency in tickers:
            if to_currency in data[coin]:
                weight = data[coin][to_currency]
                if weight > 0:
                    g.add_edge(from_currency, to_currency, weight=weight)
    return g

# Calculate total weight of a path
def calculate_path_weight(g, path):
    weight = 1.0
    for i in range(len(path) - 1):
        weight *= g[path[i]][path[i+1]]['weight']
    return weight

# logic
def find_arbitrage_opportunities(graph):
    max_factor = 0
    min_factor = float('inf')
    max_details = ()
    min_details = ()

    for src, dst in permutations(graph.nodes, 2):
        forward_paths = list(nx.all_simple_paths(graph, src, dst))
        reverse_paths = list(nx.all_simple_paths(graph, dst, src))

        for f_path in forward_paths:
            forward_weight = calculate_path_weight(graph, f_path)

            for r_path in reverse_paths:
                reverse_weight = calculate_path_weight(graph, r_path)
                factor = forward_weight * reverse_weight

                # Print each set of paths
                print(f"\nPaths from {src} to {dst} -------------------------")
                print(f"{f_path} {forward_weight}")
                print(f"{r_path} {reverse_weight}")
                print(f"Factor: {factor}")

                # Track max/min dis-equilibrium factors
                if factor > max_factor:
                    max_factor = factor
                    max_details = (f_path, r_path, forward_weight, reverse_weight)
                if factor < min_factor:
                    min_factor = factor
                    min_details = (f_path, r_path, forward_weight, reverse_weight)

    # Final summary
    print("\n\n======== Arbitrage Summary ========")
    print("\nMax arbitrage opportunity:")
    print(f"Forward path: {max_details[0]} Weight: {max_details[2]}")
    print(f"Reverse path: {max_details[1]} Weight: {max_details[3]}")
    print(f"Factor: {max_factor}")

    print("\nMin arbitrage opportunity:")
    print(f"Forward path: {min_details[0]} Weight: {min_details[2]}")
    print(f"Reverse path: {min_details[1]} Weight: {min_details[3]}")
    print(f"Factor: {min_factor}")
    print("====================================")

# Run the program
def main():
    print("Fetching exchange rates from CoinGecko...")
    data = fetch_exchange_rates()
    print("Building graph...")
    graph = build_graph(data)
    print("Searching for arbitrage opportunities...")
    find_arbitrage_opportunities(graph)

if __name__ == "__main__":
    main()
