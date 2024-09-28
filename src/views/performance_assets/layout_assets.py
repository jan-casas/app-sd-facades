import dash
import dash_mantine_components as dmc
from dash import dash_table
from views.default.layout_chat import layout_modal_help
from views.default.layout_default import layout_header, sidebar  # ,
from views.default.layout_modals import *
from src.views.performance_assets.performance import df_post_analysis, fig

# import dash_table

dash.register_page(__name__, path="/assets")

layout_map_dash_deck = dbc.Container([
    html.H2("Discover Long Term Profitable Assets", className="my-3 mx-5"),
    dbc.Row([
        html.H3('View Selected Assets'),
        dcc.Markdown("""    
        The graphs below provide detailed metrics for the selected performance_assets, enabling a 
        comprehensive 
        evaluation to determine the perfect asset for your specific needs. This analysis 
        incorporates 
        advanced 3D models and real-time environmental data, ensuring accuracy and relevance. 
        The data is 
        meticulously processed and then visualized within an interactive dashboard, offering 
        intuitive 
        insights. Additionally, the dashboard allows for customized filtering and comparison 
        of performance_assets, 
        empowering users to make informed decisions based on their unique criteria and 
        objectives.
        """),
        # Add parcoord graph
        dcc.Graph(id='parcoord_graph', figure=fig),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df_post_analysis.columns],
            data=df_post_analysis.to_dict('records'),
            # export_format='xlsx',
            # export_headers='display',
            # export_columns='all',
            editable=False,
            filter_action="native",
            filter_options={"placeholder_text": "Filter column..."},
            sort_action="native",
            sort_mode='multi',
            page_size=5,
            row_selectable="multi",
            selected_rows=[],
            style_table={'overflowX': 'scroll'},
        ),
        dcc.Markdown("""**Figure 2.** Table about testing data."""),

        # Conclusion of this section
        html.Span('Top Assets In Spain Performing the Current Analysis:'),
        dcc.Markdown("""
The analysis is based on the data of the sensors that are installed in the building. The sensors 
are 
connected to a node that is connected to the internet. The node sends the data to a server that 
stores the 
data. The data is then processed and visualized in the dashboard. The dashboard is updated every 
5 minutes."""),

    ], className="my-4 mx-5"),
],
    fluid=True)

layout_asset_comparative = dbc.Container([
    dbc.Row([
        html.Span('Top Assets In Spain Performing the Current Analysis:'),
        dcc.Markdown("""
    The analysis is based on the data of the sensors that are installed in the building. The 
    sensors are 
    connected to a node that is connected to the internet. The node sends the data to a server 
    that stores the 
    data. The data is then processed and visualized in the dashboard. The dashboard is updated 
    every 5 minutes."""),
        dcc.Graph(id='subplot_div_assets', figure={}),
        dcc.Markdown("""**Figure 2.** Bar chart about 
            the current performance of the performance_assets globally."""),
        # dcc.Markdown(congrats_conclusion),
    ], className="my-4 mx-5"),

],
    fluid=True)

layout_popup = dbc.Row([
    dbc.Popover(
        [
            # dbc.PopoverHeader("Popover title"),
            dbc.PopoverBody(
                "The Wake Up Services for Previews allows you test the functionalities of some of "
                "the services that "
                "we develop in the Wake Up Lab. These services are anonimized and are not "
                "connected to any of the "
                "real data."),
        ],
        id="popover",
        target="title_services",  # needs to be the same as the Button's id
        trigger="hover",
        placement='bottom-start'
    ),
    dbc.Popover(
        [
            # dbc.PopoverHeader("Popover title"),
            dbc.PopoverBody(
                "The Lines of Interest defines the main topics that we are currently working on. "
                "These topics are "
                "related to the research that we are developing in the Wake Up Lab."),
        ],
        id="popover",
        target="title_lines",  # needs to be the same as the Button's id
        trigger="hover",
        placement='bottom-start'
    ),
    dbc.Popover(
        [
            # dbc.PopoverHeader("Popover title"),
            dbc.PopoverBody(
                "This sections makes tribute to the people that have been instrumental in shaping "
                "your projects, "
                "fostering a culture of gratitude and collaboration."),
        ],
        id="popover",
        target="title_helpers",  # needs to be the same as the Button's id
        trigger="hover",
        placement='bottom-start'
    ),
])

layout_stepper = html.Footer([
    html.Div(id='grid-container_sub3',
             children=[
                 html.Br(),
                 html.Br(),
                 dcc.Store(id='stepper-state', storage_type='session'),
                 dmc.Stepper(
                     id="stepper-custom-icons",
                     active=2,
                     # breakpoint="sm",
                     children=[
                         dmc.StepperStep(
                             label="Geolocate Actives",
                             children=[
                                 dmc.Text("Step 1/3: Load your actives")
                             ],
                         ),
                         dmc.StepperStep(
                             label="Select Analysis",
                             children=[dmc.Text("Step 2/3: Select the desire analysis")],
                         ),
                         dmc.StepperStep(
                             label="Compare Results",
                             children=[
                                 dmc.Text(
                                     "Step 3/3: Compare the performances of your actives with the "
                                     "rest of the city", )
                             ],
                         ),
                         dmc.StepperCompleted(
                             children=[
                                 dmc.Text(
                                     "Completed, click back button to get to previous step",
                                 )
                             ]
                         ),
                     ],
                 ),
                 dmc.Group(
                     # position="center",
                     mt="xl",
                     children=[
                         dmc.Button("Back", id="back-custom-icons", variant="default"),
                         dmc.Button("Next step", id="next-custom-icons"),
                     ],
                 ),
             ],
             style={
                 'marginTop': '24px', 'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto'}
             ),
], style={'width': '100%', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '50px',
          'background-color': '#f7f7f8', 'height': '200px'})

layout_details = dbc.Container([

    html.H3("Key Measurement Indicators",
            id='title_lines', className="my-3 mx-5"),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        # dbc.Row([
                        # dbc.Col(dbc.Card(
                        #     [
                        #         html.H2("Humedad:",
                        #                 className="card-title"),
                        #         html.H2("Es del 50%",
                        #                 className="card-text"),
                        #     ],
                        #     body=True,
                        #     color="light",
                        # ), width='50%'),
                        dbc.Col(dbc.Card(
                            [
                                html.H2("Temperatura:",
                                        className="card-title"),
                                html.H2("Es de 27ºC",
                                        className="card-text", style={'color': 'white'}),
                            ],
                            body=True,
                            color="dark",
                            inverse=True,
                        ), width='50%'),

                        # ],
                        # className="card-img-small"
                        # ),
                        # html.A(
                        #     dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                        #                 alt="...", className="card-img-small"),
                        #     href="#",
                        #     id='card-image-1'
                        #     # data-toggle="modal",
                        #     # data-target="#myModal",
                        # ),
                        dbc.CardBody(
                            [
                                html.H5("Temperature Thermal Comfort",
                                        className="card-title"),
                                dbc.Badge("In Progress",
                                          color="info"),
                                html.P(
                                    "Contemporary architecture is transformed by data-driven "
                                    "decision-making, "
                                    "harmonizing aesthetics and practicality to create structures "
                                    "that resonate with "
                                    "the modern world."),
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
                                    "Explorative Non Real Spaces are digital canvases where "
                                    "designers are unshackled "
                                    "by the constraints of reality, enabling boundless creativity "
                                    "and the conception "
                                    "of visionary architectural concepts."),
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
                                    "Urban analysis has evolved with a data-driven approach, "
                                    "enabling city planners."),
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
                                    "Leverages generative design to swiftly explore and implement "
                                    "solutions."),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
                # width=3
            ),
        ],
        className="my-4 mx-5"
    ),
    # TODO: DEBERÍA SER UN GRID DE 4XN DONDE N ES EL NÚMERO DE TRAZOS SELECCIONADOS EN EL FILTRO.
    #  CADA MAPA HACIENDO ZOOM A LA LOCALIZACIÓN DEL ACTIVO.
    dbc.Row([
        dcc.Markdown("""
        The map displays various housing locations promoted by the company, marked with distinct 
        points. Each point 
        represents a specific housing location and is color-coded based on the type of property (
        e.g., apartments, 
        townhouses, single-family homes). The map includes key information such as the name of 
        the housing development, 
        address, and availability status. Interactive features allow users to click on each point 
        for detailed descriptions, 
        images, pricing, and contact information. Major roads, landmarks, and amenities are also 
        highlighted for better 
        orientation and context."""
                     ),
        dcc.Graph(id='load_assets', figure=fig),
        dcc.Markdown("""**Figure 1.** Map of the selected performance_assets."""),
        # html.Div(id='layout_dash_deck',className="my-3 mx-52),
        dcc.Markdown("""**Figure 2.** Map of the selected performance_assets."""),
    ], className="my-4 mx-5"),
    dbc.Row(
        [
            dcc.Markdown(congrats_conclusion),
            dcc.Upload(
                id='datatable-download',
                children=html.Div([
                    'Click and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'height': '60px', 'lineHeight': '60px',
                    'borderWidth': '1px', 'borderStyle': 'dashed',
                    'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
                }, className="my-4 mx-5"
            )
        ],
        className="my-4 mx-5"),

], fluid=True
)

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    layout_header,
    sidebar,
    html.Div(style={'height': '3.4rem'}),
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            layout_map_dash_deck,
            # create_layout_figures(),
            layout_details,
        ]),
    layout_modal_help,
    layout_stepper,
    layout_popup
])
