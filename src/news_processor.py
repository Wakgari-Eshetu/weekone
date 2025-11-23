# src/news_processor.py

import pandas as pd
from textblob import TextBlob
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

class NewsProcessor:
    """
    Class to handle news preprocessing and sentiment analysis.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def clean_text(self, text_col='headline') -> pd.DataFrame:
        """
        Clean text: lowercase, remove punctuation, remove stopwords.
        """
        stop_words = set(stopwords.words('english'))
        self.df[text_col] = self.df[text_col].str.lower()
        self.df[text_col] = self.df[text_col].str.translate(str.maketrans('', '', string.punctuation))
        self.df[text_col] = self.df[text_col].apply(lambda x: ' '.join([w for w in x.split() if w not in stop_words]))
        return self.df

    def analyze_sentiment(self, text_col='headline') -> pd.DataFrame:
        """
        Add sentiment score column using TextBlob.
        """
        self.df['sentiment'] = self.df[text_col].apply(lambda x: TextBlob(x).sentiment.polarity)
        self.df['sentiment_label'] = self.df['sentiment'].apply(
            lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
        return self.df
