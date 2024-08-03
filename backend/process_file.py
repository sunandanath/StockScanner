import pandas as pd
import os
import yaml
from data_retrieval import fetch_market_data, save_data_to_csv, get_nifty_stock_symbols
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

def process_file(filepath, ma_period1, ma_period2):
    symbols = get_nifty_stock_symbols(filepath)

    data_directory = 'data'
    results_directory = 'results'
    
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    alpha_vantage_key = config['alpha_vantage_key']
    
    os.makedirs(data_directory, exist_ok=True)
    os.makedirs(results_directory, exist_ok=True)

    data = {}
    for symbol in symbols:
        df = fetch_market_data(symbol)
        if df is not None:
            save_data_to_csv(symbol, df)
            data[symbol] = calculate_technical_indicators(df, ma_period1, ma_period2)

    if data:
        ranking_df = rank_stocks(data)
        csv_path = os.path.join(results_directory, 'stock_ranking.csv')
        html_path = os.path.join(results_directory, 'stock_ranking.html')
        
        save_ranking_to_csv(ranking_df, csv_path)
        save_ranking_to_html(ranking_df, html_path)
        
        return 'stock_ranking.csv', 'stock_ranking.html'
    else:
        raise Exception("No data available for ranking.")


