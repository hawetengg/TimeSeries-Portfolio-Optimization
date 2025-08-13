import yfinance as yf
import pandas as pd
from datetime import datetime

# Define assets and date range
assets = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = '2025-07-31'

# Fetch data
data = {}
for asset in assets:
    data[asset] = yf.download(asset, start=start_date, end=end_date, auto_adjust=False)
    data[asset].to_csv(f'data/{asset}_historical.csv')
    print(f"Data for {asset} saved to data/{asset}_historical.csv")

# Merge into a single DataFrame for convenience (optional)
merged = pd.concat([data[asset]['Adj Close'].rename(columns={'Adj Close': asset}) for asset in assets], axis=1)
merged.to_csv('data/merged_adj_close.csv')