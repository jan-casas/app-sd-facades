"""
Adapted from: https://pydeck.gl/gallery/polygon_layer.html

Property values in Vancouver, Canada, adapted from the deck.gl example pages.
This demos luma.gl-based shadows using the LightingEffect effect.

"""
import os
import math

import dash
import dash_deck
import dash_html_components as html
import pydeck as pdk
import pandas as pd

from utils.utils import extract_main_colors_rgb

# Load in the JSON data
DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
json = pd.read_json(DATA_URL)


def parse_data(json, image_path='static/images/energy_saving7.png', df=pd.DataFrame(), n=13):
    # Custom color scale
    # n = 13
    # image_path = 'static/images/energy_saving7.png'
    COLOR_RANGE = extract_main_colors_rgb(image_path, n)
    BREAKS = [-0.6 + i * (1.8 / (n - 1)) for i in range(n)]

    def color_scale(val):
        for i, b in enumerate(BREAKS):
            if val < b:
                return COLOR_RANGE[i]
        return COLOR_RANGE[i]

    def calculate_elevation(val):
        return math.sqrt(val) * 10

    # Parse the geometry out in Pandas
    df["coordinates"] = json["features"].apply(lambda row: row["geometry"]["coordinates"])
    df["valuePerSqm"] = json["features"].apply(lambda row: row["properties"]["valuePerSqm"])
    df["growth"] = json["features"].apply(lambda row: row["properties"]["growth"])
    df["elevation"] = json["features"].apply(
        lambda row: calculate_elevation(row["properties"]["valuePerSqm"])
    )
    df["fill_color"] = json["features"].apply(
        lambda row: color_scale(row["properties"]["growth"])
    )

    return df


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
            "latitude": 49.254,
            "longitude": -123.13,
            "zoom": 11,
            "maxZoom": 16,
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
        get_elevation="elevation",
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
        mapboxKey="pk.eyJ1IjoiamFuY2FzYXMiLCJhIjoiY2tlYTk4ZnBlMTBwZzJ5cHhzbzBjdTltaSJ9.nYGQnvw5kkC0m0EC5eHLbg"
    )

    return layout_dash_deck
