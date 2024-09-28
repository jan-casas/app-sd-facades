import dash
import dash_bootstrap_components as dbc
from flask import Flask

# Load environment variables
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, 'static/style.css',
                        dbc.icons.FONT_AWESOME]

# Define Flask app
app = Flask(__name__)

# Define Dash app
dash_app = dash.Dash(__name__, server=app, external_stylesheets=external_stylesheets,
                     use_pages=True, pages_folder='views', prevent_initial_callbacks='initial_duplicate')

# Define Dash app layout and callbacks
dash_app.layout = dash.page_container
