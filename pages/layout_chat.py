from pages.pages_helper.layout_modals import *

layout_chat = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    id="chat-area",
                    style={'height': '100%', 'overflow-y': 'auto', 'overflow-x': 'hidden'},
                )
            ),  # className="my-4 mx-4"
        ),
        dcc.Loading(
            id="loading", type="default", children=html.Div(id="loading-output")
        ),
    ],
    fluid=True,
)

layout_modal_help = html.Div([
    dbc.Modal([
        dbc.ModalHeader([
            html.Div([

                html.Div([
                    html.H2("Meta's LLaMA Assistant"),
                    # html.Span('Chat about the current page information:'),
                    dbc.Row(
                        dbc.InputGroup(
                            [
                                # dbc.InputGroupText("Enter message:"),
                                dbc.Input(
                                    id="message-input",
                                    placeholder="Ask me anything about the current page!",
                                    type="text",
                                ),
                                dbc.InputGroupText(
                                    dbc.Button("Send", id="send-button", n_clicks=0)
                                ),
                                dbc.InputGroupText(
                                    dbc.Button("Reset", id="reset-button", n_clicks=0)
                                ),
                            ],
                        ),
                        # className="my-4 mx-4",
                        # style={"position": "sticky", "bottom": "0"},
                    ),
                ], style={'marginLeft': '20px', 'textAlign': 'left'})
            ], id='grid-item-1', className='grid-item',
                style={'display': 'flex', 'alignItems': 'center', 'margin-left': '40px', 'margin-right': '40px',
                       'margin-top': '40px', 'margin-bottom': '15px'}),
        ], style={'padding': '0px', 'margin': '0px'}, close_button=False, id='modal-header-help'
        ),
        # Responsive information
        dbc.ModalBody(id='modal-body-help', children=layout_chat,
                      style={'padding': '40px', 'margin': '0px'}),

    ], id='modal-help', size='lg', scrollable=True, is_open=False,
        style={'width': '100%', 'height': '100%', 'padding': '0px', 'margin': '0px'}),
])
