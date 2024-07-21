# data_retrieval.py yfinance with logs

import yfinance as yf
import pandas as pd
import logging
from datetime import datetime, timedelta

def get_nifty_200_symbols():
    """
    Reads the Nifty 200 symbols from a CSV file and formats them for Yahoo Finance.

    Returns:
        list: A list of formatted stock symbols.
    """
    try:
        df = pd.read_csv('data/ind_nifty200list.csv')
        symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()
        logging.info(f"Successfully read {len(symbols)} symbols from CSV file.")
        return symbols
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []

def fetch_market_data(symbol):
    """
    Fetches market data for a given symbol using yfinance.

    Args:
        symbol (str): The stock symbol to fetch data for.

    Returns:
        pd.DataFrame: DataFrame containing the market data, or None if an error occurs.
    """
    try:
        ticker = yf.Ticker(symbol)
        
        # Calculate the date 6 months ago from today
        end_date = datetime.today().date()
        start_date = end_date - timedelta(days=6*30)  # Roughly 6 months
        
        df = ticker.history(start=start_date, end=end_date)  # Use start and end dates for 6 months data
        
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
    """
    Saves the DataFrame to a CSV file.

    Args:
        symbol (str): The stock symbol to name the file.
        df (pd.DataFrame): The DataFrame to save.
    """
    try:
        df.to_csv(f'data/{symbol}.csv')
        logging.info(f"Data for symbol {symbol} saved to CSV.")
    except Exception as e:
        logging.error(f"Error saving data for symbol {symbol} to CSV: {e}")


""" # data_retrieval.py Yfinance

# import requests
import yfinance as yf
import pandas as pd

def get_nifty_200_symbols():
    try:
        df = pd.read_csv('data/ind_nifty200list.csv')
        symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()
        return symbols
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


# def get_nifty_200_symbols():
#     url = 'https://nsearchives.nseindia.com/content/indices/ind_nifty200list.csv'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         df = pd.read_csv(pd.compat.StringIO(response.text))
#         symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()
#         return symbols
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching Nifty 200 symbols: {e}")
#         return []

def fetch_market_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="1mo")  # Use '1mo' period for initial data retrieval
        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")
        df = df.rename(columns={
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Volume': 'Volume'
        })
        return df

    except Exception as e:
        print(f"Error fetching data for symbol {symbol}: {e}")
        return None

def save_data_to_csv(symbol, df):
    df.to_csv(f'data/{symbol}.csv')

 """




