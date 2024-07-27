import requests
import yfinance as yf
import pandas as pd
import logging

def get_nifty_200_symbols():
    try:
        df = pd.read_csv('data/ind_nifty200list.csv')
        symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()
        logging.info(f"Successfully read {len(symbols)} symbols from CSV file.")
        return symbols
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []

def fetch_market_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="6mo")
        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")

        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns in data for symbol: {symbol}")

        df = df.rename(columns={
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Volume': 'Volume'
        })
        logging.info(f"Successfully fetched data for symbol: {symbol}")
        return df

    except Exception as e:
        logging.error(f"Error fetching data for symbol {symbol}: {e}")
        return None

def save_data_to_csv(symbol, df):
    try:
        df.to_csv(f'data/{symbol}.csv')
        logging.info(f"Data for symbol {symbol} saved to CSV.")
    except Exception as e:
        logging.error(f"Error saving data for symbol {symbol} to CSV: {e}")

def fetch_corporate_actions(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
    return None