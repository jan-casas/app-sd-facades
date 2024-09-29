import numpy as np
import pandas as pd
import plotly.graph_objects as go

from config.settings import MAPBOX_TOKEN
from utils.utils_database import building_metadata, building_data
from views.default.descriptions import description_df


def read_and_process_data():
    df_building_metadata = building_metadata()
    df_building_data = building_data()

    title_simplified_title = description_df.set_index('title')['simplified_title'].to_dict()
    df_building_data = df_building_data.rename(
        columns={col: title_simplified_title[col] for col in df_building_data.columns if
                 col in title_simplified_title}
    )

    df_building_data = df_building_data.apply(pd.to_numeric, errors='coerce')
    df_building_data = df_building_data.dropna(axis=1, how='all')

    return df_building_metadata, df_building_data


def create_scattermapbox(df_building_metadata):
    fig = go.Figure()

    # Add clustered layer
    fig.add_trace(
        go.Scattermapbox(
            lat=df_building_metadata['latitude'],
            lon=df_building_metadata['longitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9,
                color='#ffc400'
            ),
            text=df_building_metadata['local_id'],
            cluster=dict(
                enabled=True,
                maxzoom=10
            ),
            name='Clusters'
        )
    )

    # Add individual points layer
    fig.add_trace(
        go.Scattermapbox(
            lat=df_building_metadata['latitude'],
            lon=df_building_metadata['longitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9,
                color='red'
            ),
            text=df_building_metadata['local_id'],
            name='Points',
            visible=False  # Initially hidden
        )
    )

    fig.update_layout(
        height=600,
        mapbox=dict(
            zoom=6,
            center=dict(lat=42.46, lon=-2.44),
            accesstoken=MAPBOX_TOKEN
        ),
        hovermode='closest',
        dragmode='lasso',
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
        uirevision='constant',
    )

    return fig


def create_empty_scattermapbox():
    empty_fig = go.Figure(
        go.Scattermapbox(
            lat=[],
            lon=[],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9,
                color='#ffc400'
            )
        )
    )

    empty_fig.update_layout(
        height=1800,
        mapbox=dict(
            zoom=6,
            center=dict(lat=42.46, lon=-2.44),
            accesstoken=MAPBOX_TOKEN
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
    )

    return empty_fig


def create_parcoord_figure(df_building_data, margin_value=20):
    # Ensure only columns with numeric data types (int or float) are processed
    df_building_data = df_building_data.select_dtypes(include=[np.number])

    # Round, drop NaNs and any non-finite values
    df_building_data = df_building_data.round(2).dropna()

    par_coord_dimensions = []
    for column in df_building_data.columns:
        finite_values = df_building_data[column][np.isfinite(df_building_data[column])]
        if not finite_values.empty:
            par_coord_dimensions.append(
                dict(
                    range=[finite_values.min(), finite_values.max()],
                    label=column.upper(),
                    values=finite_values
                )
            )

    fig_pa = go.Figure(
        data=go.Parcoords(
            line=dict(
                showscale=False,
            ),
            dimensions=par_coord_dimensions,
        )
    )

    fig_pa.update_layout(
        margin={"r": margin_value, "t": margin_value * 3, "l": margin_value, "b": margin_value * 3},
        showlegend=False,
    )

    return fig_pa


# Initialize the data and figures
filtered_building_metadata, filtered_building_data = read_and_process_data()

fig = create_scattermapbox(filtered_building_metadata)
empty_fig = create_empty_scattermapbox()

fig_par = create_parcoord_figure(filtered_building_data)
