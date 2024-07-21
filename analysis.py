# analysis.py Yfinance with sentiment analysis


import pandas as pd
from technical_indicators import determine_trend
from news_sentiment import get_news_sentiment
from data_retrieval import fetch_corporate_actions

def rank_stocks(data, news_api_key, alpha_vantage_key):
    ranking = []

    for symbol, df in data.items():
        if df is not None and not df.empty:
            latest_close = df['Close'].iloc[-1]
            upper_band = df['Upper Band'].iloc[-1]
            lower_band = df['Lower Band'].iloc[-1]
            distance_to_support = latest_close - lower_band
            distance_to_resistance = upper_band - latest_close
            trend = determine_trend(df)
            sentiment = get_news_sentiment(symbol, news_api_key)
            corporate_actions = fetch_corporate_actions(symbol, alpha_vantage_key)

            # Calculate signal strength: closer to support is a stronger buy signal,
            # closer to resistance is a stronger sell signal
            signal_strength = (upper_band - lower_band) / 2 - abs(latest_close - (upper_band + lower_band) / 2)

            ranking.append({
                'Symbol': symbol,
                'Close': latest_close,
                'Distance to Support': distance_to_support,
                'Distance to Resistance': distance_to_resistance,
                'Support Price': lower_band,
                'Resistance Price': upper_band,
                'Signal Strength': signal_strength,
                'Trend': trend,
                'Positive Sentiment': sentiment['positive'],
                'Neutral Sentiment': sentiment['neutral'],
                'Negative Sentiment': sentiment['negative'],
                'Corporate Actions': corporate_actions
            })
    
    ranking_df = pd.DataFrame(ranking)
    ranking_df = ranking_df.sort_values(by=['Distance to Support', 'Distance to Resistance'], ascending=[True, False])
    return ranking_df

def save_ranking_to_csv(ranking_df):
    ranking_df.to_csv('stock_ranking.csv', index=False)

def save_ranking_to_html(ranking_df):
    def colorize_trend(trend):
        if trend == 'Bullish':
            return f'<span style="color: green;">{trend}</span>'
        elif trend == 'Bearish':
            return f'<span style="color: red;">{trend}</span>'
        else:
            return trend

    ranking_df['Trend'] = ranking_df['Trend'].apply(colorize_trend)
    ranking_df.to_html('stock_ranking.html', index=False, escape=False)


# analysis.py Yfinance with logs

# import pandas as pd
# from technical_indicators import determine_trend

# def rank_stocks(data):
#     """
#     Rank stocks based on their proximity to support and resistance levels and determine trend.
    
#     Args:
#         data (dict): Dictionary where keys are stock symbols and values are DataFrames with stock data.
    
#     Returns:
#         pd.DataFrame: DataFrame with stocks ranked by their proximity to support and resistance levels.
#     """
#     ranking = []

#     for symbol, df in data.items():
#         if df is not None and not df.empty:
#             latest_close = df['Close'].iloc[-1]
#             upper_band = df['Upper Band'].iloc[-1]
#             lower_band = df['Lower Band'].iloc[-1]
#             distance_to_support = latest_close - lower_band
#             distance_to_resistance = upper_band - latest_close
#             trend = determine_trend(df)

#             # Calculate signal strength: closer to support is a stronger buy signal,
#             # closer to resistance is a stronger sell signal
#             signal_strength = (upper_band - lower_band) / 2 - abs(latest_close - (upper_band + lower_band) / 2)

#             ranking.append({
#                 'Symbol': symbol,
#                 'Close': latest_close,
#                 'Distance to Support': distance_to_support,
#                 'Distance to Resistance': distance_to_resistance,
#                 'Support Price': lower_band,
#                 'Resistance Price': upper_band,
#                 'Signal Strength': signal_strength,
#                 'Trend': trend
#             })
    
#     ranking_df = pd.DataFrame(ranking)
#     # Sort by distance to support (ascending), then by distance to resistance (descending)
#     ranking_df = ranking_df.sort_values(by=['Distance to Support', 'Distance to Resistance'], ascending=[True, False])
#     return ranking_df

# def save_ranking_to_csv(ranking_df):
#     """
#     Save the ranking DataFrame to a CSV file.
    
#     Args:
#         ranking_df (pd.DataFrame): DataFrame with ranked stocks.
#     """
#     ranking_df.to_csv('stock_ranking.csv', index=False)

# def save_ranking_to_html(ranking_df):
#     """
#     Save the ranking DataFrame to an HTML file.
    
#     Args:
#         ranking_df (pd.DataFrame): DataFrame with ranked stocks.
#     """
#     # Apply CSS styling for bullish (green) and bearish (red) trends
#     def colorize_trend(trend):
#         if trend == 'Bullish':
#             return f'<span style="color: green;">{trend}</span>'
#         elif trend == 'Bearish':
#             return f'<span style="color: red;">{trend}</span>'
#         else:
#             return trend

#     ranking_df['Trend'] = ranking_df['Trend'].apply(colorize_trend)
#     ranking_df.to_html('stock_ranking.html', index=False, escape=False)


###############################################################################################################################
# # analysis.py Yfinance with right Ranking/Sorting

# import pandas as pd

# def rank_stocks(data):
#     '''
#     Rank stocks based on their proximity to support and resistance levels.
    
#     Args:
#         data (dict): Dictionary where keys are stock symbols and values are DataFrames with stock data.
    
#     Returns:
#         pd.DataFrame: DataFrame with stocks ranked by their proximity to support and resistance levels.
#     '''
#     ranking = []

#     for symbol, df in data.items():
#         if df is not None and not df.empty:
#             latest_close = df['Close'].iloc[-1]
#             upper_band = df['Upper Band'].iloc[-1]
#             lower_band = df['Lower Band'].iloc[-1]
#             distance_to_support = latest_close - lower_band
#             distance_to_resistance = upper_band - latest_close

#             # Calculate signal strength: closer to support is a stronger buy signal,
#             # closer to resistance is a stronger sell signal
#             signal_strength = (upper_band - lower_band) / 2 - abs(latest_close - (upper_band + lower_band) / 2)

#             ranking.append({
#                 'Symbol': symbol,
#                 'Close': latest_close,
#                 'Distance to Support': distance_to_support,
#                 'Distance to Resistance': distance_to_resistance,
#                 'Signal Strength': signal_strength
#             })
    
#     ranking_df = pd.DataFrame(ranking)
#     # Sort by signal strength: stocks closest to support (strongest buy signals) appear first
#     ranking_df = ranking_df.sort_values(by='Signal Strength', ascending=False)
#     return ranking_df

# def save_ranking_to_csv(ranking_df):
#     """
#     Save the ranking DataFrame to a CSV file.
    
#     Args:
#         ranking_df (pd.DataFrame): DataFrame with ranked stocks.
#     """
#     ranking_df.to_csv('stock_ranking.csv', index=False)

# def save_ranking_to_html(ranking_df):
#     """
#     Save the ranking DataFrame to an HTML file.
    
#     Args:
#         ranking_df (pd.DataFrame): DataFrame with ranked stocks.
#     """
#     ranking_df.to_html('stock_ranking.html', index=False)

##################################################################################################
""" # analysis.py Yfinance

import pandas as pd

def rank_stocks(data):
    ranking = []

    for symbol, df in data.items():
        if df is not None and not df.empty:
            latest_close = df['Close'].iloc[-1]
            upper_band = df['Upper Band'].iloc[-1]
            lower_band = df['Lower Band'].iloc[-1]
            distance_to_support = latest_close - lower_band
            distance_to_resistance = upper_band - latest_close

            ranking.append({
                'Symbol': symbol,
                'Close': latest_close,
                'Distance to Support': distance_to_support,
                'Distance to Resistance': distance_to_resistance
            })
    
    ranking_df = pd.DataFrame(ranking)
    ranking_df = ranking_df.sort_values(by=['Distance to Support', 'Distance to Resistance'])
    return ranking_df

def save_ranking_to_csv(ranking_df):
    ranking_df.to_csv('stock_ranking.csv', index=False)

def save_ranking_to_html(ranking_df):
    ranking_df.to_html('stock_ranking.html', index=False) """



""" # analysis.py Alpha Vantage

import pandas as pd


def rank_stocks(data):
    ranking = []

    for symbol, df in data.items():
        if df is not None:
            latest_close = df['Close'].iloc[-1]
            upper_band = df['Upper Band'].iloc[-1]
            lower_band = df['Lower Band'].iloc[-1]
            distance_to_support = latest_close - lower_band
            distance_to_resistance = upper_band - latest_close

            ranking.append({
                'Symbol': symbol,
                'Close': latest_close,
                'Distance to Support': distance_to_support,
                'Distance to Resistance': distance_to_resistance
            })

    ranking_df = pd.DataFrame(ranking)
    ranking_df = ranking_df.sort_values(
        by=['Distance to Support', 'Distance to Resistance'])
    return ranking_df


def save_ranking_to_csv(ranking_df):
    ranking_df.to_csv('stock_ranking.csv', index=False)


def save_ranking_to_html(ranking_df):
    ranking_df.to_html('stock_ranking.html', index=False) """
