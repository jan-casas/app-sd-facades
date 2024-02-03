import sys
import dash
from callbacks_core import dash_app
from pages.layout_modals import modal_default_layout
from pages.layout_grid import grid_option_2, grid_option_1
# Import functions
from apps.app_modals import mapbox_plotly, horizontal_bar_graph, create_subplots
# Import test data
from pages.descriptions import *
from database.test_data import df, df_global
from pages.descriptions import *
from utils.utils import extract_main_colors

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


# Card-Modal-Data interaction
@dash_app.callback(
    [dash.dependencies.Output('modal', 'is_open'),
     dash.dependencies.Output('modal_title', 'children'),
     dash.dependencies.Output('card_description', 'children'),
     dash.dependencies.Output('modal_description', 'children'),
     dash.dependencies.Output('modal-body', 'children'),
     dash.dependencies.Output('card_image', 'src')],
    [dash.dependencies.Input('card-image-1', 'n_clicks'),
     dash.dependencies.Input('card-image-2', 'n_clicks'),
     dash.dependencies.Input('card-image-3', 'n_clicks'),
     dash.dependencies.Input('card-image-4', 'n_clicks'),
     dash.dependencies.Input('card-image-5', 'n_clicks'),
     dash.dependencies.Input('card-image-6', 'n_clicks'),
     dash.dependencies.Input('card-image-7', 'n_clicks'),
     dash.dependencies.Input('card-image-8', 'n_clicks'),
     dash.dependencies.Input('card-image-9', 'n_clicks'),
     dash.dependencies.Input('card-image-10', 'n_clicks'),
     dash.dependencies.Input('card-image-11', 'n_clicks'),
     dash.dependencies.Input('card-image-12', 'n_clicks'),
     dash.dependencies.Input('helper-button-1', 'n_clicks'),
     dash.dependencies.Input('helper-button-2', 'n_clicks'),
     ],
    [dash.dependencies.State('modal', 'is_open')]
)
def toggle_modal(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, h1, h2, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, None, None, None, None, None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'card-image-1':
            return (not is_open, facade_sun_radiation['title'], facade_sun_radiation['card_introduction'],
                    facade_sun_radiation['description'], modal_default_layout, facade_sun_radiation['image'])
        elif button_id == 'card-image-2':
            return (not is_open, shadow_overcast_time['title'], shadow_overcast_time[
                'card_introduction'], shadow_overcast_time['description'], modal_default_layout,
                    shadow_overcast_time['image'])
        elif button_id == 'card-image-3':
            return (not is_open, morning_afternoon_sun_radiation['title'], morning_afternoon_sun_radiation[
                'card_introduction'],
                    morning_afternoon_sun_radiation['description'], modal_default_layout,
                    morning_afternoon_sun_radiation['image'])
        elif button_id == 'card-image-4':
            return (not is_open, density['title'], density['card_introduction'], density['description'],
                    modal_default_layout, density['image'])
        elif button_id == 'card-image-5':
            return (not is_open, views_availability['title'], views_availability['card_introduction'],
                    views_availability['description'], modal_default_layout, views_availability['image'])
        elif button_id == 'card-image-6':
            return (not is_open, age_of_building['title'], age_of_building['card_introduction'],
                    age_of_building['description'], modal_default_layout, age_of_building['image'])
        elif button_id == 'card-image-7':
            return (not is_open, urban_noise['title'], urban_noise['card_introduction'], urban_noise['description'],
                    modal_default_layout, urban_noise['image'])
        elif button_id == 'card-image-8':
            return (
                not is_open, close_distance_to_green_areas['title'], close_distance_to_green_areas['card_introduction'],
                close_distance_to_green_areas['description'], modal_default_layout,
                close_distance_to_green_areas['image'])
        elif button_id == 'card-image-9':
            return (not is_open, potential_cost_reduction_solar_energy['title'], potential_cost_reduction_solar_energy[
                'card_introduction'], potential_cost_reduction_solar_energy['description'], modal_default_layout,
                    potential_cost_reduction_solar_energy['image'])
        elif button_id == 'card-image-10':
            return (not is_open, social_life['title'], social_life[
                'card_introduction'], social_life['description'], modal_default_layout,
                    social_life['image'])
        elif button_id == 'card-image-11':
            return (not is_open, territorial_connection['title'],
                    territorial_connection['card_introduction'],
                    territorial_connection['description'], modal_default_layout,
                    territorial_connection['image'])
        elif button_id == 'card-image-12':
            return (not is_open, air_pollution['title'], air_pollution[
                'card_introduction'], air_pollution['description'], modal_default_layout,
                    air_pollution['image'])
        elif button_id == 'helper-button-1':
            return not is_open, 'Architecture Driven by Data', ('Contemporary architecture is transformed by '
                                                                'data-driven decision-making, harmonizing aesthetics '
                                                                'and practicality to create structures that resonate '
                                                                'with the modern world.'), modal_experience, None, None
        elif button_id == 'helper-button-2':
            return not is_open, 'Data-Driven Decision Making', ('Data-driven decision making is the process of making '
                                                                'decisions based on data analysis and '
                                                                'interpretation.'), modal_article_published, None, None
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
        return is_open, None, None, None, None, None


# Layout assets Speckle
views = {
    "section_Este": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&c=%5B-48.51712%2C21.59411%2C16.39624%2C18.75933%2C21.59411%2C16.39624%2C0%2C1%5D&filter=%7B%22sectionBox%22%3A%5B7.64%2C-2.95%2C-18.56%2C62.09%2C50.95%2C37.81%5D%7D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "elevation_Este": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "section_Oeste": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&c=%5B23.17697%2C91.27659%2C15.39427%2C23.17697%2C24.00014%2C15.39427%2C0%2C1%5D&filter=%7B%22sectionBox%22%3A%5B-3.22%2C-15.27%2C-18.56%2C51.22%2C38.63%2C37.81%5D%7D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "elevation_Oeste": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&c=%5B-67.99179%2C24%2C9.624%2C24%2C24%2C9.624%2C0%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "section_Sur": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&c=%5B66.71794%2C10.48167%2C14.17571%2C32.4325%2C10.48167%2C14.17571%2C0%2C1%5D&filter=%7B%22sectionBox%22%3A%5B-17.27%2C-2.95%2C-18.56%2C37.18%2C50.95%2C37.81%5D%7D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "elevation_Sur": "https://speckle.xyz/embed?stream=4000327e5d&commit=0edc6b2b24&c=%5B110.50025%2C24%2C9.624%2C24%2C24%2C9.624%2C0%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true",
    "plan": "https://speckle.xyz/embed?stream=35ba1243e5&commit=22da188d36&c=%5B24%2C23.99993%2C81.9093%2C24%2C24%2C9.624%2C0%2C1%5D&filter=%7B%22sectionBox%22%3A%5B-3.22%2C-2.95%2C-38.01%2C51.22%2C50.95%2C18.36%5D%7D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"
}


@dash_app.callback(
    [dash.dependencies.Output('section_view', 'src'),
     dash.dependencies.Output('facade_view', 'src')],
    [dash.dependencies.Input('dropdown_fachadas', 'value')]
)
def update_section(dropdown_fachadas):
    '''
    Update Section and Elevation Views
    '''
    # embed_src_section = get_stream(2, 0, views['section_'+dropdown_fachadas])
    embed_src_section = views['section_' + dropdown_fachadas]
    embed_src_elevation = views['elevation_' + dropdown_fachadas]

    return embed_src_section, embed_src_elevation


# Layout modal assets
@dash_app.callback(
    [dash.dependencies.Output('city_mapbox_modal', 'figure'),
     dash.dependencies.Output('progress_graph_max', 'figure'),
     dash.dependencies.Output('progress_graph_min', 'figure'),
     dash.dependencies.Output('progress_graph_global', 'figure'),
     dash.dependencies.Output('subplot_div', 'figure')],  # Add an output for the subplot
    [dash.dependencies.Input('city_mapbox_modal', 'selectedData'),
     dash.dependencies.Input('card_image', 'src')],
)
def create_map(selectedData, image_url):
    # Main colors
    n_rows = df.shape[0]
    colors = extract_main_colors(image_url, n_rows)
    colors_str = ['rgb(' + ', '.join(map(str, color)) + ')' for color in colors]

    # Check if the selectedData is None
    if selectedData is None:
        top_performers, low_performers, global_performers = horizontal_bar_graph(df, df_global, colors_str=colors_str)
        subplot_fig = create_subplots(df, colors_str=colors_str)  # Create the subplot

        return (mapbox_plotly(city_data=df, df_global=df_global, colors_str=colors_str), top_performers,
                low_performers, global_performers, subplot_fig)
    else:
        points = selectedData['points']
        localid = [point['text'] for point in points]
        city_data = df[df['localid'].isin(localid)]
        top_performers, low_performers, global_performers = horizontal_bar_graph(city_data, df_global,
                                                                                 colors_str=colors_str)
        subplot_fig = create_subplots(city_data, colors_str=colors_str)  # Create the subplot
        # Create the mapbox plot
        return (
            mapbox_plotly(city_data=city_data, df_global=df_global, colors_str=colors_str), top_performers,
            low_performers,
            global_performers, subplot_fig)
