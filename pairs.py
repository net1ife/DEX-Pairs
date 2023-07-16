import streamlit as st
import requests


EXCHANGE_URLS = {
    'uniswap': 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    'sushiswap': 'https://api.thegraph.com/subgraphs/name/sushiswap/exchange',
}


def get_token_pairs_with_highest_liquidity(exchange_name, num_pairs):
    # Set the exchange subgraph URL
    subgraph_url = EXCHANGE_URLS[exchange_name.lower()]

    # Query the subgraph to get token pairs sorted by liquidity
    query = f'''
        query {{
            pairs(first: {num_pairs}, orderBy: reserveUSD, orderDirection: desc) {{
                token0 {{
                    symbol
                    id
                }}
                token1 {{
                    symbol
                    id
                }}
                reserveUSD
            }}
        }}
    '''

    response = requests.post(subgraph_url, json={'query': query})
    response.raise_for_status()

    data = response.json()

    if 'data' in data:
        pairs = data['data']['pairs']
        return pairs
    else:
        return []


def format_pair(pair):
    token0_symbol = pair['token0']['symbol']
    token0_address = pair['token0']['id']
    token1_symbol = pair['token1']['symbol']
    token1_address = pair['token1']['id']
    reserve_usd = pair['reserveUSD']
    return f"Pair: {token0_symbol}/{token1_symbol}, Address: {token0_address}/{token1_address}, Liquidity: ${reserve_usd}"


def main():
    # Streamlit UI
    st.title('Token Pairs with Highest Liquidity')

    exchange_name = st.sidebar.selectbox('Select Exchange', list(EXCHANGE_URLS.keys()))
    num_pairs = st.sidebar.number_input('Number of Pairs', min_value=1, max_value=20, value=10)

    if st.sidebar.button('Get Pairs'):
        try:
            pairs = get_token_pairs_with_highest_liquidity(exchange_name, num_pairs)
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
            return

        if pairs:
            st.subheader(f'{exchange_name} token pairs with highest liquidity:')
            for pair in pairs:
                st.write(format_pair(pair))
        else:
            st.warning('No token pairs found.')


if __name__ == "__main__":
    main()
