import base64
import io
import logging

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from src.core_callbacks import dash_app
from views.default.descriptions import *
from views.load_assets.load_assets import df_real_state_original
from views.discover_assets.dash_deck import *
from utils.utils import extract_main_colors


# Upload file interaction
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an Excel file
        return pd.read_excel(io.BytesIO(decoded))


# @dash_app.callback(
#     dash.dependencies.Output('datatable-upload-container', 'data'),
#     dash.dependencies.Output('datatable-upload-container', 'columns'),
#     dash.dependencies.Output('load_assets', 'figure'),
#     dash.dependencies.Input('datatable-upload', 'contents'),
#     dash.dependencies.State('datatable-upload', 'filename'))
def _deprecated_update_output(contents, filename):
    df_new = parse_contents(contents, filename)
    # TODO: Coalesce Insert into the database

    if df_new is not None:
        fig.add_trace(
            go.Scattermapbox(
                lat=df_new.latitude,
                lon=df_new.longitude,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=9,
                    color='#ff0000'
                ),
                cluster=dict(enabled=True),
                hovertext=df_new['local_id'],
            ))

    if contents is None:
        return [{}], [], fig

    return df_new.to_dict('records'), [{"name": i, "id": i} for i in df_new.columns], fig


# Update table with selected points
@dash_app.callback(
    dash.dependencies.Output('table', 'data'),
    dash.dependencies.Input('load_assets', 'selectedData'),
    dash.dependencies.State('table', 'data')
)
def update_table(selectedData, table_data):
    original_table_data = df_real_state_original.to_dict('records')
    if selectedData is None or not selectedData['points']:
        logging.error("No points selected.")
        return original_table_data

    selected_points = {point['pointIndex'] for point in selectedData['points']}
    filtered_data = [row for i, row in enumerate(original_table_data) if i in selected_points]
    logging.info(f"Selected points: {len(filtered_data)}")

    return filtered_data


# TODO: Add popups if the format is not correct

# My Assets location selectector in blank_map
@dash_app.callback(
    dash.dependencies.Output('layout_dash_deck', 'children'),
    [dash.dependencies.Input('url', 'pathname')],
    prevent_initial_call=False,
)
def callback(pathname):
    # Main colors
    image_path = 'static/images/energy_saving8.png'
    n_rows = df_real_state_original.shape[0]
    colors = extract_main_colors(image_path, n_rows)  # Use a default image path or color scheme
    colors_str = ['rgb(' + ', '.join(map(str, color)) + ')' for color in colors]

    # Parse data and create deck layer
    df_deck = parse_data(gdf, image_path)  # Use a default image path
    deck_layer = create_deck_layer(df_deck)
    print(f"Deck layer created with {n_rows} rows.")

    return deck_layer


# Table home markdown interaction
# @dash_app.callback(
#     dash.dependencies.Output('table_home_markdown', 'children'),
#     [dash.dependencies.Input('datatable-interactivity', 'selected_rows')],
# )
def _deprecated_update_table_home_markdown(rows: list):
    # Every row must read a different markdown file
    # if multiple rows append it
    # TODO: Create a relation between the analysis row and the construction of the cards with the
    #  speckle models
    # if row is not None:
    #     return [dcc.Markdown(f"Row {r} selected") for r in row]
    # return no_update

    result = [
        html.Span('Analysis Explanation:'),
        dcc.Markdown("""
            The next Speckle Iframes models will show a glimpse of the analysis made in a small 
            size city of Spain. 
            This is 
            used for preview purposes. 
            The analysis includes various factors such as temperature, occupancy, climatic 
            responsiveness, 
            and installation performance. 
            Each of these factors is carefully studied and visualized using Speckle, 
            a data-driven design platform. 
            The models provide a comprehensive understanding of the city's architectural and 
            environmental dynamics. 
            They serve as a 
            valuable tool for architects, city planners, and environmentalists to make informed 
            decisions and create 
            sustainable urban 
            environments. 

            Please note that the models are interactive, allowing you to explore different 
            aspects of the city's 
            architecture and 
            environment in detail.
        """),
    ]

    for row in rows:
        df_description_selected = description_df.iloc[row, :]
        card = dbc.Card(
            [
                html.A(
                    html.Iframe(
                        src=df_description_selected["src"],
                        width="100%", height="100%", className="card-img"),
                    # target="_blank",
                    # id="card-preview-3"
                ),
                dbc.CardBody(
                    [
                        html.H5(df_description_selected["title"], className="card-title"),
                        html.P(df_description_selected["description"], className="card-text"),
                    ]
                ),
            ],
            className="h-100"
        )
        result.append(card)
        result.append(html.Br())
    return result
