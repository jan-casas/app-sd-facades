import logging
import sys
import dash_bootstrap_components as dbc
from flask import Flask
import dash

# Load environment variables
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, '/static/style.css', dbc.icons.FONT_AWESOME]

# Define Flask app
app = Flask(__name__)

# Define Dash app
dash_app = dash.Dash(__name__, server=app, external_stylesheets=external_stylesheets, use_pages=True,
                     pages_folder='pages')
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define Dash app layout and callbacks
dash_app.layout = dash.page_container
