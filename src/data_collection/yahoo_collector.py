import os

import pandas as pd
import yfinance as yf

from config import STOCK_SYMBOLS, START_DATE, END_DATE
from logger import setup_logger

logger = setup_logger()


def download_stock_data(symbol: str) -> pd.DataFrame:
    """
    Download stock data from Yahoo Finance.
    """
    logger.info(f"Downloading {symbol}...")

    data = yf.download(
        symbol,
        start=START_DATE,
        end=END_DATE,
        progress=False,
        auto_adjust=False
    )

    # Flatten MultiIndex columns if they exist
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Convert Date index into a normal column
    data.reset_index(inplace=True)

    return data


def save_stock_data(symbol: str, data: pd.DataFrame):
    """
    Save downloaded data as CSV.
    """
    os.makedirs("data/raw", exist_ok=True)

    filename = f"data/raw/{symbol}.csv"

    data.to_csv(filename, index=False)

    logger.info(f"Saved -> {filename}")


def main():
    for symbol in STOCK_SYMBOLS:
        data = download_stock_data(symbol)
        save_stock_data(symbol, data)


if __name__ == "__main__":
    main()