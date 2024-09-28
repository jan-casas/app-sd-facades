import logging
import sys

import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from numpy import intersect1d
from pandas import DataFrame

from src.core_callbacks import dash_app
from views.default._deprecated import update_mapbox, geojson, propiedades_entidad

sys.path.insert(0, '/static/style.py')
sys.path.insert(0, 'core_callbacks.py')
sys.path.insert(0, 'src/mapbox_interactive.py')

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


# ---- GENERIC/MODALS ----
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
    if pathname != '/performance_assets/':
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
        return "/performance_assets", active_step_var
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
