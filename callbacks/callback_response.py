from dash.dependencies import Input, Output
from dash.dependencies import Input, Output, State
import openai
import logging
import sys
import time
from typing import List, Optional
import requests
import json

import dash
import dash_bootstrap_components as dbc

from callbacks_core import app, dash_app

# from dash.exceptions import PreventUpdate


sys.path.insert(0, '/static/style.py')
sys.path.insert(0, 'callbacks_core.py')


# %%
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
