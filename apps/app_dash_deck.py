"""
Adapted from: https://pydeck.gl/gallery/polygon_layer.html

Property values in Vancouver, Canada, adapted from the deck.gl example pages.
This demos luma.gl-based shadows using the LightingEffect effect.

"""
import os
import math

import dash
from dash import html
import dash_deck
from psycopg2.sql import SQL, Identifier
from sqlalchemy import create_engine, text
# import pickle
# import pyarrow as pa
# import pyarrow.parquet as pq

# import dash_html_components as html
import pydeck as pdk
import pandas as pd
import geopandas as gpd
from shapely import wkb

from utils.utils import extract_main_colors_rgb
from utils.utils_database import retrieve_df
from constants import MAPBOX_API, PG_USER, PG_PASS, PG_HOST, PG_DATABASE, PG_PORT

# Load in the JSON data
# Load the GeoJSON file
# DATA_URL = (r"C:\Users\casas\OneDrive\Escritorio\Projects-In "
#             r"Progress\APPS\app-sd-facades\gis\buildings\building_logroño_bp.geojson")
# gdf = gpd.read_file(DATA_URL)


query_buildings = text("SELECT * FROM {} WHERE numberoffl > 1;".format("qgis.logrono"))
gdf = retrieve_df(query_buildings)
gdf['geometry'] = gdf['wkb_geometry'].apply(lambda x: wkb.loads(bytes(x).hex(), hex=True))
gdf.rename(columns={'localid': 'localId', 'numberoffl': 'numberOfFl'}, inplace=True)


def extract_coordinates(geom):
    # Check the geometry type and process accordingly
    if geom.geom_type == 'Polygon':
        return [list(geom.exterior.coords)]
    elif geom.geom_type == 'MultiPolygon':
        # Extract coordinates for each Polygon in the MultiPolygon
        coords = []
        for polygon in geom.geoms:  # Use .geoms to properly iterate through a MultiPolygon
            coords.append(list(polygon.exterior.coords))
        return coords
    else:
        raise ValueError(f'Unhandled geometry type: {geom.geom_type}')


def parse_data(gdf, image_path='static/images/energy_saving7.png', df=pd.DataFrame(), n=13):
    # Custom color scale
    COLOR_RANGE = extract_main_colors_rgb(image_path, n)
    min_fl = 1
    max_fl = 50
    BREAKS = [min_fl + i * ((max_fl - min_fl) / (n - 1)) for i in range(n)]

    def color_scale(val):
        for i, b in enumerate(BREAKS):
            if val < b:
                return COLOR_RANGE[i]
        return COLOR_RANGE[i]

    def calculate_elevation(val):
        return val * 3

    # Parse the geometry out in Pandas
    df["coordinates"] = gdf["geometry"].apply(extract_coordinates)
    df["localId"] = gdf["localId"]
    df["numberOfFl"] = gdf["numberOfFl"].apply(calculate_elevation)
    df["fill_color"] = df["numberOfFl"].apply(color_scale)

    return df


# todo: check if the package is sending data about my geometry into the server (like mapbox does)
def create_deck_layer(df):
    # Add sunlight shadow to the polygons
    sunlight = {
        "@@type": "_SunLight",
        "timestamp": 1564696800000,  # Date.UTC(2019, 7, 1, 22),
        "color": [255, 255, 255],
        "intensity": 1.0,
        "_shadow": True,
    }

    ambient_light = {"@@type": "AmbientLight", "color": [255, 255, 255], "intensity": 1.0}

    lighting_effect = {
        "@@type": "LightingEffect",
        "shadowColor": [0, 0, 0, 0.5],
        "ambientLight": ambient_light,
        "directionalLights": [sunlight],
    }

    view_state = pdk.ViewState(
        **{
            "latitude": 42.466,
            "longitude": -2.450,
            "zoom": 15,
            "maxZoom": 17,
            "pitch": 45,
            "bearing": 0,
        }
    )

    tooltip = {
        "html": "<b>Value per Square Meter:</b> {valuePerSqm} <br /><b>Growth rate:</b> {growth}"
    }

    polygon_layer = pdk.Layer(
        "PolygonLayer",
        df,
        id="geojson",
        opacity=0.8,
        stroked=False,
        get_polygon="coordinates",
        filled=True,
        extruded=True,
        wireframe=False,
        get_elevation="numberOfFl",
        get_fill_color="fill_color",
        get_line_color=[255, 255, 255],
        auto_highlight=True,
        pickable=True,
    )

    r = pdk.Deck(
        polygon_layer,
        initial_view_state=view_state,
        map_style=pdk.map_styles.LIGHT,
        # effects=[lighting_effect],
    )

    layout_dash_deck = dash_deck.DeckGL(
        r.to_json(), id="deck-gl", tooltip=tooltip,
        mapboxKey=MAPBOX_API
    )

    return layout_dash_deck
