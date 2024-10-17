# TODO: https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from views.load_assets.load_assets import empty_fig

dash.register_page(__name__, path='/login')

# Layout for the login screen
layout_login = dbc.Card(
    html.Form(
        [
            dbc.Row(
                html.H2("Please log in to continue:", id="h1"),
                justify="center"
            ),
            dbc.Row(
                dcc.Input(
                    placeholder="Enter your username",
                    type="text",
                    id="uname-box",
                    name='username',
                    className="mb-3",
                )
            ),
            dbc.Row(
                dcc.Input(
                    placeholder="Enter your password",
                    type="password",
                    id="pwd-box",
                    name='password',
                    className="mb-3",
                )
            ),
            dbc.Row(
                dbc.Button("Login", id="login-button", color="primary", className="mt-3")
            ),
            html.Div(children="", id="output-state", className="mt-3"),
            dcc.Store(id='login-data')
        ],
        className='sidebar-login'
    ),
    body=True,
    className='p-4'
)

# Layout for the background
layout_background = html.Div(
    dcc.Graph(id='empty_fig', figure=empty_fig, config={'displayModeBar': False}),
    style={
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'width': '100%',
        'height': '100%',
    },
)

# Complete layout
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
