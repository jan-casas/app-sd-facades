import numpy as np
import pandas as pd
import plotly.graph_objects as go

from config.settings import MAPBOX_TOKEN
from pages.pages_helper.descriptions import description_df


def read_and_process_data():
    df_real_state_original = pd.read_excel('database/data/real_estate_data.xlsx')
    df_post_analysis = pd.read_excel('database/data/real_estate_data_spain_updated.xlsx')

    title_simplified_title = description_df.set_index('title')['simplified_title'].to_dict()
    df_post_analysis = df_post_analysis.rename(
        columns={col: title_simplified_title[col] for col in df_post_analysis.columns if
                 col in title_simplified_title}
    )

    df_post_analysis = df_post_analysis.apply(pd.to_numeric, errors='coerce')
    df_post_analysis = df_post_analysis.dropna(axis=1, how='all')

    return df_real_state_original, df_post_analysis


def create_scattermapbox(df_real_state_original):
    fig = go.Figure(
        go.Scattermapbox(
            lat=df_real_state_original['latitude'],
            lon=df_real_state_original['longitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=9,
                color='#ffc400'
            ),
            text=df_real_state_original['local_id'],
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


def create_parcoord_figure(df_post_analysis, margin_value=20):
    # Ensure only columns with numeric data types (int or float) are processed
    df_post_analysis = df_post_analysis.select_dtypes(include=[np.number])

    # Round, drop NaNs and any non-finite values
    df_post_analysis = df_post_analysis.round(2).dropna()

    par_coord_dimensions = []
    for column in df_post_analysis.columns:
        finite_values = df_post_analysis[column][np.isfinite(df_post_analysis[column])]
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
df_real_state_original, df_post_analysis = read_and_process_data()

fig = create_scattermapbox(df_real_state_original)
empty_fig = create_empty_scattermapbox()

fig_par = create_parcoord_figure(df_post_analysis)
