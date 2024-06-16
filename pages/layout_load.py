import dash
import pandas as pd
from dash import dash_table
# import dash_table
import dash_leaflet as dl
from apps.app_load_assets import df, fig
from pages.pages_helper.layout_modals import *
from pages.pages_helper.layout_default import layout_header, layout_footer, sidebar, layout_notifications
from pages.layout_chat import layout_modal_help
from apps.futures_figures import fig_normal, fig_cum
import dash_mantine_components as dmc

dash.register_page(__name__, path="/load")

selector_grid = dbc.Collapse(
    dbc.Row([
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
                    {'label': 'Potential Cost Reduction Using Solar Energy',
                     'value': 'static/images/energy_saving2.png'},
                    {'label': 'Social Life', 'value': 'static/images/city_territorial.png'},
                    {'label': 'Territorial Connection', 'value': 'static/images/energy_saving3.png'},
                    {'label': 'Air Pollution', 'value': 'static/images/city_density.png'},
                ],
                value='static/images/energy_saving8.png',
                style={'margin-top': '1rem',
                       'margin-right': '1rem'}
            ),
            dcc.Markdown(
                """
                Morning/Afternoon Sun Radiation: The analysis is based on the data of the sensors that are installed in 
                the building. The sensors are connected to a node that is connected to the internet. The node sends the 
                data to a server that stores the data. The data is then processed and visualized in the dashboard. The 
                dashboard is updated every 5 minutes.
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

layout_load_assets = dbc.Container([
    html.H2("My Assets In Map View", className="my-3 mx-5"),
    dbc.Row([
        html.Span('Description of the Map:'),
        dcc.Markdown("""
The map displays various housing locations promoted by the company, marked with distinct points. Each point 
represents a specific housing location and is color-coded based on the type of property (e.g., apartments, 
townhouses, single-family homes). The map includes key information such as the name of the housing development, 
address, and availability status. Interactive features allow users to click on each point for detailed descriptions, 
images, pricing, and contact information. Major roads, landmarks, and amenities are also highlighted for better 
orientation and context."""),
        # dl.Map(id='load_assets',
        #        children=[
        #            dl.TileLayer(),
        #            dl.GestureHandling()
        #        ], center=[56, 10], zoom=6
        #        ),
        dcc.Graph(id='load_assets', figure=fig),
        # html.Div(id='layout_dash_deck', className="map-size"),

        dcc.Markdown(
            """**Figure 1.** Location of the assets."""),
        # Add inputs to insert new points
    ], className="my-4 mx-5"),
    dbc.Row([
        # Existing assets in the database
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            editable=False,
            filter_action="native",
            filter_options={"placeholder_text": "Filter column..."},
            sort_action="native",
            sort_mode='multi',
            page_size=10,
            row_selectable="multi",
            selected_rows=[],
        ),
        dcc.Markdown("""**Figure 2.** Existing assets in the database."""),

        # Upload new data
        dash_table.DataTable(
            id='datatable-upload-container',
            editable=False,
            page_size=10,
            filter_action="native",
            # row_selectable="multi",
            # selected_rows=[],
            sort_action="native",
            sort_mode='multi',
        ),
        dcc.Upload(
            id='datatable-upload',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'height': '60px', 'lineHeight': '60px',
                'borderWidth': '1px', 'borderStyle': 'dashed',
                'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
            },
            className="my-4 mx-5"
        ),

        dcc.Markdown("""**Figure 3.** New assets to include in the database."""),

    ], className="my-4 mx-5"),

    # Conclusions
    dbc.Row(
        dcc.Markdown(congrats_conclusion), className="my-4 mx-5"),
],
    fluid=True)

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

layout_stepper = html.Footer([
    html.Div(id='grid-container_sub3',
             children=[
                 html.Br(),
                 html.Br(),
                 dcc.Store(id='stepper-state', storage_type='session'),
                 dmc.Stepper(
                     id="stepper-custom-icons",
                     active=0,
                     breakpoint="sm",
                     children=[
                         dmc.StepperStep(
                             label="Geolocate Actives",
                             children=[
                                 dmc.Text("Step 1/3: Load your actives", align="center")
                             ],
                         ),
                         dmc.StepperStep(
                             label="Select Analysis",
                             children=[dmc.Text("Step 2/3: Select the desire analysis", align="center")],
                         ),
                         dmc.StepperStep(
                             label="Compare Results",
                             children=[
                                 dmc.Text(
                                     "Step 3/3: Compare the performances of your actives with the rest of the city",
                                     align="center")
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
    selector_grid,
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            layout_load_assets
        ]),
    layout_modal_help,
    layout_stepper,
    layout_popup,
    layout_notifications,
    # layout_footer
])

# TODO: Here the selectors must filter the type of analysis only
# TODO: https://dash.plotly.com/datatable/editable (drag and drop; add row; export excel)
