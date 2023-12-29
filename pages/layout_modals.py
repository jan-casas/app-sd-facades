from dash import Dash, Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc

modal_exploratory_spaces = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Video(src='/static/videos/AbsoluteNft.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    ),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Video(src='/static/videos/Pedroso.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 2.** Architecture of the API.
		''',
    ),
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})

modal_architecture_data = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/Castelar.png',
             style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    ),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/HighresScreenshot00048.png',
             style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 2.** Architecture of the API.
		''',
    )
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})


modal_urban_analysis = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/3dmodel_l.png', style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    ),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/nft_valencia_invert.png',
             style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 2.** Architecture of the API.
		''',
    ),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/qgis.png', style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 3.** Architecture of the API.
		''',
    ),
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})

# TODO: ADD LOSANGELES video IN 'Article published' modal along with info about the articles


modal_experience = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
BECARIO GRUPO INVESTIGACIÓN ARQUITECTURAS OPEN SOURCE
-	AUTOR INVESTIGACIÓN : Harmonization of land-cover data to assess agricultural land transformation patterns in the peri-urban Spanish Mediterranean Huertas.

ESTUDIANTE PHD GRUPO INVESTIGACIÓN ARQUITECTURAS OPEN SOURCE
-	AUTOR INVESTIGACIÓN : Parametric-based and automatized GIS application to calculate energy savings of the building envelope in rehabilitated nearly zero energy buildings. 
-	PROYECTO CTAZ LINEAS TRANSPORTE : Procesamiento y análisis de datos históricos en líneas de Transporte Públicas área metropolitana de Zaragoza. 
-	CÁTEDRA MOBILITY EXPERIENCE : Simulación y análisis con variables de movilidad urbana según escenarios cotidianos en Zaragoza. 

ARQUITECTO EN GRAVALOSDIMONTE ARQUITECTOS
-	BIENAL DE VENECIA 2019: Una strategia di riuso per gli scali ferroviari alla biennale

PROVEEDOR AUTÓNOMO GRUPO INVESTIGACIÓN OPEN SOURCE
-	EXTRACCIÓN Y PROCESAMIENTO A ESCALA NACIONAL : Automatización de los cálculos de Ahorro Energético en el envolvente de edificios en España.
-	SIMULACIÓN LOS ÁNGELES: Material de apoyo interactivo Conferencia sobre desarrollo urbano en Los Ángeles.

CIENTÍFICO DATOS EN ELLIOT CLOUD/BOSONIT
-	PROYECTO OPEDENERGY: Desarrollo proyecto plantas solares en 2 continentes. Programación en Python de los procesos de calidad de datos, auditorías y automatizaciones complejas, utilización y mejoras de APIs, desarrollo de bases de datos, KPIS y diseño de paneles de control.
		''',
    ),

    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})


modal_article_published = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
-	Harmonization of land-cover data to assess agricultural land transformation patterns in the peri-urban Spanish Mediterranean Huertas.
https://www.tandfonline.com/doi/full/10.1080/1747423X.2021.2022793
-	Parametric-based and automatized GIS application to calculate energy savings of the building envelope in rehabilitated nearly zero energy buildings. 
https://www.sciencedirect.com/science/article/abs/pii/S0378778819332888
-	CÁTEDRA MOBILITY EXPERIENCE : Simulación y análisis con variables de movilidad urbana según escenarios cotidianos en Zaragoza. 
		''',
    ),
    html.Video(src='/static/videos/LosAngeles.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 2.** Architecture of the API.
		''',
    ),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Img(src='/static/web/lidar_upscale.png',
             style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 2.** Architecture of the API.
		''',
    ),
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})


# TODO: Modificar los layout modal según portfolio proyectos (mñas completo)


# %% Modals preview
# DE MOMENTO NO SE UTILIZA, ES MÁS SENCILLO AÑADIR UN MODAL AL INICIO DE LA APP QUE EXPLIQUE TODO, DESDE UNA NUEVA VENTANA -> CON LAS FUNCIONES TAMPOCO TIENE SENTIOD EL MODAL. EL RESTO DE MODALES FALLA PORQUE SI NO ESTÁ SELECCIONADO POR EL DROPDOWN DA ERROR EL CALLBACK
modal_preview_urban_gpt = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Video(src='/static/videos/AbsoluteNft.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    )
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})

modal_preview_compute = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Video(src='/static/videos/AbsoluteNft.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    )
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})

modal_preview_energy = dbc.Row([
    # html.Hr(),
    html.H2('Architecture of the API'),
    dcc.Markdown(
        '''
		The importance of the API is that it allows the communication between the front-end and the back-end. The front-end is the part of the application that the user interacts with, while the back-end is the part that processes the data and sends it to the front-end. The API is the intermediary between the two, allowing the front-end to send requests to the back-end and receive responses.
		''',
    ),
    html.Video(src='/static/videos/AbsoluteNft.mp4',
               controls=True, style={'width': '100%'}),
    dcc.Markdown(
        '''					
		**Figure 1.** Architecture of the API.
		''',
    )
    # html.Hr(),
], style={'padding': '0px', 'margin-left': '40px', 'margin-right': '40px', 'margin-bottom': '0px', 'margin-top': '0px'})
