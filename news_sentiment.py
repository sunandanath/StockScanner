###########################################################################################################

# News_sentiment _ Corporate Actions _ Earnings
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

def fetch_news(symbol, api_key):
    """
    Fetch news articles for a given stock symbol using NewsAPI.

    Args:
        symbol (str): Stock symbol to fetch news for.
        api_key (str): NewsAPI key.

    Returns:
        list: List of news articles.
    """
    url = f"https://newsapi.org/v2/everything?q={symbol}&language=en&sortBy=publishedAt&pageSize=100&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        logging.info(f"Fetched {len(articles)} articles for symbol: {symbol}")
        return articles
    else:
        logging.error(f"Failed to fetch news for symbol: {symbol}, Status Code: {response.status_code}")
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
        if text.strip() == '':  # Skip empty texts
            continue
        sentiment = analyzer.polarity_scores(text)
        logging.debug(f"Article: {text}, Sentiment: {sentiment}")
        if sentiment['compound'] >= 0.05:
            sentiment_scores['positive'] += 1
        elif sentiment['compound'] <= -0.05:
            sentiment_scores['negative'] += 1
        else:
            sentiment_scores['neutral'] += 1
            
    logging.info(f"Sentiment scores: {sentiment_scores}")
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


###########################################################################################################
# # News_sentiment _ Corporate Actions _ Earnings _ With Retry
# import requests
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import logging
# import time

# def fetch_news(symbol, api_key, retries=3, delay=60):
#     """
#     Fetch news articles for a given stock symbol using NewsAPI.

#     Args:
#         symbol (str): Stock symbol to fetch news for.
#         api_key (str): NewsAPI key.
#         retries (int): Number of retries if rate limit is exceeded.
#         delay (int): Delay in seconds between retries.

#     Returns:
#         list: List of news articles.
#     """
#     url = f"https://newsapi.org/v2/everything?q={symbol}&language=en&sortBy=publishedAt&pageSize=100&apiKey={api_key}"
#     for attempt in range(retries):
#         response = requests.get(url)
#         if response.status_code == 200:
#             news_data = response.json()
#             articles = news_data.get('articles', [])
#             logging.info(f"Fetched {len(articles)} articles for symbol: {symbol}")
#             return articles
#         elif response.status_code == 429:
#             logging.warning(f"Rate limit exceeded for symbol: {symbol}. Retrying in {delay} seconds.")
#             time.sleep(delay)
#         else:
#             logging.error(f"Failed to fetch news for symbol: {symbol}, Status Code: {response.status_code}")
#             break
#     return []

# def analyze_sentiment(articles):
#     """
#     Analyze the sentiment of a list of news articles.

#     Args:
#         articles (list): List of news articles.

#     Returns:
#         dict: Sentiment scores.
#     """
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = {'positive': 0, 'neutral': 0, 'negative': 0}
    
#     for article in articles:
#         title = article.get('title', '')
#         description = article.get('description', '')
#         text = title + ' ' + description
#         if text.strip() == '':  # Skip empty texts
#             continue
#         sentiment = analyzer.polarity_scores(text)
#         logging.debug(f"Article: {text}, Sentiment: {sentiment}")
#         if sentiment['compound'] >= 0.05:
#             sentiment_scores['positive'] += 1
#         elif sentiment['compound'] <= -0.05:
#             sentiment_scores['negative'] += 1
#         else:
#             sentiment_scores['neutral'] += 1
            
#     logging.info(f"Sentiment scores: {sentiment_scores}")
#     return sentiment_scores

# def get_news_sentiment(symbol, api_key):
#     """
#     Get news sentiment for a given stock symbol.

#     Args:
#         symbol (str): Stock symbol to get news sentiment for.
#         api_key (str): NewsAPI key.

#     Returns:
#         dict: Sentiment scores.
#     """
#     articles = fetch_news(symbol, api_key)
#     if not articles:
#         return {'positive': 0, 'neutral': 0, 'negative': 0}
    
#     sentiment_scores = analyze_sentiment(articles)
#     return sentiment_scores


###########################################################################################################
# News_sentiment _ Corporate Actions

# import requests
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# def fetch_news(symbol, api_key):
#     """
#     Fetch news articles for a given stock symbol using NewsAPI.

#     Args:
#         symbol (str): Stock symbol to fetch news for.
#         api_key (str): NewsAPI key.

#     Returns:
#         list: List of news articles.
#     """
#     url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         news_data = response.json()
#         return news_data['articles']
#     else:
#         return []

# def analyze_sentiment(articles):
#     """
#     Analyze the sentiment of a list of news articles.

#     Args:
#         articles (list): List of news articles.

#     Returns:
#         dict: Sentiment scores.
#     """
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = {'positive': 0, 'neutral': 0, 'negative': 0}
    
#     for article in articles:
#         title = article.get('title', '')
#         description = article.get('description', '')
#         text = title + ' ' + description
#         sentiment = analyzer.polarity_scores(text)
#         if sentiment['compound'] >= 0.05:
#             sentiment_scores['positive'] += 1
#         elif sentiment['compound'] <= -0.05:
#             sentiment_scores['negative'] += 1
#         else:
#             sentiment_scores['neutral'] += 1
            
#     return sentiment_scores

# def get_news_sentiment(symbol, api_key):
#     """
#     Get news sentiment for a given stock symbol.

#     Args:
#         symbol (str): Stock symbol to get news sentiment for.
#         api_key (str): NewsAPI key.

#     Returns:
#         dict: Sentiment scores.
#     """
#     articles = fetch_news(symbol, api_key)
#     if not articles:
#         return {'positive': 0, 'neutral': 0, 'negative': 0}
    
#     sentiment_scores = analyze_sentiment(articles)
#     return sentiment_scores

###########################################################################################################
