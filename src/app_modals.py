from typing import List
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import sys
from config.settings import MAPBOX_TOKEN
import logging
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots

sys.path.insert(0, '../core_callbacks.py')


def create_subplots(df: pd.DataFrame, ncols: int = 3, colors_str: List[str] = None):
    # Define the number of rows for the subplot layout
    nrows = int(np.ceil(df.shape[0] / ncols))
    df['color'] = colors_str

    # Create a subplot with secondary y-axis
    fig = make_subplots(rows=nrows, cols=ncols, subplot_titles=df['localid'].tolist(),
                        specs=[[{'secondary_y': True}] * ncols] * nrows,
                        horizontal_spacing=0.07,  # Adjust this value as needed
                        vertical_spacing=0.1)  # Adjust this value as needed

    # Iterate over each row in the DataFrame
    for i in range(df.shape[0]):
        # Create a histogram for the row
        hist = go.Histogram(x=df.iloc[i, :], nbinsx=20, name=f'Row {i + 1}', histnorm='probability density',
                            histfunc='count', marker_color=df.iloc[i, :]['color'])

        # Calculate the row and column position for the subplot
        row = i // ncols + 1
        col = i % ncols + 1

        # Add the histogram to the subplot
        fig.add_trace(hist, row=row, col=col, secondary_y=True)

        # Add a vertical line to show the current value
        fig.add_shape(

            type="line",
            x0=df.iloc[i, :]['value'],
            y0=0,
            x1=df.iloc[i, :]['value'],
            y1=1,
            yref="paper",
            line=dict(
                color="RoyalBlue",
                width=1,
            ),
            row=row,
            col=col,
        )

        # Add text to show the current value
        fig.add_annotation(
            x=df.iloc[i, :]['value'],
            y=0.95,
            yref="paper",
            text=f"{df.iloc[i, :]['value']}",
            showarrow=False,
            font=dict(
                size=8,
                color="RoyalBlue"
            ),
            row=row,
            col=col,
        )

    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font=dict(
            family="Colfax",
            size=8
        )
    )

    fig.update_yaxes(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='lightgray')
    fig.update_xaxes(showgrid=False, gridcolor='lightgray', zeroline=True, zerolinecolor='lightgray')
    # Reduce the title size of the subplots
    fig.update_annotations(dict(font=dict(size=12)))
    # Return the subplot
    return fig


def create_progress_bars(df):
    progress_bars = []
    for index, row in df.iterrows():
        progress_bar = dbc.Progress(id="progress", value=row['value'], max=row['max'], label=row['label'],
                                    animated=False, striped=True, color=row['color'], className="mb-1")
        progress_bars.append(progress_bar)
    return progress_bars


# create horizontal bar graph
def create_figure(df: pd.DataFrame, graph_height: int) -> go.Figure:
    fig = go.Figure(go.Bar(
        x=df['value'],
        y=df['label'],
        orientation='h',
        marker_color=df['color'],
        opacity=0.6,
        text=df['label'],
        textposition='auto',
    ))

    fig.update_layout(
        xaxis=dict(showticklabels=False),
        yaxis=dict(showticklabels=False),
        bargap=0.15,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=graph_height,
        font=dict(
            family="Colfax",
            size=10
        )
    )

    return fig


def horizontal_bar_graph(df: pd.DataFrame, df_global: pd.DataFrame, graph_height: int = 80,
                         colors_str: List[str] = None):
    df['color'] = colors_str
    top_performers = df.sort_values(by='value', ascending=True).tail(4)
    lower_performers = df.sort_values(by='value', ascending=True).head(4)
    global_performers = df_global.sort_values(by='value', ascending=True).tail(4)

    fig_top = create_figure(top_performers, graph_height)
    fig_lower = create_figure(lower_performers, graph_height)
    fig_global = create_figure(global_performers, graph_height)

    return fig_top, fig_lower, fig_global


# Mapbox plotly
def mapbox_plotly(city_data: pd.DataFrame = None, df_global: pd.DataFrame = None, title: str = 'Mapa de la ciudad',
                  marker_size: int = 30, colors_str: List[str] = None) -> go.Figure:
    try:
        city_data['color'] = colors_str
        # Create the figure
        fig = go.Figure()

        # Normalize the size of the markers (max 20)
        marker_display_size = city_data.copy()
        marker_display_size['number_assets'] = city_data['number_assets'] / city_data[
            'number_assets'].max() * marker_size

        # Add the mapbox
        for index, row in city_data.iterrows():
            fig.add_trace(go.Scattermapbox(
                lat=[row['lat']],
                lon=[row['lon']],
                mode='markers+text',
                marker=go.scattermapbox.Marker(
                    size=marker_display_size.loc[index, 'number_assets'],
                    color=row['color'],
                    showscale=False,
                    opacity=0.85
                ),
                text=[row['localid'] + ': ' + str(row['number_assets'])],
                textposition='bottom center'
            ))

            if index in df_global.index:
                fig.add_trace(go.Scattermapbox(
                    lat=[df_global.at[index, 'lat']],
                    lon=[df_global.at[index, 'lon']],
                    mode='markers',
                    marker=go.scattermapbox.Marker(
                        size=7,
                        color='red',
                        showscale=False,
                        opacity=0.65
                    ),
                    text=[df_global.at[index, 'localid'] + ': ' + str(df_global.at[index, 'number_assets'])],
                    textposition='bottom center'
                ))

        # Add the layout
        fig.update_layout(
            title=title,
            autosize=True,
            hovermode='closest',
            showlegend=False,
            mapbox=dict(
                style='light',
                accesstoken=MAPBOX_TOKEN,
                bearing=0,
                center=dict(
                    lon=-3.70256,
                    lat=40.4165
                ),
                pitch=0,
                zoom=5
            ),
            margin=dict(l=0, r=0, t=0, b=0),
        )

        return fig

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise e
