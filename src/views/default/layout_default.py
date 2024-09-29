import datetime

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify

# HEADER
last_updated = datetime.datetime.now().strftime('%Y-%m -%d')

layout_header = dbc.NavbarSimple(
    children=[
        # html.H6("Grupo Aransa"),
        # html.Span("|"),
        # html.Span("Hello again, MK", className="navbar-text me-2"),
        # dmc.Indicator(
        #     dmc.Avatar("MK", color="cyan", radius="xl"),
        #     inline=True,
        #     size=12,
        #     # label="New",
        #     color="blue",
        #     # processing=True
        # ),
        dmc.Switch(
            id="switch",
            onLabel="DEV",
            offLabel="NOOB",
            color="blue",
            size="lg",
            checked=False
        ),
    ],
    sticky="top",
    className='app-header justify-content-center',
)

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2([
                    "Urban Data",
                    dbc.Badge("Breeze v1.2", color="info", className="ms-2")
                ],
                    style={"color": "black"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        # dbc.Input(type="search", placeholder="Search", className="mb-3"),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="bi bi-person-circle me-2"),
                        html.Span("Login"),
                    ],
                    href="/login",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-cloud-upload-fill me-2"),
                        html.Span("Load Assets"),
                        # dbc.Collapse(
                        #     dbc.Nav(
                        #         [
                        #             dbc.NavLink([
                        #                 html.I(className="bi bi-dash-square-dotted me-2"),
                        #                 html.Span("Edit Assets"),
                        #             ],
                        #                 href="/discover_assets/subitem2",
                        #                 active="exact"),
                        #         ],
                        #         vertical=True,
                        #     ),
                        #     id="collapse_assets",
                        #     is_open=False,
                        # ),
                    ],
                    href="/load",
                    active="exact",
                    id="assets_link",
                ),
                # dbc.NavLink(
                #     [html.I(className="bi bi-cart-check-fill me-2"),
                #      html.Span("Select Analysis")],
                #     href="/home",
                #     active="exact",
                # ),
                dbc.NavLink(
                    [html.I(className="bi bi-search-heart me-2"),
                     html.Span("Performance Assets")],
                    href="/performance",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.I(className="bi bi-arrow-through-heart-fill me-2"),
                     html.Span("Discover Assets "),
                     dbc.Badge("Premium", color="warning", className="ms-2")
                     ],
                    href="/assets",
                    active="exact",
                ),
                html.Hr(),
                # dbc.NavLink(
                #     [
                #         html.I(className="bi bi-balloon-heart-fill me-2"),
                #         html.Span("Explore Preferences"),
                #         dbc.Badge("New", color="warning", className="ms-2"),
                #         # dbc.Collapse(
                #         #     dbc.Nav(
                #         #         [
                #         #             dbc.NavLink([
                #         #                 html.I(className="bi bi-dash-square-dotted me-2"),
                #         #                 html.Span(" Energy Saving"),
                #         #             ],
                #         #                 href="/experiments/subitem1",
                #         #                 active="exact"),
                #         #             dbc.NavLink([
                #         #                 html.I(className="bi bi-dash-square-dotted me-2"),
                #         #                 html.Span(" Sun Exposure"),
                #         #             ],
                #         #                 href="/experiments/subitem2",
                #         #                 active="exact"),
                #         #         ],
                #         #         vertical=True,
                #         #     ),
                #         #     id="collapse_experiments",
                #         #     is_open=False,
                #         # ),
                #     ],
                #     href="/experiments",
                #     active="exact",
                #     id="experiments_link",
                # ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-life-preserver me-2"),
                        html.Span("Discuss"),
                    ],
                    # href="",
                    active="exact",
                    id="nav-link-contact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)


def get_icon(icon):
    return DashIconify(icon=icon, height=20)


# layout_notifications = dmc.NotificationProvider(
#     html.Div(
#         [
# html.Div(id="notifications-container"),
#         ]
#     )
# )

layout_footer = html.Footer([
    html.Div(id='grid-container_sub3', children=[
        html.Div([
            html.Div([
                html.Img(src='/static/icons/life-preserver.svg',
                         className='icon-item-icon',
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center',
                                'justifyContent': 'center'}),
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
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center',
                                'justifyContent': 'center'}),
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
                         style={'height': '20px', 'width': '20px', 'alignItems': 'center',
                                'justifyContent': 'center'}),
                html.H3('Service Status'),
                html.P(
                    'Check the status of the API services.'),
                html.A('Example Link', href='https://www.example.com')
            ], style={'marginLeft': '20px', 'textAlign': 'center'})
        ], id='grid-item-53', className='grid-item',
            style={'display': 'flex', 'alignItems': 'center', 'margin': '0px'}),
    ], style={'display': 'grid', 'grid-template-columns': 'repeat(3, 1fr)', 'grid-gap': '44px',
              'marginTop': '24px',
              'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto'}),
], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '50px',
          'background-color': '#f7f7f8', 'height': '200px'})

# Layout Chat
default_modal = dbc.Row([
    # html.Hr(),
    dbc.Col([
        html.H6('Code Example'),
        dcc.Markdown(
            '```python\n@app.route("/", methods=["GET"])\ndef read_root() -> dict:\n\treturn {'
            '"Hello": "World"}\n```'),
    ], style={'padding': '0px', 'margin': '0px'}),
    dbc.Col([
        html.H6('Response Example'),
        dcc.Markdown('```json\n{\n    "message": "Hello, World!"\n}\n```'),
    ], style={'padding': '0px', 'margin': '0px'}),
    html.Div(id='api-response', children=[]),
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px',
          'margin-top': '0px'})

default_response = dbc.Row([
    # html.Hr(),
    html.P(
        'Please tell us the orientation of the building where you live. This information is '
        'important for us to '
        'understand the amount of sunlight and shade your building receives throughout the day.\n '
        'Please tell us the '
        'orientation of the building where you live. This information is important for us to '
        'understand the amount of '
        'sunlight and shade your building receives throughout the day.',
        style={'color': '#202123', 'padding': '0px'}
    ),
    html.Div(id='api-response', children=[]),
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px',
          'margin-top': '0px'})

app_welcome = html.Div([
    html.H1('Bienvenido a la plataforma', style={
        'textAlign': 'left', 'margin-bottom': '20px'}),
    html.H2('Empieza con lo básico', style={'textAlign': 'left'})
], style={'margin-bottom': '48px', 'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto',
          'margin-top': '100px'})

LAYOUT_ASSETS = {
    '1': ['/static/icons/life-preserver.svg', 'Areas verdes próximas',
          'Find and refine existing data sources',
          'icon-item green-gradient-bg'],
    '2': ['/static/icons/virus.svg', 'Polución del aire', 'Deploy always changing scenarios',
          'icon-item pink-gradient-bg'],
    '3': ['/static/icons/clock-fill.svg', 'Edad edificación', 'Reuse grasshopper definitions',
          'icon-item purple-gradient-bg'],
    '4': ['/static/icons/browser-safari.svg', 'Orientación edificación',
          'Query large datasets just asking for insights', 'icon-item yellow-gradient-bg'],
    '5': ['/static/icons/volume-mute-fill.svg', 'Índice de ruido',
          'Perform geospatial analysis on the cloud',
          'icon-item pink-gradient-bg'],
    '6': ['/static/icons/fingerprint.svg', 'Proximidad cultural',
          'Associate precise data with your discover_assets',
          'icon-item red-gradient-bg'],
    '7': ['/static/icons/image-fill.svg', 'Potenciales vistas', 'Extract information from imagery',
          'icon-item blue-gradient-bg'],
    '8': ['/static/icons/thermometer.svg', 'Temperatura y clima',
          'Extract data simulating 3d models',
          'icon-item yellow-gradient-bg'],
    '9': ['/static/icons/chat-square-text-fill.svg', 'Cercanía lugares turísticos',
          'Extract information from imagery',
          'icon-item red-gradient-bg'],
    '10': ['/static/icons/balloon-heart-fill.svg', 'Densidad urbana',
           'Extract data simulating 3d models',
           'icon-item green-gradient-bg'],
}

TEXT_PLACEHOLDER = {
    '1': 'Hola, estoy buscando una casa en Valencia con orientación sur para aprovechar la luz '
         'solar. ¿Podrías '
         'recomendarme propiedades que cumplan con esta preferencia? Me encantaría tener '
         'habitaciones iluminadas por '
         'el sol de la mañana y espacios abiertos para disfrutar de la luz natural. Gracias.',
    '2': 'Hola, estoy buscando una casa en Valencia que esté en una zona tranquila y libre de '
         'ruidos en la calle. '
         '¿Podrías recomendarme propiedades que cumplan con esta preferencia? Me encantaría tener '
         'un ambiente '
         'tranquilo y silencioso para poder relajarme y disfrutar de mi hogar. Gracias.',
    '3': 'Hola, estoy buscando una casa en Valencia que sea de construcción reciente. ¿Podrías '
         'recomendarme '
         'propiedades que cumplan con esta preferencia? Me encantaría tener una casa moderna y '
         'actualizada con todas '
         'las comodidades y tecnologías más recientes. Gracias.',
    '4': 'Hola, estoy buscando una casa en Valencia que no esté en sombra debido a otros '
         'edificios cercanos. ¿Podrías '
         'recomendarme propiedades que cumplan con esta preferencia? Me encantaría tener una casa '
         'con buena '
         'iluminación natural y sin sombras de otros edificios que puedan afectar la luz solar. '
         'Gracias.',
    '5': 'Hola, estoy buscando una casa en Valencia que esté cerca del centro de la ciudad. '
         '¿Podrías recomendarme '
         'propiedades que cumplan con esta preferencia? Me encantaría tener una casa con fácil '
         'acceso a todas las '
         'comodidades y atracciones del centro de la ciudad. Gracias.',
    '6': 'Hola, estoy buscando una casa en Valencia que esté cerca de parques y entornos '
         'vegetales. ¿Podrías '
         'recomendarme propiedades que cumplan con esta preferencia? Me encantaría tener una casa '
         'con fácil acceso a '
         'espacios verdes y naturales para disfrutar del aire libre y la naturaleza. Gracias.',
    '7': 'Hola, estoy buscando una casa en Valencia que no esté cerca de centros turísticos. '
         '¿Podrías recomendarme '
         'propiedades que cumplan con esta preferencia? Me encantaría tener una casa en una zona '
         'tranquila y alejada '
         'del bullicio turístico para poder disfrutar de mi hogar en paz. Gracias.',
    '8': 'Hola, estoy buscando una casa en Valencia que tenga buenas vistas. ¿Podrías '
         'recomendarme propiedades que '
         'cumplan con esta preferencia? Me encantaría tener una casa con una vista impresionante '
         'de la ciudad o del '
         'paisaje natural. Gracias.',
    '9': 'Hola, estoy buscando una casa en Valencia que tenga un consumo energético eficiente. '
         '¿Podrías recomendarme '
         'propiedades que cumplan con esta preferencia? Me encantaría tener una casa con un bajo '
         'consumo de energía y '
         'que sea respetuosa con el medio ambiente. Gracias.',
    '10': 'Hola, estoy buscando una casa en Valencia que esté en un vecindario seguro. ¿Podrías '
          'recomendarme '
          'propiedades que cumplan con esta preferencia? Me encantaría tener una casa en una zona '
          'con bajos índices '
          'de criminalidad y donde pueda vivir tranquilo y sin preocupaciones. Gracias.',

}
