import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from pages.layout_modals import *
from pages.layout_default import layout_header
from pages.layout_grid import grid_option_1


dash.register_page(__name__, path="/")


layout_intro = dbc.Row([
    html.Hr(),
    html.Hr(),
    html.Hr(),
    html.Hr(style={'height': '0px'}),

    dbc.Row([
        dbc.Col(
            dbc.Button(
                dcc.Markdown(''' 
    # Introduction
    ''', id='title_intro'),
                id='button_intro',
                color="link",
                style={"text-decoration": "none"},
            )),
        dbc.Col(
            dcc.Markdown('''
                         ## Overall, this project represents a cutting-edge approach to urban analysis, blending modern technology to assess and enhance the quality of urban environments. It aims to contribute significantly to the development of urban areas that are not only functional but also enrich the lives of their inhabitants.
                         '''),
        ),
    ]),
], className="mx-5"
)

layout_intro_modal = dbc.Modal([
    dbc.ModalHeader("# Introduction"),
    dbc.ModalBody(dcc.Markdown('''


    This project focuses on extracting data from a 3D urban model to evaluate the urban quality of a city, using advanced technologies like parametric modeling, data handling, geometric database management, and stable diffusion processes. Its aim is to provide a thorough analysis of various factors that contribute to urban quality. Here's an overview of the project:

    1. **Objective of Urban Quality Assessment**: The primary aim is to extract and analyze data from a 3D urban model, which involves a detailed examination of elements like the alignment of streets and buildings, the diversity of views (including sky, land, roads, and buildings), and the patterns of sunlight exposure throughout the city. This comprehensive analysis helps in understanding the environmental, architectural, and spatial dynamics that significantly impact the city's urban quality.

    2. **Technological Framework**: The project employs a range of sophisticated technologies to achieve its goals:
    - **Parametric Modeling**: This is used for dynamic and efficient manipulation and analysis of the urban model, enabling a flexible approach to urban design.
    - **Data Handling**: Advanced methods are implemented for managing and interpreting the large volumes of data generated from the urban model.
    - **Geometric Database Management**: This involves using state-of-the-art database systems to effectively store, retrieve, and manipulate geometric data.
    - **Stable Diffusion Processes**: Incorporating stable diffusion allows for the visualization of potential improvements in the urban landscape, creating hypothetical images or designs that depict how these enhancements could materialize.

    3. **Expected Outcomes**: By employing these technologies and analyzing critical aspects of urban design, the project aims to provide valuable insights and visualizations. These can inform urban planning and design strategies, leading to improvements in urban quality. The focus is on making data-driven decisions to enhance the livability, sustainability, and aesthetic appeal of urban spaces.

    Overall, this project represents a cutting-edge approach to urban analysis, blending modern technology to assess and enhance the quality of urban environments. It aims to contribute significantly to the development of urban areas that are not only functional but also enrich the lives of their inhabitants.

    Enjoy exploring the application!
    '''), className='modal-body-modals'),
], id='modal_intro', is_open=False, size='lg')


layout_matrix = dbc.Container([

    dbc.Row(
        [
            dbc.Col(
                html.H2("Resulted Matrix and Statistical Data", id='title_services', className="mx-5",
                        style={'margin-right': '1rem'}),
            ),
            dbc.Col(
                dcc.Dropdown(
                    id='dropdown',
                    options=[
                        {'label': 'Previous Analysis   ',
                         'value': 'option1'},
                        {'label': html.Span(['Functionalities Used in Research  ', dbc.Badge(
                            "In Progress", color="info")]), 'value': 'option2'}
                    ],
                    value='option1',
                    className="mx-5",
                    style={'margin-right': '1rem'}
                )
            ),
        ], style={'--bs-gutter-x': '0rem'}
    ),

    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
                        href="#",
                        id='card-image-1'

                    ),
                    dbc.CardBody(
                        [
                            html.H5("Architecture Driven by Data",
                                    className="card-title"),
                            html.P(
                                "Contemporary architecture is transformed by data-driven decision-making, harmonizing aesthetics and practicality to create structures that resonate with the modern world."),
                        ]
                    ),
                ],
                className="h-100"
            ),
            # width=3
        ),
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
                        href="#",
                        id='card-image-3'

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
                        dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
                        href="#",
                        id='card-image-3'

                    ),
                ],
                className="h-100"
            ),
            # width=3
        ),
    ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),
],    fluid=True,
)


layout_modal = html.Div([
    dbc.Modal([
        dbc.ModalHeader([
            html.Div([

                        html.Div([
                            html.H3(
                                id='modal-title', children='Architecture Driven by Data'),
                            html.P(
                                "Contemporary architecture is transformed by data-driven decision-making, harmonizing aesthetics and practicality to create structures that resonate with the modern world.", id='modal-description'),
                        ], style={'marginLeft': '20px', 'textAlign': 'left'})
                        ], id='grid-item-1', className='grid-item', style={'display': 'flex', 'alignItems': 'center', 'margin-left': '40px', 'margin-right': '40px', 'margin-top': '40px', 'margin-bottom': '15px'}),
        ], style={'padding': '0px', 'margin': '0px'}, close_button=False, id='modal-header'
        ),
        dbc.Row([
            html.P('Please tell us the orientation of the building where you live. This information is important for us to understand the amount of sunlight and shade your building receives throughout the day.'),
            html.Span('Buscar lo que más se adapte a tus necesidades:'),

        ], style={'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '16px', 'margin-top': '20px'}),

        # Responsive information
        dbc.ModalBody(id='modal-body', children=[],
                      style={'padding': '0px', 'margin': '0px'}),

    ], id='modal', size='lg', scrollable=True, is_open=False, style={'width': '100%', 'height': '100%', 'padding': '0px', 'margin': '0px'}),
])

selector_grid = dbc.Row(
    [
        dbc.Col(
            html.H2("Wake Up Services for Preview", id='title_services', className="mx-5",
                    style={'margin-top': '4rem', 'margin-right': '1rem'}),
        ),
        # dbc.Col(className="mx-2", style={'margin-top': '5rem'}),
        dbc.Col(
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Previous Services Used in Projects   ',
                     'value': 'option1'},
                    {'label': html.Span(['Functionalities Used in Research  ', dbc.Badge(
                        "In Progress", color="info")]), 'value': 'option2'}
                ],
                value='option1',
                className="mx-5",
                style={'margin-top': '4rem',
                       'margin-right': '1rem'}
            )
        ),
    ], style={'--bs-gutter-x': '0rem'}
)


layout_grid = dbc.Container(children=grid_option_1,
                            id='grid_selector_id', fluid=True)


layout_workflow_explanation = dbc.Row([
    html.Hr(),
    dbc.Row([
        dbc.Col(
            dbc.Button(
                dcc.Markdown(''' 
    # Workflow Explanation
    ''', id='title_workflow'),
                id='button_workflow',
                color="link",
                style={"text-decoration": "none"},
            )),
        dbc.Col(
            dcc.Markdown('''
                         ## This workflow represents a comprehensive approach to urban space design, leveraging advanced tools like Grasshopper and Speckle System to create data-driven, sustainable, and contextually relevant urban environments. By integrating geospatial data, parametric modeling, and environmental analysis, this method offers a deeply informed and efficient pathway to designing urban spaces that are both functional and aesthetically pleasing.
                         '''),
        ),
    ]),
], className="mx-5"
)


layout_workflow_modal = dbc.Modal([
    dbc.ModalHeader("# Workflow Explanation"),
    dbc.ModalBody(dcc.Markdown('''                              
                        
    The workflow for urban space design using Grasshopper, a parametric modeler, and Speckle System, a database version control for geometry, is a sophisticated process that leverages the power of data and parametric design to create detailed and informed urban models. Here's an overview of the workflow, divided into key steps:

    1. **Importing Georeferenced Data**: The process begins with the **importation of georeferenced datasets** of the building environment into Grasshopper. This data, which can include topographical, infrastructural, and built environment information, serves as the foundation for creating a **three-dimensional model of the city**. This step is crucial as it ensures the model is grounded in real-world coordinates, providing accuracy and relevance to the urban context. Utilizing Grasshopper's parametric capabilities, the imported data is then transformed into a detailed 3D model of the city. This model includes buildings, streets, and other relevant urban features. The parametric nature of Grasshopper allows for flexibility and precision in modeling, ensuring that the city model is both comprehensive and adaptable to changes.

    2. **Surface Orientation and Type Analysis**: The next phase involves **analyzing the orientation and type of surfaces** across the entire model. This analysis is pivotal in understanding how different surfaces interact with environmental factors such as light and air flow. It helps in identifying potential areas for sustainable design interventions, such as optimizing building orientations for solar gain or natural ventilation. A **sun analysis** is added to the workflow, which assesses sunlight exposure and shadow patterns on the buildings and surrounding areas. This is a crucial step for sustainable urban design, as it informs decisions regarding building placement, window orientation, and the design of outdoor spaces to maximize natural light and minimize heat gain.

    3. **Hypothetical Window View Simulation**: Finally, the workflow culminates in **simulating a view from a hypothetical window position**. This step involves generating a visual representation of what one would see from a specific point within the building, taking into account the orientation, sun exposure, and shadow analysis previously conducted. This simulation is instrumental in understanding the visual and environmental impact of the design from a human perspective.

    This workflow represents a comprehensive approach to urban space design, leveraging advanced tools like Grasshopper and Speckle System to create data-driven, sustainable, and contextually relevant urban environments. By integrating geospatial data, parametric modeling, and environmental analysis, this method offers a deeply informed and efficient pathway to designing urban spaces that are both functional and aesthetically pleasing.
        '''), className='modal-body-modals'),
], id='collapse_workflow', is_open=False, size='lg')


layout_workflow = dbc.Container([

    html.H2("Speckle Exaplanation", id='title_lines', className="my-3 mx-5"),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
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
                                        top=True, alt="...", className="card-img-small"),
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
                                        top=True, alt="...", className="card-img-small"),
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
                                        top=True, alt="...", className="card-img-small"),
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
],    fluid=True,
)


layout_details = dbc.Container([

    html.H2("Stable Diffusion Samples",
            id='title_lines', className="my-3 mx-5"),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        html.A(
                            dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-1'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-2'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-3'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-4'
                        ),
                    ],
                    className="h-100"
                ),
                # width=3
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
                            dbc.CardImg(src="/static/images/OIG (1).jpg", top=True,
                                        alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-1'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-2'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-3'
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
                                        top=True, alt="...", className="card-img-small"),
                            href="#",
                            id='card-image-4'
                        ),
                    ],
                    className="h-100"
                ),
                # width=3
            ),
        ],
        className="my-4 mx-5"  # Add lateral and top/down margin to the row

    ),

],    fluid=True,
)

layout_helper = dbc.Container([

    html.H2("Helper Hands", id='title_helpers', className="my-3 mx-5"),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Experience",
                                    className="card-title"),
                            html.P(
                                "Go-to resource for entering the world of collaborative software development on GitHub, providing essential tools and insights to kickstart your coding projects.", className="card-text"),
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
                                "Repository of your expertise and ideas, featuring a collection of insightful and informative articles you've shared with the world.", className="card-text"),
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
                                "Invaluable contributions of individuals and teams who have been instrumental in shaping your projects, fostering a culture of gratitude and collaboration.", className="card-text"),
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
], fluid=True,
)

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


layout_conclusion = dbc.Row([
    html.Hr(),
    dbc.Row([
        dbc.Col(
            dbc.Button(
                dcc.Markdown(''' 
    # Conclusion
    ''', id='title_conclusion'),
                id='button_conclusion',
                color="link",
                style={"text-decoration": "none"},
            )),
        dbc.Col(
            dcc.Markdown('''
                         ## In summary, the use of stable diffusion in urban space design facilitates a more dynamic, collaborative, and innovative approach to urban planning. It enables faster prototyping and iteration, leading to designs that are not only cost-effective and sustainable but also more aligned with the needs and aspirations of the community.
                         '''),
        ),
    ]),
], className="mx-5")

layout_conclusion_modal = dbc.Modal([
    dbc.ModalHeader("# Workflow Explanation"),
    dbc.ModalBody(dcc.Markdown('''  
                    
                    
    Creating or designing urban spaces using stable diffusion for fast prototyping and iteration offers a range of advantages that can significantly enhance the efficiency and effectiveness of urban planning and architectural design. Here are some key points:

    1. **Speed and Efficiency**: 
    One of the primary advantages of using stable diffusion in urban design is the significant reduction in time required to create and modify designs. This technology enables architects and urban planners to quickly generate a wide range of design variations, allowing for rapid exploration of different ideas and concepts. This speed is particularly useful in the early stages of design, where numerous options need to be considered and assessed.
    Employing stable diffusion techniques reduces the need for extensive physical models or time-consuming manual rendering. By cutting down on these traditionally resource-intensive aspects of urban design, significant cost savings can be achieved. This makes it feasible to explore more options within a given budget, or to allocate resources to other critical areas of a project.

    3. **Enhanced Creativity and Innovation**: The ability to rapidly prototype various designs encourages creativity and innovation. Designers are not limited by the time and effort typically required to visualize each new iteration of their ideas. This freedom allows for more experimental and bold designs, as the cost of failure is much lower when designs can be easily altered or discarded.
    Stable diffusion technology facilitates better collaboration among team members, as well as between designers and stakeholders. It's easier to share and discuss ideas when they can be visualized quickly and accurately. This can lead to more inclusive design processes, where feedback is sought and integrated at various stages, leading to more well-rounded and accepted urban spaces.
    Integrating stable diffusion with other urban planning tools and data sources enables a more analytical approach to design. For instance, designers can quickly model how different urban layouts might affect traffic flow, sunlight exposure, or energy efficiency, and make informed decisions based on these insights.

    6. **Sustainability and Adaptability**: The ability to simulate various scenarios can lead to more sustainable urban designs. Planners can assess the environmental impact of different materials, layouts, and structures before any physical construction begins. Additionally, the adaptability offered by this technology means that designs can be easily modified to respond to changing environmental, social, or economic conditions.
    This technology can also be used to engage the public in the urban design process. By visualizing and sharing potential designs with the community, planners can gather valuable feedback and foster a sense of ownership among residents. This can lead to designs that better reflect the needs and desires of the community.

    In summary, the use of stable diffusion in urban space design facilitates a more dynamic, collaborative, and innovative approach to urban planning. It enables faster prototyping and iteration, leading to designs that are not only cost-effective and sustainable but also more aligned with the needs and aspirations of the community.
    '''), className='modal-body-modals'),
], id='collapse_conclusion', is_open=False, size='lg')


layout = html.Div([
    # dcc.Location(id='url', refresh=False),
    layout_header,
    layout_intro,
    layout_intro_modal,
    layout_matrix,
    # selector_grid,
    # layout_grid,
    layout_workflow_explanation,
    layout_workflow,
    layout_workflow_modal,
    layout_details,
    layout_conclusion,
    layout_conclusion_modal,
    # layout_helper,
    layout_modal,
    layout_popup,
])


# TODO: ADD CARD WITH THE FUNCTIONALITIES OF THE SCRAPPING RESEARCHGATE (VIDEO-TEXT)
