import dash
from pages.pages_helper.layout_modals import *
from pages.pages_helper.layout_default import sidebar, layout_footer, layout_header, \
    layout_notifications
from pages.pages_helper.descriptions import *
from pages.layout_chat import layout_modal_help
import dash_mantine_components as dmc

dash.register_page(__name__, path="/home")

layout_modal = html.Div([
    dbc.Modal([
        dbc.ModalHeader([
            html.Div([

                html.Div([
                    html.H2(id='modal_title'),
                    html.P(id='card_description'),
                    html.Span('Description of the Analysis:'),
                    dcc.Markdown(id='modal_description'),
                    dcc.Store(id='card_image', storage_type='session'),
                ], style={'marginLeft': '20px', 'textAlign': 'left'})
            ], id='grid-item-1', className='grid-item',
                style={'display': 'flex', 'alignItems': 'center', 'margin-left': '40px', 'margin-right': '40px',
                       'margin-top': '40px', 'margin-bottom': '15px'}),
        ], style={'padding': '0px', 'margin': '0px'}, close_button=False, id='modal-header'
        ),
        # Responsive information
        dcc.Loading(
            id="loading",
            type="dot",
            fullscreen=False,
            children=[
                dbc.ModalBody(id='modal-body', children=[],
                              style={'padding': '0px', 'margin': '0px'}),
            ]),
    ], id='modal', size='xl', scrollable=True, is_open=False,
        style={'width': '100%', 'height': '100%', 'padding': '0px', 'margin': '0px'}),
])

layout_details = dbc.Container([

    html.H2("New Releases", id='title_lines', className="my-3 mx-5"),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=facade_sun_radiation['image'], top=True,
                                        alt="...", className="card-img-smallest"),
                            href="#",
                            id=facade_sun_radiation['id']
                            # data-toggle="modal",
                            # data-target="#myModal",
                        ),
                        dbc.CardBody(
                            [
                                html.H5(facade_sun_radiation['title'],
                                        className="card-title"),
                                dbc.Badge(facade_sun_radiation['badge'],
                                          color="info"),
                                html.P(
                                    facade_sun_radiation['card_introduction']),
                            ]
                        ),
                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=shadow_overcast_time['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id=shadow_overcast_time['id']
                        ),
                        dbc.CardBody(
                            [
                                html.H5(shadow_overcast_time['title'],
                                        className="card-title"),
                                dbc.Badge(shadow_overcast_time['badge'],
                                          color="warning"),
                                html.P(shadow_overcast_time['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=morning_afternoon_sun_radiation['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id=morning_afternoon_sun_radiation['id']
                        ),
                        dbc.CardBody(
                            [
                                html.H5(morning_afternoon_sun_radiation['title'],
                                        className="card-title"),
                                html.P(morning_afternoon_sun_radiation['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=density['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id=density['id']
                        ),
                        dbc.CardBody(
                            [
                                html.H5(density['title'],
                                        className="card-title"),
                                dbc.Badge(density['badge'],
                                          color="warning"),
                                html.P(density['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row
    ),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=views_availability['image'], top=True,
                                        alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-5'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(views_availability['title'],
                                        className="card-title"),
                                html.P(views_availability['card_introduction']),
                            ]
                        ),
                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=age_of_building['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-6'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(age_of_building['title'],
                                        className="card-title"),
                                html.P(age_of_building['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=urban_noise['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-7'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(urban_noise['title'],
                                        className="card-title"),
                                dbc.Badge(urban_noise['badge'],
                                          color="info"),
                                dbc.Badge('Updated',
                                          color="danger"),
                                html.P(urban_noise['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=close_distance_to_green_areas['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-8'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(close_distance_to_green_areas['title'],
                                        className="card-title"),
                                html.P(close_distance_to_green_areas['card_introduction']),
                            ]
                        ),

                    ],
                    className="h-100"
                ),
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=potential_cost_reduction_solar_energy['image'], top=True,
                                        alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-9'
                            # data-toggle="modal",
                            # data-target="#myModal",
                        ),
                        dbc.CardBody(
                            [
                                html.H5(potential_cost_reduction_solar_energy['title'],
                                        className="card-title"),
                                dbc.Badge("In Progress",
                                          color="info"),
                                html.P(potential_cost_reduction_solar_energy['card_introduction']),
                            ]
                        ),
                    ],
                    className="h-100"
                ),
            ),
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src=social_life['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-10'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(social_life['title'],
                                        className="card-title"),
                                html.P(social_life['card_introduction']),
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
                            dbc.CardImg(src=territorial_connection['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-11'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(territorial_connection['title'],
                                        className="card-title"),
                                html.P(territorial_connection['card_introduction']),
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
                            dbc.CardImg(src=air_pollution['image'],
                                        top=True, alt="...", className="card-img-smallest"),
                            href="#",
                            id='card-image-12'
                        ),
                        dbc.CardBody(
                            [
                                html.H5(air_pollution['title'],
                                        className="card-title"),
                                html.P(air_pollution['card_introduction']),
                            ]
                        ),
                    ],
                    className="h-100"
                ),
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),
], fluid=True,
)

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
                "The Wake Up Services for Previews allows you test the functionalities of some of the services that "
                "we develop in the Wake Up Lab. These services are anonimized and are not connected to any of the "
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
                "The Lines of Interest defines the main topics that we are currently working on. These topics are "
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
                "This sections makes tribute to the people that have been instrumental in shaping your projects, "
                "fostering a culture of gratitude and collaboration."),
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
            active=0,
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
    # layout_header,
    dcc.Location(id='url', refresh=True),
    layout_header,
    sidebar,
    html.Div(style={'height': '3.4rem'}),
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            layout_details,
            layout_stepper,
            layout_helper
        ]),
    layout_modal,
    layout_modal_help,
    layout_popup,
    layout_notifications,
    layout_footer
])
