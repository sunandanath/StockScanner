import pandas as pd

def calculate_technical_indicators(df):
    """
    Calculate technical indicators for a given DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame containing stock data with 'Close' prices.
    
    Returns:
        pd.DataFrame: DataFrame with additional columns for technical indicators.
    """
    df['10 Day MA'] = df['Close'].rolling(window=10).mean()
    df['20 Day MA'] = df['Close'].rolling(window=20).mean()
    df['Upper Band'] = df['20 Day MA'] + (df['Close'].rolling(window=20).std() * 2)
    df['Lower Band'] = df['20 Day MA'] - (df['Close'].rolling(window=20).std() * 2)
    return df

def determine_trend(df, period='3mo'):
    """
    Determine if the trend over the last specified period is bullish or bearish.
    
    Args:
        df (pd.DataFrame): DataFrame containing stock data with 'Close' prices.
        period (str): Period to determine the trend (default is '3mo').
    
    Returns:
        str: 'Bullish' if the trend is upward, 'Bearish' if the trend is downward.
    """
    # Calculate the trend based on the last 3 months
    if len(df) < 60:
        return 'Unknown'  # Not enough data to determine trend
    
    recent_data = df.tail(60)  # Assuming 20 trading days per month, 60 days for 3 months
    if recent_data['Close'].iloc[-1] > recent_data['Close'].iloc[0]:
        return 'Bullish'
    else:
        return 'Bearish'
