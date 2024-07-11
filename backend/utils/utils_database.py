import logging

import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

from constants import PG_HOST, PG_DATABASE, PG_USER, PG_PASS


def execute_query(query, params=None):
    try:
        with pg.connect(
                f"dbname={PG_DATABASE} user={PG_USER} host={PG_HOST} password={PG_PASS}") as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                logging.info("Data saved in postgres database successfully")
        return 'STATUS: OK'

    except Exception as e:
        logging.error(f"Error saving data in postgres database: {e}")
        return 'STATUS: ERROR'


def insert_dataframe(df: pd.DataFrame, table_name: str, schema_name: str):
    engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_DATABASE}")

    try:
        df.to_sql(table_name, engine, if_exists='append', index=False, schema=schema_name)
    except Exception as e:
        logging.error(f"Error saving data in postgres database: {e}")
    finally:
        engine.dispose()


def retrieve_dataframe(query):
    try:
        engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_DATABASE}")
        df = pd.read_sql(query, engine)
        return df

    except Exception as e:
        logging.error(f"Error retrieving data from postgres database: {e}")
        return None


def execute_queries(query, vars_list):
    """
    Execute a query with a list of variables

    Args:
        query (str): query to execute
        vars_list (list): list of variables to insert in the query
    """
    try:
        with pg.connect(
                f"dbname={PG_DATABASE} user={PG_USER} host={PG_HOST} password={PG_PASS}") as conn:
            with conn.cursor() as cur:
                cur.executemany(query=query, vars_list=vars_list)
                conn.commit()
                logging.info("Data saved in postgres database successfully")
        return 'STATUS: OK'

    except Exception as e:
        logging.error(f"Error saving data in postgres database: {e}")
        return 'STATUS: ERROR'

    finally:
        conn.close()


def convert_string_tuple(string_text_list, split_character=', '):
    # split_character=', '
    # string_text=db_arduino[0]
    tuple_list = []
    for t in string_text_list:
        string_delete_comillas = t.replace("(", "").replace(")", "")
        tuple_list.append(
            tuple(map(float, string_delete_comillas.split(split_character))))
    return tuple_list
