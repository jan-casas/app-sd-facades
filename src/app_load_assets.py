import pandas as pd
import plotly.graph_objects as go
import numpy as np

from constants import MAPBOX_TOKEN
from pages.pages_helper.descriptions import description_df

# Read Excel file
df = pd.read_excel('backend/database/data/real_estate_data.xlsx')
df_post_analysis = pd.read_excel('backend/database/data/real_estate_data_spain_updated.xlsx')
# map df vtitle value using the description df title-simplified title values
title_simplified_title = description_df.set_index('title')['simplified_title'].to_dict()
df_post_analysis = df_post_analysis.rename(
    columns={col: title_simplified_title[col] for col in df_post_analysis.columns if col in title_simplified_title})

MAPBOX_STYLE = 'mapbox://styles/jancasas/clvjtoxhd01ao01qz15ox2ljp'
# mapbox_style='mapbox://styles/jancasas/clxg3vbvt006h01qmds548xxw',
# mapbox_style='mapbox://styles/jancasas/clvjtfkfl01bg01qrel0igtek',

# Center of Logroño
center_lat = 42.46
center_lon = -2.44

# Generate 100 random latitude and longitude values around the center
np.random.seed(0)  # for reproducibility
lats = np.random.normal(loc=center_lat, scale=0.01, size=100)
lons = np.random.normal(loc=center_lon, scale=0.01, size=100)

# Generate 100 random names for the points
names = ["Point {}".format(i) for i in range(100)]

# Create a Scattermapbox trace with the random points
trace = go.Scattermapbox(
    lat=[],
    lon=[],
    mode='markers+text',  # Add 'text' to the mode
    marker=go.scattermapbox.Marker(
        size=9,
        color='#ffc400'
    ),
    text=names,  # Add labels to the points
    textposition='bottom center',  # Position the labels below the points
)

fig = go.Figure(
    go.Scattermapbox(
        lat=df.latitude,
        lon=df.longitude,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9,
            color='#ffc400'
        ),
        cluster=dict(enabled=True),
        hovertext=df['local_id'],
    )
)

fig.update_layout(
    height=600,
    mapbox_zoom=6,
    mapbox_center_lat=42.46,
    mapbox_center_lon=-2.44,
    hovermode='closest',
    dragmode='lasso',
    mapbox_accesstoken=MAPBOX_TOKEN,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    showlegend=False,
    uirevision='constant',
)

empty_fig = go.Figure(
    go.Scattermapbox(
        lat=[],
        lon=[],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9,
            color='#ffc400'
        ),
        cluster=dict(enabled=True),
    )
)

empty_fig.update_layout(
    height=1800,
    mapbox_zoom=6,
    mapbox_center_lat=42.46,
    mapbox_center_lon=-2.44,
    # mapbox_style=map_style,
    mapbox_accesstoken=MAPBOX_TOKEN,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    showlegend=False,
)

# Create par coordinates Plotly
# For each normalized column, set value
par_coord_dimensions = []
for column in df_post_analysis.columns:
    if column not in ['latitude', 'longitude', 'local_id', 'street', 'local_use', 'local_id', 'number', 'unit_cost',
                      'mantainance_cost']:
        par_coord_dimensions.append(
            dict(
                range=[df_post_analysis[column].min(), df_post_analysis[column].max()],
                label=column.upper(), values=df_post_analysis[column])
        )

fig_parcoord = go.Figure(
    data=go.Parcoords(
        line=dict(
            # color=df_post_analysis['year_construction'],
            # colorscale='Electric',
            showscale=False,
            # cmin=-df_post_analysis['year_construction'].min(),
            # cmax=-df_post_analysis['year_construction'].max(),
        ),
        dimensions=par_coord_dimensions,
    )
)

margin_value = 20
fig_parcoord.update_layout(
    # height=600,
    margin={"r": margin_value, "t": margin_value * 3, "l": margin_value, "b": margin_value * 3},
    showlegend=False,
    # uirevision='constant',
    # width=2800,

)
