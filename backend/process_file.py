import pandas as pd
import os
import yaml
from data_retrieval import fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

def process_file(filepath):
    df = pd.read_csv(filepath)
    symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()

    data_directory = 'data'
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    alpha_vantage_key = config['alpha_vantage_key']
    
    os.makedirs(data_directory, exist_ok=True)

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
    else:
        raise Exception("No data available for ranking.")
