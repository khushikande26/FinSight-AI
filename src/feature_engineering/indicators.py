from pathlib import Path

import pandas as pd

PROCESSED_DATA_DIR = Path("data/processed")
FEATURE_DATA_DIR = Path("data/features")


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new financial features.
    """

    # Price Change
    df["Price_Change"] = df["Close"] - df["Open"]

    # High-Low Spread
    df["High_Low_Spread"] = df["High"] - df["Low"]

    # Daily Return
    df["Daily_Return"] = df["Close"].pct_change()

    # 20-Day Moving Average
    df["SMA_20"] = df["Close"].rolling(window=20).mean()

    # 50-Day Moving Average
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    return df