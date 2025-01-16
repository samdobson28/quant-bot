# data/storage/db_store.py

import pandas as pd
from sqlalchemy import create_engine

# NOTE: Adjust connection string parameters to match your local Postgres setup:
# Format: "postgresql://username:password@hostname:port/database"
# Example if running locally: "postgresql://quant_user:quant_pass@localhost:5432/quant_db"
DATABASE_URL = "postgresql://quant_user:quant_pass@localhost:5432/quant_db"

# Create a global engine instance
engine = create_engine(DATABASE_URL, echo=False)


def save_to_db(df: pd.DataFrame, table_name: str):
    """
    Appends DataFrame rows to the specified table in PostgreSQL.
    If the table doesn't exist, it will be created automatically.

    :param df: Pandas DataFrame containing your data.
    :param table_name: The name of the table in PostgreSQL.
    """
    # Write to the DB using DataFrame's built-in to_sql functionality
    df.to_sql(name=table_name, con=engine, if_exists="append", index=False)
    print(f"[db_store] Appended {len(df)} rows to '{table_name}'.")


def load_from_db(table_name: str, query_filter: str = "") -> pd.DataFrame:
    """
    Loads data from a specified table and optional filter.

    :param table_name: The name of the table in PostgreSQL.
    :param query_filter: An optional WHERE condition, e.g. "WHERE symbol = 'BTC/USD'"
    :return: A DataFrame with all (or filtered) rows from the table.
    """
    query = f"SELECT * FROM {table_name} {query_filter};"
    df = pd.read_sql(query, con=engine)
    print(f"[db_store] Loaded {len(df)} rows from '{table_name}' with filter '{query_filter}'.")
    return df
