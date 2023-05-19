import requests


def get_token_pairs_with_highest_liquidity(exchange_name, num_pairs):
    # Set the exchange subgraph URL
    if exchange_name.lower() == 'uniswap':
        subgraph_url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    elif exchange_name.lower() == 'sushiswap':
        subgraph_url = 'https://api.thegraph.com/subgraphs/name/sushiswap/exchange'

    # Query the subgraph to get token pairs sorted by liquidity
    query = '''
        query {
            pairs(first: %d, orderBy: reserveUSD, orderDirection: desc) {
                token0 {
                    symbol
                    id
                }
                token1 {
                    symbol
                    id
                }
                reserveUSD
            }
        }
    ''' % num_pairs

    response = requests.post(subgraph_url, json={'query': query})
    data = response.json()

    if 'data' in data:
        pairs = data['data']['pairs']
        return pairs
    else:
        return []


# Example usage
num_pairs = 10  # Number of token pairs to retrieve

uniswap_pairs = get_token_pairs_with_highest_liquidity('uniswap', num_pairs)
sushiswap_pairs = get_token_pairs_with_highest_liquidity(
    'sushiswap', num_pairs)


def format_pair(pair):
    token0_symbol = pair['token0']['symbol']
    token0_address = pair['token0']['id']
    token1_symbol = pair['token1']['symbol']
    token1_address = pair['token1']['id']
    reserve_usd = pair['reserveUSD']
    return f"Pair: {token0_symbol}/{token1_symbol}, Address: {token0_address}/{token1_address}, Liquidity: ${reserve_usd}"


if uniswap_pairs:
    print("Uniswap token pairs with highest liquidity:")
    for pair in uniswap_pairs:
        print(format_pair(pair))
else:
    print("No Uniswap token pairs found.")

print()

if sushiswap_pairs:
    print("Sushiswap token pairs with highest liquidity:")
    for pair in sushiswap_pairs:
        print(format_pair(pair))
else:
    print("No Sushiswap token pairs found.")
