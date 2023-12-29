'''
Default layout for the app
Contains the header, footer and body for the app
'''

from dash import Dash, Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc
import datetime


# %%
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
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This example show the definition of a custom generative panel and its integration with the Speckle API."),
            ],
            id="popover",
            target="contact",  # needs to be the same as the Button's id
            trigger="focus",
        ),
        dbc.Popover(
            [
                # dbc.PopoverHeader("Popover title"),
                dbc.PopoverBody(
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This example show the definition of a custom generative panel and its integration with the Speckle API."),
            ],
            id="popover",
            target="Acknowledgements",  # needs to be the same as the Button's id
            trigger="focus",
        ),
        dbc.Popover(
            [
                # dbc.PopoverHeader("Popover title"),
                dbc.PopoverBody(
                    "The Rhino Compute API allows you to run Rhino and Grasshopper algorithms in the cloud. This example show the definition of a custom generative panel and its integration with the Speckle API."),
            ],
            id="popover",
            target="journey",  # needs to be the same as the Button's id
            trigger="focus",
        ),
    ],
    sticky="top",
    className='app-header'
)
