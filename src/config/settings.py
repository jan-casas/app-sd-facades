import os

import openai
from dotenv import load_dotenv

load_dotenv()

AZURE_DDBB = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_DATABASE"),
    "port": os.getenv("DB_PORT")
}

LOCAL_DDBB = {
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASS"),
    "host": os.getenv("PG_HOST"),
    "database": os.getenv("PG_DATABASE"),
    "port": os.getenv("PG_PORT")
}

# Mapbox credentials
MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')
MAPBOX_MAP_STYLE = os.environ.get('MAPBOX_MAP_STYLE')
access_token_mapbox = os.environ.get("ACCESS_TOKEN_MAPBOX")
style_token_mapbox = os.environ.get("STYLE_TOKEN_MAPBOX")

# API credentials
openai.api_key = os.getenv("OPENAI_API_KEY", "")
weather_api_key = os.getenv("IQAIR_WEATHER_API", "")

MAPBOX_API = os.getenv("MAPBOX_API",
                       "pk.eyJ1IjoiamFuY2FzYXMiLCJhIjoiY2tlYTk4ZnBlMTBwZzJ5cHhzbzBjdTltaSJ9"
                       ".nYGQnvw5kkC0m0EC5eHLbg")

# Hughingface API
HUGGINGFACE_MAIL = os.getenv("HUGGINGFACE_API", "casasvil@protonmail.com")
HUGGINGFACE_PASSWORD = os.getenv("HUGGINGFACE_PASSWORD", "MArbuTpw29t:8zB")

# DATA URL
GIS_URL = {
    "centroid": os.getenv("GIS_CENTROID", r'G:\app-sd-facades\gis\data\monoparte.pkl'),
}
