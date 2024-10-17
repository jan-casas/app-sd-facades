import dash
import dash_mantine_components as dmc
from dash import dash_table

from views.load_assets.load_assets import filtered_building_data, fig
from views.default.layout_chat import layout_modal_help
from views.default.layout_default import layout_header, sidebar  # ,
from views.default.layout_modals import *
from views.discover_assets.performance import kde_cdf_fig

dash.register_page(__name__, path="/performance")


def create_layout_figures():
    return dbc.Container([
        dbc.Row([
            html.H3("Statistical Analysis of the Assets", ),
            dcc.Markdown("""
            The analysis is based on the data of the sensors that are installed in the building. The
            sensors are connected to a node that is connected to the internet. The node sends the 
            data
            to a server that stores the data. The data is then processed and visualized in the 
            dashboard.
            """),
            dcc.Graph(id='kde_cdf_fig', figure=kde_cdf_fig, config={'displayModeBar': False}),
            dcc.Markdown("""**Figure 3.** Table about testing data.""")
        ], className="my-4 mx-5"),
    ], fluid=True)


layout_table = dbc.Container([
    html.H2("Performance of your Assets", className="my-3 mx-5"),
    dbc.Row([
        dcc.Markdown("""
        The Performance of your Assets section provides a comprehensive overview of the
        performance of the selected assets. The analysis is based on the data obtain on a hight 
        performance urban model. The data is processed and visualized in the dashboard. 
        """
                     ),
        dcc.Dropdown(
            id='analysis_options',
            multi=True,
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'Sunlight', 'value': 'Sunlight'},
                {'label': 'Temperature', 'value': 'Temperature'},
                {'label': 'Occupancy', 'value': 'Occupancy'}
            ],
            placeholder='Select analysis options',
        ),
    ], className="my-4 mx-5"
    ),
    dbc.Row([
        html.H3('Asset location'),
        dcc.Markdown("""
            The map displays various housing locations promoted by the company, marked with 
            distinct points. Each point 
            represents a specific housing location and is color-coded based on the type of 
            property (e.g., apartments, 
            townhouses, single-family homes). The map includes key information such as the name 
            of the housing development, 
            address, and availability status. Interactive features allow users to click on each 
            point for detailed descriptions, 
            images, pricing, and contact information. Major roads, landmarks, and amenities are 
            also highlighted for better 
            orientation and context."""
                     ),
        # html.Iframe(src="https://speckle.xyz/streams/df13255f81/commits/0c61f52341",
        # style={"width": "100%", "height": "400px"}),
        dcc.Graph(id='load_assets', figure=fig),

        # Add inputs to insert new points
    ], className="my-4 mx-5"),
    dbc.Row([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in filtered_building_data.columns],
            data=filtered_building_data.to_dict('records'),
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
        dcc.Markdown(
            """**Figure 1.** Location of the discover_assets."""),
    ], className="my-4 mx-5"),
],
    fluid=True)


def create_card(title, text, color, inverse=False, badge_text=None, badge_color=None,
                description=None):
    card_content = [
        dbc.Col(dbc.Card(
            [
                html.H2(title, className="card-title"),
                html.H2(text, className="card-text", style={'color': 'white'} if inverse else {}),
            ],
            body=True,
            color=color,
            inverse=inverse,
        ), width='50%'),
        dbc.CardBody(
            [
                html.H5(description, className="card-title") if description else None,
                dbc.Badge(badge_text, color=badge_color) if badge_text else None,
                html.P(description) if description else None,
            ]
        ),
    ]
    return dbc.Card(card_content, className="h-100")


def assets_conclusion_cards():
    return dbc.Row(
        [
            dbc.Col(create_card("Temperatura:", "Es de 27ºC", "dark", inverse=True,
                                badge_text="In Progress", badge_color="info",
                                description="Temperature Thermal Comfort")),
            dbc.Col(create_card("Ocupación:", "Es del 20%", "light",
                                description="Ocupancy and Density")),
            dbc.Col(create_card("Responsividad:", "Es de 1.2s", "light",
                                description="Climatic Responsive Design")),
            dbc.Col(create_card("Performance:", "Está al 95%", "light",
                                description="Installation Performance")),
        ],
        className="my-4 mx-5"
    )


layout_conclusion_performance = dbc.Container([
    dbc.Row([
        html.H3('Conclusion Performance Assets'),
        dcc.Markdown("""
            The analysis is based on the data of the sensors that are installed in the building. The
            sensors are connected to a node that is connected to the internet. The node sends the 
            data
            to a server that stores the data. The data is then processed and visualized in the 
            dashboard.
            The graphs below provide detailed metrics for the selected discover_assets, 
            enabling a 
            comprehensive evaluation to determine the perfect asset for your specific needs. This 
            analysis incorporates advanced 3D models and real-time environmental data, ensuring 
            accuracy and relevance. The data is meticulously processed and then visualized within 
            an interactive dashboard, offering intuitive insights. Additionally, the dashboard 
            allows for customized filtering and comparison of discover_assets, empowering 
            users to make 
            informed decisions based on their unique criteria and objectives.
            """),
    ], className="my-4 mx-5"),
    assets_conclusion_cards(),
    dbc.Row([
        dcc.Markdown(congrats_conclusion),
        # dbc.Row(
        #     dbc.Button(
        #         children=html.H6('Download Report'),
        #         id='continue-discover',
        #         # color="primary",
        #         style={
        #             'height': '60px', 'lineHeight': '60px',
        #             'borderWidth': '1px', 'borderStyle': 'dashed',
        #             'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px',
        #             'width': '45%'
        #         },
        #         className="my-4 diagonal-pattern"
        #     ), className="my-4 mx-5 justify-content-end"
        # ),
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
        ),
    ], className="my-4 mx-5"),
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

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    layout_header,
    sidebar,
    html.Div(style={'height': '3.4rem'}),
    # selector_grid,
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            layout_table,
            # TODO: WHEN CLICK ON TABLE, PLOT VERTICAL LINES SHOWING THE POSITION OF THE ASSET
            create_layout_figures(),
            layout_conclusion_performance
        ]),
    layout_modal_help,
    layout_stepper,
    layout_popup,
    # layout_notifications,
    # layout_footer
])
