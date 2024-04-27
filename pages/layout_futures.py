import dash
from dash import dash_table
# import dash_table


from apps.test_data import df
from pages.pages_helper.layout_modals import *
from pages.pages_helper.layout_default import layout_footer, layout_stepper, sidebar, layout_header, layout_notifications
from pages.layout_chat import layout_modal_help
from apps.futures_figures import fig_normal, fig_cum

dash.register_page(__name__, path="/futures")

selector_grid = dbc.Collapse(dbc.Row([
    dbc.Col([
        html.Label('Slider 1', id='slider1-label'),
        dcc.Dropdown(
            id='dropdown_analysis_id',
            options=[
                {'label': 'Facade Sun Radiation', 'value': 'static/images/energy_saving8.png'},
                {'label': 'Shadow Overcast Time', 'value': 'static/images/energy_saving7.png'},
                {'label': 'Morning/Afternoon Sun Radiation',
                 'value': 'static/images/energy_saving6.png'},
                {'label': 'Density', 'value': 'static/images/energy_saving5.png'},
                {'label': 'Views Availability', 'value': 'static/images/city_density4.png'},
                {'label': 'Age of the Building', 'value': 'static/images/city_density3.png'},
                {'label': 'Urban Noise', 'value': 'static/images/city_density2.png'},
                {'label': 'Close Distance to Green/Walking Areas', 'value': 'static/images/energy_saving.png'},
                {'label': 'Potential Cost Reduction Using Solar Energy', 'value': 'static/images/energy_saving2.png'},
                {'label': 'Social Life', 'value': 'static/images/city_territorial.png'},
                {'label': 'Territorial Connection', 'value': 'static/images/energy_saving3.png'},
                {'label': 'Air Pollution', 'value': 'static/images/city_density.png'},
            ],
            value='static/images/energy_saving8.png',
            style={'margin-top': '1rem',
                   'margin-right': '1rem'}
        ),
        dcc.Dropdown(
            id='dropdown_analysis_id2',
            options=[
                {'label': 'Facade Sun Radiation', 'value': 'static/images/energy_saving8.png'},
                {'label': 'Shadow Overcast Time', 'value': 'static/images/energy_saving7.png'},
            ],
            value='static/images/energy_saving7.png',
            style={'margin-top': '1rem',
                   'margin-right': '1rem'}
        ),
        dcc.Markdown(
            """
            Morning/Afternoon Sun Radiation: The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to a node that is connected to the internet. The node sends the data to a server that stores the data.
            """),
    ], style={'margin-top': '1rem', 'margin-right': '1rem'}
    ),
    # TODO: Create the collapsable bar like in speckle vsc
    dbc.Col([
        html.Label('Slider 1', id='slider1-label'),
        dcc.RangeSlider(
            id='slider_analysis_id',
            min=-1,
            max=1,
            step=0.1,
            value=[-0.5, 0.5],
            marks={i / 10: str(i / 10) for i in range(-10, 11)}
        ),
        html.Label('Slider 2', id='slider2-label'),
        dcc.RangeSlider(
            id='slider_analysis_id2',
            min=-1,
            max=1,
            step=0.2,
            value=[-0.5, 0.5],
            marks={i / 10: str(i / 10) for i in range(-10, 11)}
        ),
        html.Label('Slider 3', id='slider2-label'),
        dcc.Slider(
            id='slider_analysis_id2',
            min=0,
            max=10,
            step=1,
            value=5,
            marks={i: str(i) for i in range(0, 11)}
        ),
    ], style={'margin-top': '1rem', 'margin-right': '1rem'}),
    dbc.Col([
        # html.Label('Slider 1', id='slider1-label'),
        dbc.Row([
            html.Label('Description of the Analysis:'),
            dbc.Col(
                dcc.Graph(id='normal_distribution', figure=fig_normal)
            ),
            dbc.Col(
                dcc.Graph(id='cumulative_distribution', figure=fig_cum)
            ),
        ]),
    ], style={'margin-top': '1rem', 'margin-right': '1rem'}),
    html.Hr(),
], style={'--bs-gutter-x': '0rem', 'z-index': '9999'}, className="mx-5")
    , id='collapse', is_open=True, style={'position': 'fixed', 'z-index': '9999', 'top': '3.4rem', 'width': '100%',
                                          'background-color': 'white'})

layout_details = dbc.Container([

    html.H2("Key Measurement Indicators",
            id='title_lines', className="my-3 mx-5"),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Large Scale Deployment for Generative Prototyping",
                                    className="card-title"),
                            html.P(
                                "The goal of this project is to create a digital twin of a real object, using sensors that capture information about its state and behavior. In this case, the real object is a digital twin model that represents the location of the sensors in space. \n The sensors can measure different environmental variables such as temperature, humidity, lighting, or noise. An Arduino and a Raspberry Pi are used to transmit the sensor data to the digital twin."),
                        ]
                    ),

                    # ],
                    className="h-100"
                ),
                # width=3
            ),
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
                # width=3
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),
], fluid=True,
)

layout_map_dash_deck = dbc.Container([
    html.H2("My Assets In Detail View", className="my-3 mx-5"),
    dbc.Row([
        dbc.Col([
            html.Span('Description of the Analysis:'),
            dcc.Markdown("""
    The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to a node that is connected to the internet. The node sends the data to a server that stores the data. The data is then processed and visualized in the dashboard. The dashboard is updated every 5 minutes."""),
            dbc.Card(
                html.Div(id='layout_dash_deck', className="map-size"),
                # html.Iframe(
                # src="https://speckle.xyz/embed?stream=df13255f81&commit=0c61f52341&c=%5B-918.70498%2C1182.48981
                # %2C125.07711%2C-998.06%2C1136.40997%2C21%2C1%2C0.5987369392383786%5D&transparent=true&autoload=true&hidecontrols=true&noscroll=true&hidesidebar=true&hideselectioninfo=true",
                # className="map-size"),
            ),
            dcc.Markdown(
                """**Figure 1.** Map of the selected assets."""),
        ], width=8
        ),
        dbc.Col([
            html.Span('Top Assets In Spain Performing the Current Analysis:'),
            dcc.Markdown("""
    The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to a node that is connected to the internet."""),
            dbc.Card(dcc.Graph(id='blank_map', figure={})),
            # dcc.Graph(id='subplot_div', figure={}),
            dcc.Markdown("""**Figure 1.** Bar chart about the current performance of the assets globally."""),
            dcc.Markdown(congrats_conclusion)], width=4),
    ], className="my-4 mx-5"),
    dbc.Row([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
        ),
        dcc.Markdown("""**Figure 1.** Table about testing data."""),
    ], className="my-4 mx-5"),
    dbc.Row([
        html.Span('Top Assets In Spain Performing the Current Analysis:'),
        dcc.Markdown("""
        The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to a node that is connected to the internet. The node sends the data to a server that stores the data. The data is then processed and visualized in the dashboard. The dashboard is updated every 5 minutes."""),
        dcc.Graph(id='subplot_div_assets', figure={}),
        dcc.Markdown("""**Figure 1.** Bar chart about the current performance of the assets globally."""),
        # dcc.Markdown(congrats_conclusion),
    ], className="my-4 mx-5"),
    dbc.Row(
        dcc.Markdown(congrats_conclusion), className="my-4 mx-5"),
],
    fluid=True)

# TODO: Probably this should be a modal -> Then delete the layout_helper
layout_iframe_speckle = dbc.Container([
    html.H2('Analytical Model Sample'),
    dcc.Markdown("""
        The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to a node that is connected to the internet. The node sends the data to a server that stores the data. The data is then processed and visualized in the dashboard. The dashboard is updated every 5 minutes."""),
    dbc.Card(
        html.Iframe(
            src="https://speckle.xyz/embed?stream=df13255f81&commit=0c61f52341&c=%5B-918.70498%2C1182.48981%2C125"
                ".07711%2C-998.06%2C1136.40997%2C21%2C1%2C0.5987369392383786%5D&transparent=true&autoload=true"
                "&hidecontrols=true&noscroll=true&hidesidebar=true&hideselectioninfo=true", className="map-size")),
], className="my-4 mx-5")

layout_helper = dbc.Container([

    html.H2("In Depth Contact", id='title_helpers', className="my-3 mx-5"),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Experience",
                                    className="card-title"),
                            html.P(
                                "Go-to resource for entering the world of collaborative software development on "
                                "GitHub, providing essential tools and insights to kickstart your coding projects.",
                                className="card-text"),
                            dbc.Button(">>", id='helper-button-1',
                                       color="primary", href="#", size="sm"),
                        ]
                    ), className="h-100"
                ),
                # width=6,
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Articles Published",
                                    className="card-title"),
                            html.P(
                                "Repository of your expertise and ideas, featuring a collection of insightful and "
                                "informative articles you've shared with the world.",
                                className="card-text"),
                            dbc.Button(">>", id='helper-button-2',
                                       color="primary", href="#", size="sm"),
                        ]
                    ), className="h-100"
                ),
                # width=6,
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Credits and Acknowledgements",
                                    className="card-title"),
                            html.P(
                                "Invaluable contributions of individuals and teams who have been instrumental in "
                                "shaping your projects, fostering a culture of gratitude and collaboration.",
                                className="card-text"),
                            # dbc.Button("Watch list",
                            #            color="primary", href="#"),
                        ]
                    ), className="h-100"
                ),
                # width=6,
            ),
        ],
        className="my-4 mx-5"
    )
], fluid=True)

layout_popup = dbc.Row([
    dbc.Popover(
        [
            # dbc.PopoverHeader("Popover title"),
            dbc.PopoverBody(
                "The Wake Up Services for Previews allows you test the functionalities of some of the services that we develop in the Wake Up Lab. These services are anonimized and are not connected to any of the real data."),
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
                "The Lines of Interest defines the main topics that we are currently working on. These topics are related to the research that we are developing in the Wake Up Lab."),
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
                "This sections makes tribute to the people that have been instrumental in shaping your projects, fostering a culture of gratitude and collaboration."),
        ],
        id="popover",
        target="title_helpers",  # needs to be the same as the Button's id
        trigger="hover",
        placement='bottom-start'
    ),
])

layout_stepper = dmc.Container(
    children=[
        dcc.Store(id='stepper-state', storage_type='session'),
        dmc.Stepper(
            id="stepper-custom-icons",
            active=2,
            breakpoint="sm",
            children=[
                dmc.StepperStep(
                    label="First step",
                    description="Select an analysis",
                    # icon=get_icon(icon="material-symbols:account-circle"),
                    # progressIcon=get_icon(icon="material-symbols:account-circle"),
                    # completedIcon=get_icon(icon="mdi:account-check"),
                    children=[
                        dmc.Text("Step 1 content: Create an account", align="center")
                    ],
                ),
                dmc.StepperStep(
                    label="Second step",
                    description="Search meaningful data",
                    # icon=get_icon(icon="ic:outline-email"),
                    # progressIcon=get_icon(icon="ic:outline-email"),
                    # completedIcon=get_icon(icon="material-symbols:mark-email-read-rounded"),
                    children=[dmc.Text("Step 2 content: Verify email", align="center")],
                ),
                dmc.StepperStep(
                    label="Final step",
                    description="Save the report",
                    # icon=get_icon(icon="material-symbols:lock-outline"),
                    # progressIcon=get_icon(icon="material-symbols:lock-outline"),
                    # completedIcon=get_icon(icon="material-symbols:lock-open-outline"),
                    children=[
                        dmc.Text("Step 3 content: Get full access", align="center")
                    ],
                ),
                dmc.StepperCompleted(
                    children=[
                        dmc.Text(
                            "Completed, click back button to get to previous step",
                            align="center",
                        )
                    ]
                ),
            ],
        ),
        dmc.Group(
            position="center",
            mt="xl",
            children=[
                dmc.Button("Back", id="back-custom-icons", variant="default"),
                dmc.Button("Next step", id="next-custom-icons"),
            ],
        ),
    ]
)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    layout_header,
    sidebar,
    html.Div(style={'height': '3.4rem'}),
    selector_grid,
    layout_details,
    layout_map_dash_deck,
    layout_modal_help,
    # layout_iframe_speckle,
    # layout_helper,
    layout_stepper,
    layout_popup,
    layout_notifications,
    layout_footer
])
