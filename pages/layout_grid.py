import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from pages.layout_modals import *
from pages.layout_default import layout_header


grid_option_1 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.A(
                        dbc.CardImg(src="/static/images/OIG (6).jpg",
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
                        dbc.CardImg(src="/static/images/F3.jpg",
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
                        dbc.CardImg(src="/static/images/F1.jpg",
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
                        dbc.CardImg(src="/static/images/versions.jpg",
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
                        dbc.CardImg(src="/static/images/F2.jpg", top=True,
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
