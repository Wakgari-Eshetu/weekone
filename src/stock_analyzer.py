# src/stock_analyzer.py

import pandas as pd

class StockAnalyzer:
    """
    Class to handle stock returns and volatility calculation.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate_daily_returns(self, price_col='close') -> pd.DataFrame:
        """
        Calculate daily returns from stock prices.
        """
        self.df['daily_return'] = self.df[price_col].pct_change()
        return self.df

    def calculate_rolling_volatility(self, window=20) -> pd.DataFrame:
        """
        Calculate rolling volatility of daily returns.
        """
        self.df['volatility'] = self.df['daily_return'].rolling(window).std()
        return self.df
