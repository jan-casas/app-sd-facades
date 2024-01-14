'''
Default layout for the app
Contains the header, footer and body for the app
'''

from dash import Dash, Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc
import datetime

# HEADER
last_updated = datetime.datetime.now().strftime('%Y-%m-%d')

layout_header = dbc.NavbarSimple(
    children=[
        dcc.Markdown(''' 
    # My Dash Application
    ''', className='app-header-title'
                     ),
        dbc.NavItem(
            dbc.NavLink(
                f"Last updated: {last_updated}",
                # href="#",
                # id="last-updated-link",
                style={'font-style': 'italic', 'color': 'lightgray'}
            )
        ),
        dbc.NavItem(dbc.NavLink(
            "Journey", href="/"), id='journey'),
        dbc.NavItem(dbc.NavLink("Contact", href="/"),
                    id='contact'),
        dbc.NavItem(dbc.NavLink("Acknowledgements", href="/"),
                    id='Acknowledgements'),
        dbc.Popover(
            [
                # dbc.PopoverHeader("Popover title"),
                dbc.PopoverBody(
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This "
                    "example show the definition of a custom generative panel and its integration with the Speckle "
                    "API."),
            ],
            id="popover",
            target="contact",  # needs to be the same as the Button's id
            trigger="focus",
        ),
        dbc.Popover(
            [
                # dbc.PopoverHeader("Popover title"),
                dbc.PopoverBody(
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This "
                    "example show the definition of a custom generative panel and its integration with the Speckle "
                    "API."),
            ],
            id="popover",
            target="Acknowledgements",  # needs to be the same as the Button's id
            trigger="focus",
        ),
        dbc.Popover(
            [
                # dbc.PopoverHeader("Popover title"),
                dbc.PopoverBody(
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This "
                    "example show the definition of a custom generative panel and its integration with the Speckle "
                    "API."),
            ],
            id="popover",
            target="journey",  # needs to be the same as the Button's id
            trigger="focus",
        ),
    ],
    sticky="top",
    className='app-header'
)

layout_footer = html.Footer([
    html.Div(id='grid-container_sub3', children=[
        html.Div([
            html.Div([
                html.Img(src='/static/icons/life-preserver.svg',
                         className='icon-item-icon',
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center', 'justifyContent': 'center'}),
                html.H3('Help Center'),
                html.P(
                    'Answers to frequently asked account and billing questions.'),
                html.A('Example Link', href='https://www.example.com')
            ], style={'marginLeft': '20px', 'textAlign': 'center'})
        ], id='grid-item-51', className='grid-item',
            style={'display': 'flex', 'alignItems': 'center', 'margin': '0px'}),
        html.Div([
            html.Div([
                html.Img(src='/static/icons/search.svg',
                         className='icon-item-icon',
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center', 'justifyContent': 'center'}),
                html.H3('Disclosure'),
                html.P(
                    'Ask questions and discuss topics with other developers.'),
                html.A('Example Link', href='https://www.example.com')
            ], style={'marginLeft': '20px', 'textAlign': 'center'})
        ], id='grid-item-52', className='grid-item',
            style={'display': 'flex', 'alignItems': 'center', 'margin': '0px'}),
        html.Div([
            html.Div([
                html.Img(src='/static/icons/broadcast.svg',
                         className='icon-item-icon',
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center', 'justifyContent': 'center'}),
                html.H3('Service Status'),
                html.P(
                    'Check the status of the API services.'),
                html.A('Example Link', href='https://www.example.com')
            ], style={'marginLeft': '20px', 'textAlign': 'center'})
        ], id='grid-item-53', className='grid-item',
            style={'display': 'flex', 'alignItems': 'center', 'margin': '0px'}),
    ], style={'display': 'grid', 'grid-template-columns': 'repeat(3, 1fr)', 'grid-gap': '44px', 'marginTop': '24px',
              'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto'}),
], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '50px',
          'background-color': '#f7f7f8', 'height': '200px'})
