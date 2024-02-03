# import dash_daq as daq
import apps.app_mapbox_playground
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from pages.layout_default import layout_header, layout_footer, sidebar

dash.register_page(__name__, path="/experiments")

layout_workflow_explanation = dbc.Row([
    html.Hr(),
    dbc.Row([
        dbc.Col(
            dbc.Button(
                dcc.Markdown(''' 
                ## Energy savings of the building envelope
                ''', id='title_workflow'),
                id='button_workflow',
                color="link",
                style={"text-decoration": "none"}), width=4),
        dbc.Col(
            dcc.Markdown('''
                         ### Parametric-based and automatized GIS application to calculate energy savings of the  building envelope: The energy losses produced by the exterior envelope of a building are generally 60% to  65% of the total [1,2]. 
                         '''), width=8),
    ]),
], style={'backgroundColor': '#fcfcfc'}, className=['mx-5', 'diagonal-pattern']
)

layout_playground = dbc.Row(
    dbc.Col([
        dbc.Row(
            dcc.Graph(id='city_mapbox', figure={}, clickData={'points': []}, config={'displayModeBar': False}),
            style={'height': '50vh'}),
        dbc.Row([
            dbc.Col(
                dbc.Row([
                    html.P('''
                    One main action to transform buildings to nZEB is the structural improvement of the elements of 
                    the exterior envelope [3].
                    '''),
                    dcc.Graph(id='graph_edad', figure={}, config={'displayModeBar': False}),
                ]), width=4),
            dbc.Col(
                dbc.Row([
                    html.P('''Although research on the topic is scant, preliminary work provides some support for 
                    cadastral data processing using GIS in energy efficiency issues [5]. Although research on the topic is scant, 
                    '''),
                    dcc.Graph(id='graph_stacked', figure={}, config={'displayModeBar': False}),
                ]),
                width=8),
        ], style={'height': '50vh'}),
    ]),
    style={'backgroundColor': '#fcfcfc'}, className=['mx-5', 'diagonal-pattern'])

layout_workflow = dbc.Container([
    html.H2("Related Analysis", id='title_lines', className="my-3 mx-5"),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-smalest"),
                            href="#",
                            id='card-image-1'
                            # data-toggle="modal",
                            # data-target="#myModal",
                        ),
                        dbc.CardBody(
                            [
                                html.H5("Architecture Driven by Data",
                                        className="card-title"),
                                dbc.Badge("In Progress",
                                          color="info"),
                                html.P(
                                    "Contemporary architecture is transformed by data-driven decision-making, harmonizing aesthetics and practicality to create structures that resonate with the modern world."),
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
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (2).jpg",
                                        top=True, alt="...", className="card-img-smalest"),
                            href="#",
                            id='card-image-2'
                        ),
                        dbc.CardBody(
                            [
                                html.H5("Explorative Non Real Spaces",
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
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (4).jpg",
                                        top=True, alt="...", className="card-img-smalest"),
                            href="#",
                            id='card-image-3'
                        ),
                        dbc.CardBody(
                            [
                                html.H5("Data Driven Approach to Urban Analysis",
                                        className="card-title"),
                                html.P(
                                    "Urban analysis has evolved with a data-driven approach, enabling city planners to make informed choices for infrastructure, transportation, and public spaces, ultimately fostering the development of more sustainable and habitable cities."),
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
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (3).jpg",
                                        top=True, alt="...", className="card-img-smalest"),
                            href="#",
                            id='card-image-4'
                        ),
                        dbc.CardBody(
                            [
                                html.H5("Large Scale Deployment for Generative Prototyping",
                                        className="card-title"),
                                html.P(
                                    "Leverages generative design to swiftly explore and implement groundbreaking architectural solutions on a grand scale, ensuring adaptability and innovation in urban development."),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
                # width=3
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),
], fluid=True,
)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    layout_workflow_explanation,
    layout_playground,
    # layout_workflow,
    layout_footer
])
