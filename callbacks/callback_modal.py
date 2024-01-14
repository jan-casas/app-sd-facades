import logging
import sys

import dash
import dash_bootstrap_components as dbc

from callbacks_core import app, dash_app
from pages.layout_modals import (modal_architecture_data, modal_article_published,
                                 modal_experience, modal_exploratory_spaces,
                                 modal_urban_analysis,
    #  modal_preview_urban_gpt, modal_preview_energy, modal_preview_compute
                                 )
from pages.layout_grid import grid_option_2, grid_option_1

sys.path.insert(0, 'callbacks_core.py')


# Selector grid
@dash_app.callback(
    dash.dependencies.Output('grid_selector_id', 'children'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_layout(value):
    if value == 'option1':
        return grid_option_1
    else:
        return grid_option_2


# Modal ui
@dash_app.callback(
    [dash.dependencies.Output('modal', 'is_open'),
     dash.dependencies.Output('modal-title', 'children'),
     dash.dependencies.Output('modal-description', 'children'),
     dash.dependencies.Output('modal-body', 'children')],
    [dash.dependencies.Input('card-image-1', 'n_clicks'),
     dash.dependencies.Input('card-image-2', 'n_clicks'),
     dash.dependencies.Input('card-image-3', 'n_clicks'),
     dash.dependencies.Input('helper-button-1', 'n_clicks'),
     dash.dependencies.Input('helper-button-2', 'n_clicks'),
     #  dash.dependencies.Input('card-preview-1', 'n_clicks'),
     #  dash.dependencies.Input('card-preview-2', 'n_clicks'),
     #  dash.dependencies.Input('card-preview-3', 'n_clicks'),
     ],
    [dash.dependencies.State('modal', 'is_open')]
)
def toggle_modal(n1, n2, n3, h1, h2, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, None, None, None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'card-image-1':
            return not is_open, 'Architecture Driven by Data', ('Contemporary architecture is transformed by '
                                                                'data-driven decision-making, harmonizing aesthetics '
                                                                'and practicality to create structures that resonate '
                                                                'with the modern world.'), modal_architecture_data
        elif button_id == 'card-image-2':
            return not is_open, 'Data-Driven Decision Making', ('Data-driven decision making is the process of making '
                                                                'decisions based on data analysis and '
                                                                'interpretation.'), modal_exploratory_spaces
        elif button_id == 'card-image-3':
            return (not is_open, 'Practicality and Aesthetics', ('Practicality and aesthetics are two important '
                                                                 'considerations in contemporary architecture.'),
                    modal_urban_analysis)
        elif button_id == 'helper-button-1':
            return not is_open, 'Architecture Driven by Data', ('Contemporary architecture is transformed by '
                                                                'data-driven decision-making, harmonizing aesthetics '
                                                                'and practicality to create structures that resonate '
                                                                'with the modern world.'), modal_experience
        elif button_id == 'helper-button-2':
            return not is_open, 'Data-Driven Decision Making', ('Data-driven decision making is the process of making '
                                                                'decisions based on data analysis and '
                                                                'interpretation.'), modal_article_published
        # # Avoid interference with the dropdown
        # elif button_id == 'card-preview-1' and p1:
        #     return not is_open, 'Data-Driven Decision Making', 'Data-driven decision making is the process of
        #     making decisions based on data analysis and interpretation.', modal_preview_urban_gpt
        # elif button_id == 'card-preview-2' and p2:
        #     return not is_open, 'Data-Driven Decision Making', 'Data-driven decision making is the process of
        #     making decisions based on data analysis and interpretation.', modal_preview_compute
        # elif button_id == 'card-preview-3' and p3:
        #     return not is_open, 'Data-Driven Decision Making', 'Data-driven decision making is the process of
        #     making decisions based on data analysis and interpretation.', modal_preview_energy
        return is_open, None, None, None
