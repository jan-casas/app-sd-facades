from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user
from callbacks_core import app, dash_app
from flask import Flask, request, redirect, session
import os
from dash import dcc, html, Input, Output, State, ALL, no_update
from dash.exceptions import PreventUpdate
from utils.login_handler import restricted_page

#  passwords should be encrypted
VALID_USERNAME_PASSWORD = {"test": "test", "hello": "world"}


@app.route('/login', methods=['POST'])
def login_button_click():
    if request.form:
        username = request.form['username']
        password = request.form['password']
        if VALID_USERNAME_PASSWORD.get(username) is None:
            return """invalid username and/or password <a href='/login'>login here</a>"""
        if VALID_USERNAME_PASSWORD.get(username) == password:
            login_user(User(username))
            if 'url' in session:
                if session['url']:
                    url = session['url']
                    session['url'] = None
                    # redirect to target url
                    return redirect(url)
            # redirect to home
            return redirect('/')
        return """invalid username and/or password <a href='/login'>login here</a>"""


# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
app.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


class User(UserMixin):
    """
    User data model. It has to have at least self.id as a minimum
    """

    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    """This function loads the user by user id. Typically this looks up the user from a user database.
    We won't be registering or looking up users in this example, since we'll just login using LDAP server.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


@login_manager.user_loader
def load_user(username):
    """
    This function loads the user by user id. Typically this looks up the user from a user database.
    We won't be registering or looking up users in this example, since we'll just login using LDAP server.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


# Login
@dash_app.callback(
    Output("user-status-header", "children"),
    Output('url', 'pathname'),
    Input("url", "pathname"),
    Input({'index': ALL, 'type': 'redirect'}, 'n_intervals')
)
def update_authentication_status(path, n):
    # logout redirect
    if n:
        if not n[0]:
            return '', no_update
        else:
            return '', '/login'

    # test if user is logged in
    if current_user.is_authenticated:
        if path == '/login':
            return dcc.Link("logout", href="/logout"), '/'
        return dcc.Link("logout", href="/logout"), no_update
    else:
        # if page is restricted, redirect to login and save path
        if path in restricted_page:
            session['url'] = path
            return dcc.Link("login", href="/login"), '/login'

    # if path not login and logout display login link
    if current_user and path not in ['/login', '/logout']:
        return dcc.Link("login", href="/login"), no_update

    # if path login and logout hide links
    if path in ['/login', '/logout']:
        return '', no_update
