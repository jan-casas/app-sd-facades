import dash_bootstrap_components as dbc
from dash import dcc, html
from views.default.descriptions import congrats_conclusion, congrats_intro

modal_default_layout = dbc.Row([
    html.Hr(style={'borderTop': '1px solid white'}),
    dbc.Row([
        html.H3('Your Assets Performance on Current Analysis'),
        html.Span('Top Assets Performing the Current Analysis:'),
        dcc.Graph(id='progress_graph_max', figure={})
    ]),
    dbc.Row([
        html.Span('Low Assets Performing the Current Analysis:'),
        dcc.Graph(id='progress_graph_min', figure={}),
        dcc.Graph(id='progress_graph_global', figure={}, style={'display': 'none'}),
        dcc.Markdown("""**Figure 1.** Bar chart about the current performance of the discover_assets."""),
        dcc.Markdown(congrats_intro),
    ]),
    html.H3('Valuable Assets on Current Analysis'),
    html.Span('Location of best performing discover_assets:'),
    dbc.Row(
        dcc.Graph(id='city_mapbox_modal', figure={}, clickData={'points': []}, config={'displayModeBar': False}),
        style={'height': '50vh'}),
    dcc.Markdown("""**Figure 1.** Architecture of the API."""),
    dbc.Row([
        html.Span('Top Assets In Spain Performing the Current Analysis:'),
        dcc.Graph(id='subplot_div', figure={}),
        dcc.Markdown("""**Figure 1.** Bar chart about the current performance of the discover_assets globally."""),
        dcc.Markdown(congrats_conclusion),
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.Col(dbc.Card(
                        [
                            html.H2("Ocupación:",
                                    className="card-title"),
                            html.H2("Es del 20%",
                                    className="card-text"),
                        ],
                        body=True,
                        color="light",
                    ), width='50%'),
                    # dcc.Graph(id='monthly_heatmap', figure={},
                    #           className="card-img-small"),

                    # html.A(
                    #     dbc.CardImg(src="/static/images/OIG (2).jpg",
                    #                 top=True, alt="...", className="card-img-small"),
                    #     href="#",
                    #     id='card-image-2'
                    # ),
                    dbc.CardBody(
                        [
                            html.H5("Ocupancy and Density",
                                    className="card-title"),
                            html.P(
                                "Explorative Non Real Spaces are digital canvases where designers are unshackled by the constraints of reality, enabling boundless creativity and the conception of visionary architectural concepts."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.Row([
                        dbc.Col(dbc.Card(
                            [
                                html.H2("Responsividad:",
                                        className="card-title"),
                                html.H2("Es de 1.2s",
                                        className="card-text"),
                            ],
                            body=True,
                            color="light",
                        ), width='50%'),
                        dbc.Col(dbc.Card(
                            [
                                html.H2("Consumo:",
                                        className="card-title"),
                                html.H2("Es de 120Kw/h",
                                        className="card-text", style={'color': 'white'}),
                            ],
                            body=True,
                            color="dark",
                            inverse=True,
                        ), width='50%'),

                    ], ),
                    dbc.CardBody(
                        [
                            html.H5("Climatic Responsive Design",
                                    className="card-title"),
                            html.P(
                                "Urban analysis has evolved with a data-driven approach, enabling city planners."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.Row([
                        dbc.Col(dbc.Card(
                            [
                                html.H2("Performance:",
                                        className="card-title"),
                                html.H2("Está al 95%",
                                        className="card-text"),
                            ],
                            body=True,
                            color="light",
                        ), width='50%'),
                        dbc.Col(dbc.Card(
                            [
                                html.H2("Incidencias:",
                                        className="card-title"),
                                html.H2("Hay 12 Incidencias",
                                        className="card-text", style={'color': 'white'}),
                            ],
                            body=True,
                            color="dark",
                            inverse=True,
                        ), width='50%'),

                    ], ),
                    dbc.CardBody(
                        [
                            html.H5("Installation Performance",
                                    className="card-title"),
                            html.P(
                                "Leverages generative design to swiftly explore and implement solutions."),
                        ]
                    ),

                ],
                className="h-100"
            ),
        ),
    ]),
    dbc.Row([
        html.Hr(style={'borderTop': '1px solid white'}),
        html.Span("Know more about this analysis on your discover_assets, please visit the [GitHub repository]()"),
        html.Hr(style={'borderTop': '1px solid white'}),
        html.Hr(style={'borderTop': '1px solid white'}),
    ]),
    # TODO: Add className to modulate the size of the modal
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})
