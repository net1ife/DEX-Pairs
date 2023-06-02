# Token Pairs with Highest Liquidity

This is a simple Streamlit app that retrieves and displays token pairs with the highest liquidity from Uniswap or Sushiswap exchanges. It uses the subgraph APIs provided by Uniswap and Sushiswap to fetch the data.

## Requirements

- Python 3.6+
- Streamlit
- Requests

## Installation

1. Clone the repository or download the files.
2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app using the following command:

```
streamlit run pairs.py
```

2. The app will start and open in your default web browser.
3. Use the sidebar to select the exchange (Uniswap or Sushiswap) and specify the number of pairs to retrieve.
4. Click the "Get Pairs" button to fetch and display the token pairs with the highest liquidity.
5. The app will show the pairs along with their symbols, addresses, and liquidity.

## Notes

- The app relies on the subgraph APIs provided by Uniswap and Sushiswap, so it requires an internet connection to fetch the data.
- The number of pairs to retrieve can be set between 1 and 20.
- If no token pairs are found for the selected exchange, a warning message will be displayed.
