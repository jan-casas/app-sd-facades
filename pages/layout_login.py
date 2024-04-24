# TODO: https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import dash_mantine_components as dmc

dash.register_page(__name__, path='/login')

# Login screen
layout = dbc.Card(html.Form(
    [
        dbc.Row(
            html.H2("Please log in to continue:", id="h1"),
            justify="center"),
        dbc.Row(
            dmc.PasswordInput(
                label="Your username:",
                placeholder="Your password",
                icon=DashIconify(icon="bi:shield-lock"),
            ),
            # dcc.Input(placeholder="Enter your username", type="text", id="uname-box", name='username'),
        ),
        dbc.Row(
            dmc.PasswordInput(
                label="Your password:",
                placeholder="Your password",
                icon=DashIconify(icon="bi:shield-lock"),
            ),
        ),
        # dmc.Button("Outline button", variant="outline", color="blue", type="submit", id="login-button"),
        html.Div(children="", id="output-state")
    ], method='POST', className='sidebar-login'
    # , style={'background-image': 'url(/static/images/city_density.png)',
    #                                                   'background-size': 'cover', 'background-repeat': 'no-repeat'}
),
)
