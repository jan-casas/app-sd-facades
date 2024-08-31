import logging

import pandas as pd
from sqlalchemy import create_engine

from config.settings import AZURE_DDBB


def fetch_data_from_db(query, sample_size: int = 1000):
    try:
        # Create the SQLAlchemy engine
        engine = create_engine(
            f"postgresql+psycopg2://{AZURE_DDBB['user']}:{AZURE_DDBB['password']}@"
            f"{AZURE_DDBB['host']}:{AZURE_DDBB['port']}/{AZURE_DDBB['database']}")

        # Retrieve data from the table
        df = pd.read_sql_query(query, engine)

        # Reduce sample
        df_reduced = df.sample(sample_size)

        # Filter to include only numeric columns
        df_numeric = df_reduced.select_dtypes(include=[float, int])

        return df_numeric

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
