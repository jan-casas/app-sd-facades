import dash
from dash import dash_table
# import dash_table

from apps.test_data import df
from pages.pages_helper.layout_modals import *
from pages.pages_helper.layout_default import layout_header, layout_footer, sidebar, layout_notifications
from pages.layout_chat import layout_modal_help
from apps.futures_figures import fig_normal, fig_cum
import dash_mantine_components as dmc

dash.register_page(__name__, path="/assets")

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
                    {'label': 'Potential Cost Reduction Using Solar Energy', 'value': 'static/images/energy_saving2.png'},
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
                                          'background-color': 'white'}
)

layout_map_dash_deck = dbc.Container([
    html.H2("My Assets In Detail View", className="my-3 mx-5"),
    dbc.Row([
        html.Span('Description of the Analysis:'),
        dcc.Markdown("""
The analysis is based on the data of the sensors that are installed in the building. The sensors are connected to 
a node that is connected to the internet. The node sends the data to a server that stores the data. The data is 
then processed and visualized in the dashboard. The dashboard is updated every 5 minutes."""),
        dbc.Card(
            html.Div(id='layout_dash_deck', className="map-size"),
        ),
        dcc.Markdown(
            """**Figure 1.** Map of the selected assets."""),
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
        The analysis is based on the data of the sensors that are installed in the building. The sensors are 
        connected to a node that is connected to the internet. The node sends the data to a server that stores the 
        data. The data is then processed and visualized in the dashboard. The dashboard is updated every 5 minutes."""),
        dcc.Graph(id='subplot_div_assets', figure={}),
        dcc.Markdown("""**Figure 2.** Bar chart about 
                the current performance of the assets globally."""),
        # dcc.Markdown(congrats_conclusion),
    ], className="my-4 mx-5"),
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
                     active=2,
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
                                 dmc.Text("Step 3/3: Compare the performances of your actives with the rest of the city", align="center")
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
            # layout_details,
            layout_map_dash_deck
        ]),
    layout_modal_help,
    layout_stepper,
    layout_popup,
    layout_notifications,
    # layout_footer
])
