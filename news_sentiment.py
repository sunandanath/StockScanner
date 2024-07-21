import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fetch_news(symbol, api_key):
    """
    Fetch news articles for a given stock symbol using NewsAPI.

    Args:
        symbol (str): Stock symbol to fetch news for.
        api_key (str): NewsAPI key.

    Returns:
        list: List of news articles.
    """
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        return []

def analyze_sentiment(articles):
    """
    Analyze the sentiment of a list of news articles.

    Args:
        articles (list): List of news articles.

    Returns:
        dict: Sentiment scores.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = {'positive': 0, 'neutral': 0, 'negative': 0}
    
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        text = title + ' ' + description
        sentiment = analyzer.polarity_scores(text)
        if sentiment['compound'] >= 0.05:
            sentiment_scores['positive'] += 1
        elif sentiment['compound'] <= -0.05:
            sentiment_scores['negative'] += 1
        else:
            sentiment_scores['neutral'] += 1
            
    return sentiment_scores

def get_news_sentiment(symbol, api_key):
    """
    Get news sentiment for a given stock symbol.

    Args:
        symbol (str): Stock symbol to get news sentiment for.
        api_key (str): NewsAPI key.

    Returns:
        dict: Sentiment scores.
    """
    articles = fetch_news(symbol, api_key)
    if not articles:
        return {'positive': 0, 'neutral': 0, 'negative': 0}
    
    sentiment_scores = analyze_sentiment(articles)
    return sentiment_scores
