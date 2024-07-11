# TODO: https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507
import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

from src.app_load_assets import empty_fig

dash.register_page(__name__, path='/login')

# Login screen
layout_login = dbc.Card(
    html.Form(
        [
            dbc.Row(
                html.H2("Please log in to continue:", id="h1"),
                justify="center"),
            dbc.Row(
                dmc.PasswordInput(
                    label="Your username:",
                    placeholder="Your password",
                    # icon=DashIconify(icon="bi:shield-lock"),
                ),
                # dcc.Input(placeholder="Enter your username", type="text", id="uname-box",
                # name='username'),
            ),
            dbc.Row(
                dmc.PasswordInput(
                    label="Your password:",
                    placeholder="Your password",
                    # icon=DashIconify(icon="bi:shield-lock"),
                ),
            ),
            html.Div(children="", id="output-state")
        ], method='POST', className='sidebar-login'
    ),
)

layout_background = html.Div(
    dcc.Graph(id='empty_fig', figure=empty_fig, config={'displayModeBar': False}),
    style={
        # 'display': 'none',
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'width': '100%',
        'height': '100%',
    },
)

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    dcc.Loading(
        id="loading",
        type="dots",
        fullscreen=True,
        children=[
            layout_login,
            layout_background,
        ]),
])
