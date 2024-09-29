import dash
from dash import State, ctx

from core_callbacks import dash_app

restricted_page = {}


def require_login(page):
    for pg in dash.page_registry:
        if page == pg:
            restricted_page[dash.page_registry[pg]['path']] = True


# Callback for login authentication
@dash_app.callback(
    [dash.dependencies.Output('output-state', 'children'),
     dash.dependencies.Output('url', 'pathname'),
     dash.dependencies.Output('login-data', 'data')],
    dash.dependencies.Input('login-button', 'n_clicks'),
    [dash.dependencies.State('uname-box', 'value'),
     dash.dependencies.State('pwd-box', 'value')]
)
def login_auth(n_clicks, username, password):
    if n_clicks and ctx.triggered_id == 'login-button':
        if username == "admin" and password == "1234":
            return "Login successful! Redirecting...", "/load", {'username': username,
                                                                 'password': password}
        else:
            return "Invalid username or password. Please try again.", dash.no_update, dash.no_update
    return "", dash.no_update, dash.no_update
