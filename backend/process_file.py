import pandas as pd
import os
import yaml
from data_retrieval import fetch_market_data, save_data_to_csv
from technical_indicators import calculate_technical_indicators
from analysis import rank_stocks

def process_file(filepath):
    df = pd.read_csv(filepath)
    symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()

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
            data[symbol] = calculate_technical_indicators(df)

    if data:
        ranking_df = rank_stocks(data)
        csv_filename = 'stock_ranking.csv'
        html_filename = 'stock_ranking.html'
        csv_path = os.path.join(results_directory, csv_filename)
        html_path = os.path.join(results_directory, html_filename)
        ranking_df.to_csv(csv_path, index=False)
        ranking_df.to_html(html_path, index=False, escape=False)
        return csv_filename, html_filename
    else:
        raise Exception("No data available for ranking.")


