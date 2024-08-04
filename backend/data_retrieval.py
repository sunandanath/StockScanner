import requests
import yfinance as yf
import pandas as pd
import logging

def get_nifty_stock_symbols(filepath):
    try:
        df = pd.read_csv(filepath)
        symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()
        logging.info(f"Successfully read {len(symbols)} symbols from CSV file.")
        return symbols
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []

def fetch_market_data(symbol, period="6mo"):
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period)
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
