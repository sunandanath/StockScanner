import pandas as pd
from technical_indicators import determine_trend

def rank_stocks(data):
    """
    Rank stocks based on their proximity to support and resistance levels and determine trend.
    
    Args:
        data (dict): Dictionary where keys are stock symbols and values are DataFrames with stock data.
    
    Returns:
        pd.DataFrame: DataFrame with stocks ranked by their proximity to support and resistance levels.
    """
    ranking = []

    for symbol, df in data.items():
        if df is not None and not df.empty:
            latest_close = df['Close'].iloc[-1]
            upper_band = df['Upper Band'].iloc[-1]
            lower_band = df['Lower Band'].iloc[-1]
            distance_to_support_pct = ((latest_close - lower_band) / lower_band) * 100
            distance_to_resistance_pct = ((upper_band - latest_close) / upper_band) * 100
            trend = determine_trend(df)

            # Calculate signal strength: closer to support is a stronger buy signal,
            # closer to resistance is a stronger sell signal
            signal_strength = (upper_band - lower_band) / 2 - abs(latest_close - (upper_band + lower_band) / 2)

            ranking.append({
                'Symbol': symbol,
                'Close': latest_close,
                'Distance to Support (%)': distance_to_support_pct,
                'Distance to Resistance (%)': distance_to_resistance_pct,
                'Support Price': lower_band,
                'Resistance Price': upper_band,
                'Signal Strength': signal_strength,
                'Trend': trend
            })
    
    ranking_df = pd.DataFrame(ranking)
    # Sort by distance to support (ascending), then by distance to resistance (descending)
    ranking_df = ranking_df.sort_values(by=['Distance to Support (%)', 'Distance to Resistance (%)'], ascending=[True, False])
    return ranking_df

def save_ranking_to_csv(ranking_df, filepath):
    """
    Save the ranking DataFrame to a CSV file.
    
    Args:
        ranking_df (pd.DataFrame): DataFrame with ranked stocks.
        filepath (str): The path where the CSV file will be saved.
    """
    ranking_df.to_csv(filepath, index=False)

def save_ranking_to_html(ranking_df, filepath):
    """
    Save the ranking DataFrame to an HTML file.
    
    Args:
        ranking_df (pd.DataFrame): DataFrame with ranked stocks.
        filepath (str): The path where the HTML file will be saved.
    """
    # Apply CSS styling for bullish (green) and bearish (red) trends
    def colorize_trend(trend):
        if trend == 'Bullish':
            return f'<span style="color: green;">{trend}</span>'
        elif trend == 'Bearish':
            return f'<span style="color: red;">{trend}</span>'
        else:
            return trend

    ranking_df['Trend'] = ranking_df['Trend'].apply(colorize_trend)
    ranking_df.to_html(filepath, index=False, escape=False)
