import streamlit as st
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


def format_pair(pair):
    token0_symbol = pair['token0']['symbol']
    token0_address = pair['token0']['id']
    token1_symbol = pair['token1']['symbol']
    token1_address = pair['token1']['id']
    reserve_usd = pair['reserveUSD']
    return f"Pair: {token0_symbol}/{token1_symbol}, Address: {token0_address}/{token1_address}, Liquidity: ${reserve_usd}"


# Streamlit UI
st.title('Token Pairs with Highest Liquidity')

exchange_name = st.sidebar.selectbox('Select Exchange', ['Uniswap', 'Sushiswap'])
num_pairs = st.sidebar.number_input('Number of Pairs', min_value=1, max_value=20, value=10)

if st.sidebar.button('Get Pairs'):
    if exchange_name.lower() == 'uniswap':
        pairs = get_token_pairs_with_highest_liquidity('uniswap', num_pairs)
    elif exchange_name.lower() == 'sushiswap':
        pairs = get_token_pairs_with_highest_liquidity('sushiswap', num_pairs)
    else:
        st.error('Invalid exchange name.')

    if pairs:
        st.subheader(f'{exchange_name} token pairs with highest liquidity:')
        for pair in pairs:
            st.write(format_pair(pair))
    else:
        st.warning('No token pairs found.')
