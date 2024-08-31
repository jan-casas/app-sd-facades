import sys
import time

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from hugchat import hugchat
from hugchat.login import Login

from config.settings import HUGGINGFACE_MAIL, HUGGINGFACE_PASSWORD
from core_callbacks import dash_app

# import dash_core_components as dcc

sys.path.insert(0, 'core_callbacks.py')


@dash_app.callback(
    [
        dash.dependencies.Output("chat-area", "children"),
        dash.dependencies.Output("message-input", "value"),
        dash.dependencies.Output("loading-output", "children"),
    ],
    [dash.dependencies.Input("send-button", "n_clicks"),
     dash.dependencies.Input("reset-button", "n_clicks")],
    [dash.dependencies.State("message-input", "value"),
     dash.dependencies.State("chat-area", "children")],
    prevent_initial_call=True,
)
def update_chat(send_n_clicks, reset_n_clicks, message, chat_history):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # clear chat area and message input
    if button_id == "reset-button":
        return [], "", None

    if message:
        # simulate loading time (not needed)
        time.sleep(1)
        message_prompt = (f"{message}. Create a concise and precise response. Limit the answer to"
                          f"1-2 short paragraphs.")
        # call the function to handle HugChat logic
        response = handle_hugchat_logic(HUGGINGFACE_MAIL, HUGGINGFACE_PASSWORD, message_prompt)

        # prepare chat messages for display
        new_message = create_message_div(
            f"You: {message}",
            sender="user")
        response_message = create_message_div(f"Assistant: {response}", sender="bot")

        # update chat history
        updated_history = chat_history or []
        updated_history = [response_message, new_message] + updated_history

        return updated_history, "", None  # Clear message input after sending
    return chat_history, "", None


def create_message_div(message, sender="user"):
    return dbc.Row(
        dbc.Card(
            dbc.CardBody(dcc.Markdown(message)),
            className=f"mb-2 text-white {'bg-primary' if sender == 'user' else 'bg-secondary'}",
            style={"width": "75%", "margin-left": "auto" if sender == "user" else "0"},
        ),  # width=8
    )


def handle_hugchat_logic(email, password, user_message):
    try:
        # perform login to HugChat
        login = Login(email, password)
        cookies = login.login()

        # create a chatbot instance with the obtained cookies
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        # prepare the prompt for the chatbot
        prompt = f"User: {user_message}\nAssistant:"

        # get the response from the chatbot
        response = chatbot.chat(prompt)

        return response

    # handle exceptions (like login failure, API errors, etc.)
    except Exception as e:
        print("Error in HugChat logic:", e)
        return ("Sorry, I couldn't process your request. Probably because the author's credential "
                "is expired or wrong!")


@dash_app.callback(
    dash.dependencies.Output("modal-help", "is_open"),
    [dash.dependencies.Input("nav-link-contact", "n_clicks")],
    [dash.dependencies.State("modal-help", "is_open")],
)
def toggle_modal(n1, is_open: bool) -> bool:
    if n1:
        return not is_open
    return is_open
