import dash
import dash_mantine_components as dmc
from dash import dash_table

from views.default.layout_chat import layout_modal_help
# layout_notifications
from views.default.descriptions import *
from views.default.layout_default import sidebar, layout_header  # ,
from views.default.layout_modals import *
from views.load_assets.load_assets import df_real_state_original

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
                style={'display': 'flex', 'alignItems': 'center', 'margin-left': '40px',
                       'margin-right': '40px',
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
                            dbc.CardImg(src=potential_cost_reduction_solar_energy['image'],
                                        top=True,
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
                                "Go-to resource for entering the world of collaborative software "
                                "development on "
                                "GitHub, providing essential tools and insights to kickstart your "
                                "coding projects.",
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
                                "Repository of your expertise and ideas, featuring a collection "
                                "of insightful and "
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
                                "Invaluable contributions of individuals and teams who have been "
                                "instrumental in "
                                "shaping your projects, fostering a culture of gratitude and "
                                "collaboration.",
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
                     active=1,
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
                             children=[
                                 dmc.Text("Step 2/3: Select the desire analysis")],
                         ),
                         dmc.StepperStep(
                             label="Compare Results",
                             children=[
                                 dmc.Text(
                                     "Step 3/3: Compare the performances of your actives with the "
                                     "rest of the city")
                             ],
                         ),
                         dmc.StepperCompleted(
                             children=[
                                 dmc.Text(
                                     "Completed, click back button to get to previous step"
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

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

layout_types_analysis = dbc.Container(
    [
        html.H2("New Releases", id='home_title', className="my-4 mx-5"),
        html.Span('Description of the comparative tables:', className="my-4 mx-5"),
        dcc.Markdown("""The map displays various housing locations promoted by the company, 
        marked with distinct 
        points. Each point 
        represents a specific housing location and is color-coded based on the type of property (
        e.g., apartments, 
        townhouses, single-family homes). The map includes key information such as the name of 
        the housing development, 
        address, and availability status. Interactive features allow users to click on each point 
        for detailed 
        descriptions, 
        images, pricing, and contact information. Major roads, landmarks, and amenities are also 
        highlighted for better 
        orientation and context.""", className="my-4 mx-5"),
        dbc.Row([
            # Tabla analysis
            dbc.Col([
                dash_table.DataTable(
                    id='datatable-interactivity',
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": True} for i in
                        description_df[["title", "updated"]].columns
                    ],
                    data=description_df[["title", "updated"]].to_dict('records'),
                    editable=False,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    # column_selectable="single",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=20,
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(
                    """**Figure 1.** List of the available analysis."""),
            ]),
            # Table assets
            dbc.Col([
                dash_table.DataTable(
                    id='datatable-interactivity2',
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": True}
                        for i in
                        ['local_id', 'local_use', 'floor', 'year_construction', 'unit_cost']
                        if i in df_real_state_original.columns
                    ],
                    data=df_real_state_original.to_dict('records'),
                    editable=False,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=int(len(description_df.index)),
                ),
                dcc.Markdown(
                    """**Figure 2.** List of the existing assets."""),
            ]),
        ], className="my-4 mx-5"),

        html.Div(id='table_home_markdown', children=[], className="my-4 mx-5"),

    ], fluid=True)

layout = html.Div([
    layout_header,
    dcc.Location(id='url', refresh=True),
    layout_header,
    sidebar,
    html.Div(style={'height': '3.4rem'}),
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            layout_types_analysis,
            # layout_details,
            layout_stepper
        ]),
    layout_modal,
    layout_modal_help,
    layout_popup,
    # layout_notifications,
    # layout_footer
])

# TODO: Add SPeckle layout inside the explanatory markdown. Is a grid of cards with a description
#  and an speckle
#  embeded (like the
#  bulding iot examples that i did
