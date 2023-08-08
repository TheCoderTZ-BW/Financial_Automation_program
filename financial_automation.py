import requests
import pandas as pd

# Set your API key and endpoint
api_key = 'YOUR_API_KEY'
base_url = f'https://www.alphavantage.co/query'

# List of stock symbols in your portfolio
portfolio = ['AAPL', 'MSFT', 'GOOGL']

# Retrieve stock prices
def get_stock_prices(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()['Time Series (Daily)']
    df = pd.DataFrame(data).transpose()
    df['date'] = pd.to_datetime(df.index)
    df['close'] = df['4. close'].astype(float)
    return df[['date', 'close']]

# Calculate portfolio performance
def calculate_portfolio_performance():
    portfolio_data = {}
    for symbol in portfolio:
        stock_prices = get_stock_prices(symbol)
        latest_price = stock_prices.iloc[0]['close']
        portfolio_data[symbol] = {
            'latest_price': latest_price,
            # Additional calculations can be added here
        }
    return portfolio_data

# Generate a simple report
def generate_report():
    portfolio_performance = calculate_portfolio_performance()
    for symbol, data in portfolio_performance.items():
        print(f"Symbol: {symbol}")
        print(f"Latest Price: {data['latest_price']}")
        print("-" * 20)

if __name__ == '__main__':
    generate_report()
