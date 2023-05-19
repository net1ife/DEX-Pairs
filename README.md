# Token Pairs with Highest Liquidity

This script fetches and displays the token pairs with the highest liquidity on both Uniswap and Sushiswap decentralized exchanges.

## Prerequisites

- Python 3.x
- requests library (can be installed via `pip install requests`)

## Usage

1. Clone the repository or download the `pairs.py` script.
2. Install the required dependencies by running `pip install requests` in your command-line interface.
3. Open a terminal or command prompt and navigate to the directory where the `pairs.py` script is located.
4. Run the script using the command `python pairs.py`.
5. The script will retrieve the top token pairs with the highest liquidity from both Uniswap and Sushiswap subgraphs and display the results.

## Configuration

- The number of token pairs to retrieve can be adjusted by modifying the `num_pairs` variable in the script.
- The script fetches data from the Uniswap and Sushiswap subgraphs. The subgraph URLs are pre-configured in the script.

## Output

The script will output the following information:

- For Uniswap:
  - Token pair: Token0/Token1
  - Token addresses: Token0_Address/Token1_Address
  - Liquidity in USD: $Liquidity

- For Sushiswap:
  - Token pair: Token0/Token1
  - Token addresses: Token0_Address/Token1_Address
  - Liquidity in USD: $Liquidity

If no token pairs are found for a particular exchange, a corresponding message will be displayed.

## Disclaimer

This script is provided for educational and informational purposes only. Use it at your own risk. Always exercise caution when engaging in cryptocurrency-related activities and make sure to do your own research.

