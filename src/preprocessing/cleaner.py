from pathlib import Path

import pandas as pd

# Define input and output directories
RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def load_stock_data(file_path: Path) -> pd.DataFrame:
    """
    Load stock data from a CSV file.
    """
    return pd.read_csv(file_path)


def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the stock data.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove Adjusted Close column if it exists
    if "Adj Close" in df.columns:
        df = df.drop(columns=["Adj Close"])

    # Convert Date column to datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    # Convert numeric columns to numeric datatype
    numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with missing values
    df = df.dropna()

    # Sort by date
    if "Date" in df.columns:
        df = df.sort_values("Date")

    # Reset index
    df = df.reset_index(drop=True)

    return df


def save_clean_data(df: pd.DataFrame, filename: str):
    """
    Save cleaned data into the processed folder.
    """

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = PROCESSED_DATA_DIR / filename

    df.to_csv(output_file, index=False)


def main():

    csv_files = list(RAW_DATA_DIR.glob("*.csv"))

    print(f"Found {len(csv_files)} CSV files")

    for file in csv_files:

        print(f"Processing {file.name}")

        df = load_stock_data(file)

        cleaned_df = clean_stock_data(df)

        save_clean_data(cleaned_df, file.name)

        print(f"Saved cleaned file: {file.name}")


if __name__ == "__main__":
    main()