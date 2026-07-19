from pathlib import Path

import pandas as pd

from indicators import add_features

PROCESSED_DATA_DIR = Path("data/processed")
FEATURE_DATA_DIR = Path("data/features")


def process_all_files():
    """
    Process all cleaned CSV files and generate feature datasets.
    """

    FEATURE_DATA_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = list(PROCESSED_DATA_DIR.glob("*.csv"))

    print(f"Found {len(csv_files)} processed files")

    for file in csv_files:

        print(f"Processing {file.name}")

        df = pd.read_csv(file)

        print(df.head())
        print(df.dtypes)

        df = add_features(df)

        output_file = FEATURE_DATA_DIR / file.name

        df.to_csv(output_file, index=False)

        print(f"Saved -> {output_file}")


if __name__ == "__main__":
    process_all_files()