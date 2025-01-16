# data/storage/local_store.py

import pandas as pd

def save_to_csv(df: pd.DataFrame, output_path: str):
    """
    Saves DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"[local_store] Data saved to {output_path}")
