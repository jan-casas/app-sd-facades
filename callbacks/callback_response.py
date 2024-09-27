import base64
import io
import logging
import sys

import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
import plotly.graph_objects as go
from dash import dcc, html
from dash_iconify import DashIconify
from numpy import intersect1d
from pandas import DataFrame

from core_callbacks import dash_app
from pages.pages_helper.descriptions import *
from src.app_load_assets import df_real_state_original
from src.app_mapbox_playground import update_mapbox, geojson, propiedades_entidad
from src.map_dash_deck import *
from utils.utils import extract_main_colors

sys.path.insert(0, '/static/style.py')
sys.path.insert(0, 'core_callbacks.py')
sys.path.insert(0, 'src/app_mapbox_playground.py')

# %%
"""# TODO: CHECK THE SPECKLE EUSKOTREN APP BECAUSE IT IS DONE THE SAME WAY
@dash_app.callback(
    [dash.dependencies.Output('table', 'data'),
     dash.dependencies.Output('table', 'columns')],
    [dash.dependencies.Input('parcoord_graph', 'selectedData')],
)
def update_figures(selected_data):
    # Read and process data
    df_real_state_original, df_post_analysis = read_and_process_data()

    # Filter data based on selected points in the parallel coordinates graph
    if selected_data:
        selected_points = [point['pointIndex'] for point in selected_data['points']]
        df_filtered = df_post_analysis.iloc[selected_points]
    else:
        df_filtered = df_post_analysis

    # Update table data
    table_data = df_filtered.to_dict('records')
    columns = [{"name": i, "id": i} for i in df_filtered.columns]

    return table_data, columns
"""


# %% ---- GENERIC/MODALS ----
# Playground experiments
@dash_app.callback(
    [dash.dependencies.Output(component_id='city_mapbox', component_property='figure'),
     dash.dependencies.Output('graph_edad', 'figure'),
     dash.dependencies.Output('graph_stacked', 'figure')],
    [dash.dependencies.Input('city_mapbox', 'selectedData')],
)
def callback(selection1):
    selectedpoints = geojson.index
    for selected_data in [selection1]:
        if selected_data and selected_data['points']:
            selectedpoints = intersect1d(selectedpoints,
                                         [p['customdata'] for p in selected_data['points']])
    df_selected = DataFrame.from_dict(selectedpoints)
    df_selected_prop = propiedades_entidad.iloc[df_selected.iloc[:, 0].values.tolist(
    ), :].reset_index(drop=True)

    return update_mapbox(geojson, selection1, df_selected_prop)


@dash_app.callback(
    dash.dependencies.Output("collapse_conclusion", "is_open"),
    [dash.dependencies.Input("button_conclusion", "n_clicks")],
    [dash.dependencies.State("collapse_conclusion", "is_open")],
)
def toggle_conclusion(n, is_open):
    if n:
        return not is_open
    return is_open


@dash_app.callback(
    dash.dependencies.Output("collapse_workflow", "is_open"),
    [dash.dependencies.Input("button_workflow", "n_clicks")],
    [dash.dependencies.State("collapse_workflow", "is_open")],
)
def toggle_conclusion(n, is_open):
    if n:
        return not is_open
    return is_open


@dash_app.callback(
    dash.dependencies.Output("modal_intro", "is_open"),
    [dash.dependencies.Input("button_intro", "n_clicks")],
    [dash.dependencies.State("modal_intro", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


# Default sidebar sub-items collapse
@dash_app.callback(
    dash.dependencies.Output("collapse_experiments", "is_open"),
    [dash.dependencies.Input("experiments_link", "n_clicks")],
    [dash.dependencies.State("collapse_experiments", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@dash_app.callback(
    dash.dependencies.Output("collapse_assets", "is_open"),
    [dash.dependencies.Input("assets_link", "n_clicks"),
     dash.dependencies.Input('url', 'pathname')],
    [dash.dependencies.State("collapse_assets", "is_open")],
)
def toggle_collapse(n, pathname, is_open):
    if pathname != '/assets/':
        if n:
            return not is_open
    return is_open


# Notification
@dash_app.callback(
    dash.dependencies.Output("notifications-container", "children"),
    dash.dependencies.Input("next-custom-icons", "n_clicks"),
    prevent_initial_call=True,
)
def show(n_clicks):
    return dmc.Notification(
        title="Hey there!",
        id="simple-notify",
        action="show",
        message="Notifications in Dash, Awesome!",
        icon=DashIconify(icon="ic:round-celebration"),
    )


# Collapse Row
@dash_app.callback(
    dash.dependencies.Output("collapse", "is_open"),
    dash.dependencies.Input("switch", "checked"),
)
def toggle_collapse(n):
    if n is True:
        return True
    return False


# Stepper interaction: Capture the active step and update page route based on the next and back
# buttons
@dash_app.callback(
    [dash.dependencies.Output('url', 'pathname'),
     dash.dependencies.Output('stepper-state', 'data')],
    [dash.dependencies.Input("next-custom-icons", "n_clicks"),
     dash.dependencies.Input("back-custom-icons", "n_clicks")],
    [dash.dependencies.State("stepper-state", "data")],
    prevent_initial_call=True,
)
def update_url(next_clicks, back_clicks, active_step):
    logging.info(
        f"Active step: {active_step}, Next clicks: {next_clicks}, Back clicks: {back_clicks}")

    # Detect active step
    active_step_var = active_step if active_step is not None else 0

    if next_clicks is not None and back_clicks is None:
        active_step_var += 1
    elif next_clicks is None and back_clicks is not None:
        active_step_var -= 1

    logging.info(active_step_var)

    # Re-route based on active step
    if active_step_var == 0:
        return "/home", active_step_var
    elif active_step_var == 1:
        return "/assets", active_step_var
    elif active_step_var == 2:
        return "/futures", active_step_var
    elif active_step_var > 2 or active_step_var < 1:
        return "/home", 0


@dash_app.callback(
    dash.dependencies.Output('stepper-custom-icons', 'active'),
    dash.dependencies.Input('stepper-state', 'data'),
    prevent_initial_call=True,
)
def update_stepper(active_step):
    return active_step


# ---- LAYOUT LOAD ----
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


"""@dash_app.callback(
    dash.dependencies.Output('datatable-upload-container', 'data'),
    dash.dependencies.Output('datatable-upload-container', 'columns'),
    dash.dependencies.Output('load_assets', 'figure'),
    dash.dependencies.Input('datatable-upload', 'contents'),
    dash.dependencies.State('datatable-upload', 'filename'))
def update_output(contents, filename):
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
"""


# Add this callback function to your Dash app
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

# ---- LAYOUT ASSETS ----
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


# ---- LAYOUT HOME ----
# Table home markdown interaction
@dash_app.callback(
    dash.dependencies.Output('table_home_markdown', 'children'),
    [dash.dependencies.Input('datatable-interactivity', 'selected_rows')],
)
def update_table_home_markdown(rows: list):
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


# ---- LAYOUT PERFORMANCE ----
