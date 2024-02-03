import sys
import dash
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from apps.app_modals import create_subplots
from callbacks_core import dash_app, app
from apps.app_mapbox_playground import update_mapbox, geojson, propiedades_entidad, blank_map
from pandas import DataFrame
from numpy import intersect1d

from utils.utils import extract_main_colors
from database.test_data import df
from apps.app_dash_deck import *
from constants import min_step, max_step, active

sys.path.insert(0, '/static/style.py')
sys.path.insert(0, 'callbacks_core.py')
sys.path.insert(0, 'apps/app_mapbox_playground.py')


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


# My Assets location selectector in blank_map
@dash_app.callback([
    dash.dependencies.Output('blank_map', 'figure'),
    dash.dependencies.Output('subplot_div_assets', 'figure'),
    dash.dependencies.Output('layout_dash_deck', 'children'), ],
    [dash.dependencies.Input('blank_map', 'selectedData'),
     dash.dependencies.Input('dropdown_analysis_id', 'value')],
)
def callback(selection1, dropdown_analysis_id):
    # Main colors
    n_rows = df.shape[0]
    colors = extract_main_colors(dropdown_analysis_id, n_rows)
    colors_str = ['rgb(' + ', '.join(map(str, color)) + ')' for color in colors]
    subplot_fig = create_subplots(df, colors_str=colors_str)

    selectedpoints = geojson.index
    for selected_data in [selection1]:
        if selected_data and selected_data['points']:
            selectedpoints = intersect1d(selectedpoints,
                                         [p['customdata'] for p in selected_data['points']])
    df_selected = DataFrame.from_dict(selectedpoints)
    df_selected_prop = propiedades_entidad.iloc[df_selected.iloc[:, 0].values.tolist(
    ), :].reset_index(drop=True)

    df_deck = parse_data(gdf, dropdown_analysis_id)
    deck_layer = create_deck_layer(df_deck)

    return blank_map(geojson, selection1, df_selected_prop), subplot_fig, deck_layer


# Stepper
@dash_app.callback(
    dash.dependencies.Output("stepper-custom-icons", "active"),
    dash.dependencies.Input("back-custom-icons", "n_clicks"),
    dash.dependencies.Input("next-custom-icons", "n_clicks"),
    dash.dependencies.State("stepper-custom-icons", "active"),
    prevent_initial_call=True,
)
def update_with_icons(back, next_, current):
    button_id = dash.ctx.triggered_id
    step = current if current is not None else active
    if button_id == "back-custom-icons":
        step = step - 1 if step > min_step else step
    else:
        step = step + 1 if step < max_step else step
    return step


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
