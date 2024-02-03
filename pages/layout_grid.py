from pages.layout_modals import *

grid_option_1 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/city_density4.png",
                                    top=True, alt="...", className="card-img"),
                        href="https://nl-db.azurewebsites.net",
                        target="_blank",
                        # href="#",
                        id="card-preview-1"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Urban GPT",
                                    className="card-title"),
                            html.P(
                                "Urban GPT, a groundbreaking project, harnesses AI's potential to revolutionize urban planning, offering innovative solutions for smarter, more efficient cities."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/city_density.png",
                                    top=True, alt="...", className="card-img"),
                        href='#',
                        target="_blank",
                        id="card-preview-2"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Cloud Scripting Compute",
                                    className="card-title"),
                            dbc.Badge("Under Mantaineance",
                                      color="warning"),
                            html.P(
                                "Cloud Scripting Compute redefines computing with the flexibility and scalability of the cloud, enabling dynamic, on-demand data processing and analysis for a wide range of applications."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/city_density2.png",
                                    top=True, alt="...", className="card-img"),
                        href="https://dash-valencia.azurewebsites.net",
                        target="_blank",
                        # href='#',
                        id="card-preview-3"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Energy Analysis Search",
                                    className="card-title"),
                            html.P(
                                "Energy Analysis Search is an advanced tool that empowers researchers and professionals to explore, analyze, and optimize energy systems, contributing to a sustainable future."),
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
                        dbc.CardImg(src="/static/images/city_density3.png",
                                    top=True, alt="...", className="card-img"),
                        href="https://nl-db.azurewebsites.net",
                        target="_blank",
                        id="card-preview-4"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Building Version Control",
                                    className="card-title"),
                            html.P(
                                "The Version Control Dashboard provides real-time insights into transportation patterns, facilitating data-driven decisions for more accessible and efficient urban mobility."),
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
                        dbc.CardImg(src="/static/images/energy_saving9.png", top=True,
                                    alt="...", className="card-img"),
                        href="https://dash-building.azurewebsites.net",
                        target="_blank",
                        id="card-preview-5"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Smart Building Management",
                                    className="card-title"),
                            html.P(
                                "Smart Building Management integrates cutting-edge technologies to enhance the efficiency, comfort, and sustainability of structures, leading the way in the evolution of modern architecture and urban design."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
    ],
    className="my-4 mx-5"  # Add lateral and top/down margin to the row

)

grid_option_2 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/OIG (5).jpg",
                                    top=True, alt="...", className="card-img"),
                        # href="https://gptprompt.azurewebsites.net",
                        # target="_blank",
                        href="#",
                        id="card-preview-function-1"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Ask GPT to Interrogate Pdfs/Videos",
                                    className="card-title"),
                            html.P(
                                "Interrogate your pdfs with GPT-3, a groundbreaking project, harnesses AI's potential to revolutionize urban planning, offering innovative solutions for smarter, more efficient cities."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardImg(src="",
                                top=True, alt="...", className="card-img"),
                    dbc.CardBody(
                        [
                            html.H5("Ask GPT to Interrogate Videos",
                                    className="card-title"),
                            # dbc.Badge("Under Mantaineance",
                            #           color="warning"),
                            html.P(
                                "Ask GPT to Interrogate Videos redefines computing with the flexibility and scalability of the cloud, enabling dynamic, on-demand data processing."),
                        ]),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="",
                                    top=True, alt="...", className="card-img"),
                        href="#",
                        target="_blank"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Energy Analysis Search",
                                    className="card-title"),
                            html.P(
                                "Energy Analysis Search is an advanced tool that empowers researchers and professionals to explore, analyze, and optimize energy systems, contributing to a sustainable future."),
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
                        dbc.CardImg(src="https://example.com/image.jpg",
                                    top=True, alt="...", className="card-img"),
                        href="https://nl-db.azurewebsites.net",
                        target="_blank",
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Mobility Mapping Dashboard",
                                    className="card-title"),
                            html.P(
                                "The Mobility Mapping Dashboard provides real-time insights into transportation patterns, facilitating data-driven decisions for more accessible and efficient urban mobility."),
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
                        dbc.CardImg(src="https://example.com/image.jpg", top=True,
                                    alt="...", className="card-img"),
                        href="https://dash-building.azurewebsites.net",
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Smart Building Management",
                                    className="card-title"),
                            html.P(
                                "Smart Building Management integrates cutting-edge technologies to enhance the efficiency, comfort, and sustainability of structures, leading the way in the evolution of modern architecture and urban design."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
    ],
    className="my-4 mx-5"  # Add lateral and top/down margin to the row

)

# Layout assets
grid_option_1_assets = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        html.Iframe(id='section_view', width="100%", height="100%", className="card-img"),
                        target="_blank",
                        id="card-preview-1"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Section Cut Facades",
                                    className="card-title"),
                            html.P(
                                "The MediaTic building is a benchmark for sustainable architecture, with a facade that combines aesthetics and energy efficiency. The facade is composed of a double skin that acts as a thermal regulator, reducing energy consumption and improving the building's energy efficiency."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        html.Iframe(id='facade_view', width="100%",
                                    height="100%", className="card-img"),
                        # dbc.CardImg(src="/static/images/F3.jpg",
                        #             top=True, alt="...", className="card-img"),
                        href='#',
                        target="_blank",
                        id="card-preview-2"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Facade Analysis",
                                    className="card-title"),
                            dbc.Badge("Under Mantaineance",
                                      color="warning"),
                            html.P(
                                "The building has 4 facades, each with a different orientation. The facade facing the street is the most exposed to solar radiation, while the facade facing the courtyard is the least exposed. The facade facing the street is the most exposed to solar radiation, while the facade facing the courtyard is the least exposed."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        # dbc.CardImg(
                        html.Iframe(id='2d_view',
                                    src="https://speckle.xyz/embed?stream=35ba1243e5&commit=22da188d36&c=%5B24%2C23.99993%2C81.9093%2C24%2C24%2C9.624%2C0%2C1%5D&filter=%7B%22sectionBox%22%3A%5B-3.22%2C-2.95%2C-38.01%2C51.22%2C50.95%2C18.36%5D%7D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
                                    width="100%", height="100%", className="card-img"),
                        # href="https://dash-valencia.azurewebsites.net",
                        target="_blank",
                        # href='#',
                        id="card-preview-3"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Floorplan Occupancy View",
                                    className="card-title"),
                            html.P(
                                "The Floorplan Occupancy View is a tool that allows you to visualize the occupancy of a building in real time. The tool is designed to help you understand how people move through a building and how they use the space."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
    ],
    className="my-4 mx-5"  # Add lateral and top/down margin to the row

)

grid_option_2_assets = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/OIG (5).jpg",
                                    top=True, alt="...", className="card-img"),
                        # href="https://gptprompt.azurewebsites.net",
                        # target="_blank",
                        href="#",
                        id="card-preview-function-1"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Ask GPT to Interrogate Pdfs/Videos",
                                    className="card-title"),
                            html.P(
                                "Interrogate your pdfs with GPT-3, a groundbreaking project, harnesses AI's potential to revolutionize urban planning, offering innovative solutions for smarter, more efficient cities."),
                        ]
                    ),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardImg(src="",
                                top=True, alt="...", className="card-img"),
                    dbc.CardBody(
                        [
                            html.H5("Ask GPT to Interrogate Videos",
                                    className="card-title"),
                            # dbc.Badge("Under Mantaineance",
                            #           color="warning"),
                            html.P(
                                "Ask GPT to Interrogate Videos redefines computing with the flexibility and scalability of the cloud, enabling dynamic, on-demand data processing."),
                        ]),
                    # dbc.CardFooter(
                    #     "Last updated 3 mins ago", className="text-muted")
                ],
                className="h-100"
            ),
            # width=3
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="",
                                    top=True, alt="...", className="card-img"),
                        href="#",
                        target="_blank"
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Energy Analysis Search",
                                    className="card-title"),
                            html.P(
                                "Energy Analysis Search is an advanced tool that empowers researchers and professionals to explore, analyze, and optimize energy systems, contributing to a sustainable future."),
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
                        dbc.CardImg(src="https://example.com/image.jpg",
                                    top=True, alt="...", className="card-img"),
                        href="https://nl-db.azurewebsites.net",
                        target="_blank",
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Mobility Mapping Dashboard",
                                    className="card-title"),
                            html.P(
                                "The Mobility Mapping Dashboard provides real-time insights into transportation patterns, facilitating data-driven decisions for more accessible and efficient urban mobility."),
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
                        dbc.CardImg(src="https://example.com/image.jpg", top=True,
                                    alt="...", className="card-img"),
                        href="https://dash-building.azurewebsites.net",
                    ),
                    dbc.CardBody(
                        [
                            html.H5("Smart Building Management",
                                    className="card-title"),
                            html.P(
                                "Smart Building Management integrates cutting-edge technologies to enhance the efficiency, comfort, and sustainability of structures, leading the way in the evolution of modern architecture and urban design."),
                        ]
                    ),

                ],
                className="h-100"
            ),
            # width=3
        ),
    ],
    className="my-4 mx-5"  # Add lateral and top/down margin to the row

)
