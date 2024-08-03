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


###############################################################################################
# Major Changes done to get Colour in Bullish and Bearish Trend 

# import pandas as pd
# import os
# import yaml
# from data_retrieval import fetch_market_data, save_data_to_csv, get_nifty_stock_symbols
# from technical_indicators import calculate_technical_indicators
# from analysis import rank_stocks, save_ranking_to_csv, save_ranking_to_html

# def process_file(filepath):
#     symbols = get_nifty_stock_symbols(filepath)

#     data_directory = 'data'
#     results_directory = 'results'
    
#     with open('config.yaml', 'r') as file:
#         config = yaml.safe_load(file)
#     alpha_vantage_key = config['alpha_vantage_key']
    
#     os.makedirs(data_directory, exist_ok=True)
#     os.makedirs(results_directory, exist_ok=True)

#     data = {}
#     for symbol in symbols:
#         df = fetch_market_data(symbol)
#         if df is not None:
#             save_data_to_csv(symbol, df)
#             data[symbol] = calculate_technical_indicators(df)

#     if data:
#         ranking_df = rank_stocks(data)
#         csv_path = os.path.join(results_directory, 'stock_ranking.csv')
#         html_path = os.path.join(results_directory, 'stock_ranking.html')
        
#         save_ranking_to_csv(ranking_df, csv_path)
#         save_ranking_to_html(ranking_df, html_path)
        
#         return 'stock_ranking.csv', 'stock_ranking.html'
#     else:
#         raise Exception("No data available for ranking.")


###############################################################################################
# Bullish and Bearish Trend Without Colour in HTML file 

# import pandas as pd
# import os
# import yaml
# from data_retrieval import fetch_market_data, save_data_to_csv
# from technical_indicators import calculate_technical_indicators
# from analysis import rank_stocks

# def process_file(filepath):
#     df = pd.read_csv(filepath)
#     symbols = df['Symbol'].apply(lambda x: f'{x}.NS').tolist()

#     data_directory = 'data'
#     results_directory = 'results'
    
#     with open('config.yaml', 'r') as file:
#         config = yaml.safe_load(file)
#     alpha_vantage_key = config['alpha_vantage_key']
    
#     os.makedirs(data_directory, exist_ok=True)
#     os.makedirs(results_directory, exist_ok=True)

#     data = {}
#     for symbol in symbols:
#         df = fetch_market_data(symbol)
#         if df is not None:
#             save_data_to_csv(symbol, df)
#             data[symbol] = calculate_technical_indicators(df)

#     if data:
#         ranking_df = rank_stocks(data)
#         csv_filename = 'stock_ranking.csv'
#         html_filename = 'stock_ranking.html'
#         csv_path = os.path.join(results_directory, csv_filename)
#         html_path = os.path.join(results_directory, html_filename)
#         ranking_df.to_csv(csv_path, index=False)
#         ranking_df.to_html(html_path, index=False, escape=False)
#         return csv_filename, html_filename
#     else:
#         raise Exception("No data available for ranking.")


