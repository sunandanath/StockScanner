# main.py Yfinance Trand, Buy/Sell Signal

import os
import logging
import yaml
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Set up logging
logging.basicConfig(level=getattr(logging, config['log_level']), format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    data_directory = config['data_directory']
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        logging.info(f"Created '{data_directory}' directory.")

    symbols = get_nifty_200_symbols()
    if not symbols:
        logging.error("Failed to fetch Nifty 200 symbols.")
        return

    data = {}
    for symbol in symbols:
        df = fetch_market_data(symbol)
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df)

    if data:
        ranking_df = rank_stocks(data)
        save_ranking_to_csv(ranking_df)
        save_ranking_to_html(ranking_df)
        logging.info("Ranking data saved to CSV and HTML.")
    else:
        logging.error("No data available for ranking.")

if __name__ == '__main__':
    main()



""" # main.py Yfinance with logs


import os
import logging
import yaml
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Set up logging
logging.basicConfig(level=getattr(logging, config['log_level']), format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    data_directory = config['data_directory']
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        logging.info(f"Created '{data_directory}' directory.")

    symbols = get_nifty_200_symbols()
    if not symbols:
        logging.error("Failed to fetch Nifty 200 symbols.")
        return

    data = {}
    for symbol in symbols:
        df = fetch_market_data(symbol)
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df)

    if data:
        ranking_df = rank_stocks(data)
        save_ranking_to_csv(ranking_df)
        save_ranking_to_html(ranking_df)
        logging.info("Ranking data saved to CSV and HTML.")
    else:
        logging.error("No data available for ranking.")

if __name__ == '__main__':
    main()
 """


""" # main.py Yfinance

import os
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    symbols = get_nifty_200_symbols()
    if not symbols:
        print("Failed to fetch Nifty 200 symbols.")
        return

    data = {}
    for symbol in symbols:
        df = fetch_market_data(symbol)
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df)

    ranking_df = rank_stocks(data)
    save_ranking_to_csv(ranking_df)
    save_ranking_to_html(ranking_df)

if __name__ == '__main__':
    main()
 """


""" # main.py Alpha Vantage

import os
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    symbols = get_nifty_200_symbols()
    if not symbols:
        print("Failed to fetch Nifty 200 symbols.")
        return

    data = {symbol: fetch_market_data(symbol) for symbol in symbols}

    for symbol, df in data.items():
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df)
    
    ranking_df = rank_stocks(data)
    save_ranking_to_csv(ranking_df)
    save_ranking_to_html(ranking_df)

if __name__ == '__main__':
    main() """


""" # main.py

import os
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    symbols = get_nifty_200_symbols()
    if not symbols:
        print("Failed to fetch Nifty 200 symbols.")
        return

    data = {symbol: fetch_market_data(symbol) for symbol in symbols}

    for symbol, df in data.items():
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df)
    
    ranking_df = rank_stocks(data)
    save_ranking_to_csv(ranking_df)
    save_ranking_to_html(ranking_df)

if __name__ == '__main__':
    main() """


