import plotly.graph_objects as go
import numpy as np

from constants import MAPBOX_TOKEN

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

fig = go.Figure(data=[trace])

fig.update_layout(
    height=600,
    mapbox_zoom=6,
    mapbox_center_lat=42.46,
    mapbox_center_lon=-2.44,
    hovermode='closest',
    dragmode='lasso',
    # mapbox_style=map_style,
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
