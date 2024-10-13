import sqlite3
import logging
from functools import lru_cache
import pandas as pd
from sqlalchemy import create_engine
import os

from config.settings import AZURE_DDBB


# Generic function to fetch data from a database
def create_database_if_not_exists(db_path: str = r'G:\app-sd-facades\gis_data.db',
                                  sql_file: str = 'database.sql'):
    if not os.path.exists(db_path):
        try:
            with sqlite3.connect(db_path) as conn:
                with open(sql_file, 'r') as f:
                    conn.executescript(f.read())
            logging.info(f"Database created at {db_path} using {sql_file}.")
        except Exception as e:
            logging.error(f"An error occurred while creating the database: {e}")


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


@lru_cache(maxsize=32)
def fetch_data_from_sqlite_db(query, db_path: str = r'G:\app-sd-facades\gis_data.db',
                              sample_size=None, only_numeric=False):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # Retrieve data from the table
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        if sample_size:
            # Reduce sample
            df = df.sample(min(sample_size, len(df)))

        if only_numeric:
            # Filter to include only numeric columns
            df = df.select_dtypes(include=[float, int])

        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None


# Specific queries to retrieve data from the buildings database
def building_metadata():
    query = """
        SELECT DISTINCT "properties.gml_id", "properties.localId", "properties.numberOfFl"
        FROM main.monoparte
    """
    query = "SELECT * FROM main.real_estate_data_spain_updated"
    return fetch_data_from_sqlite_db(query)


def building_data():
    query = "SELECT * FROM main.real_estate_data_spain_updated"
    return fetch_data_from_sqlite_db(query)


def building_centroids():
    query = "SELECT * FROM main.monoparte"
    return fetch_data_from_sqlite_db(query)


def building_polygons():
    query = "SELECT * FROM main.data_barrios"
    return fetch_data_from_sqlite_db(query)


def building_entities():
    query = "SELECT * FROM main.df_propiedades_entidaddes"
    return fetch_data_from_sqlite_db(query)


def building_simulation_results():
    query = "SELECT * FROM main.simulation_results"
    return fetch_data_from_sqlite_db(query).round(2)
