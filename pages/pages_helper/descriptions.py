# New Releases
import datetime
import random

import pandas as pd


def random_date():
    """
    This function returns a random date between the start_date and end_date.
    """
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()

    # Use datetime.timedelta instead of datetime.datetime.timedelta
    random_date = start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    string_random_date = random_date.strftime("%Y-%m-%d %H:%M:%S")
    return string_random_date


facade_sun_radiation = {
    "id": "card-image-1",
    "title": "Facade Sun Radiation",
    "simplified_title": "Sun",
    "card_introduction": """Sun radiation on building facades is a critical factor in urban planning and 
    architectural design. It 
    directly influences the thermal comfort and energy efficiency of building.""",
    "description": """Sun radiation on building facades is a critical factor in urban planning and architectural 
    design. It directly influences the thermal comfort and energy efficiency of buildings. The amount of sun 
    radiation a facade receives 
    can significantly impact the heating and cooling requirements of a building, thereby affecting its energy 
    consumption. The results 
    will highlight the areas that receive high or low sun radiation, enabling a more informed decision-making process 
    in urban 
    development projects.""",
    "docs": "/docs/sun_radiation",
    "image": "static/images/energy_saving8.png",
    "badge": "In Progress",
    "src": """
    https://app.speckle.systems/projects/166220d6a4/models/e2960ffb4a#embed=%7B%22isEnabled%22%3Atrue%2C
    %22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "updated": random_date()
}

shadow_overcast_time = {
    "id": "card-image-2",
    "title": "Shadow Overcast Time",
    "simplified_title": "Shadow",
    "card_introduction": """The duration of shadow overcast can significantly impact the thermal comfort and energy 
    efficiency of 
    buildings.""",
    "description": """The duration of shadow overcast on a building can significantly impact its heating and cooling 
    requirements, 
    thereby affecting its energy consumption. The results will highlight the areas that have long or short shadow 
    overcast times, 
    enabling a more informed decision-making process in urban development projects.""",
    "docs": "/docs/shadow_overcast_time",
    "image": "static/images/energy_saving7.png",
    "badge": "New",
    "src": """
    https://app.speckle.systems/projects/166220d6a4/models/e2960ffb4a#embed=%7B%22isEnabled%22%3Atrue%2C
    %22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "updated": random_date()
}

morning_afternoon_sun_radiation = {
    "id": "card-image-3",
    "title": "Morning/Afternoon Sun Radiation",
    "simplified_title": "Sun Morning/Afternoon",
    "card_introduction": """The amount of sun radiation in the morning and afternoon can significantly impact the 
    thermal comfort and 
    energy efficiency of buildings.""",
    "description": """The amount of sun radiation a building receives in the morning and afternoon can significantly 
    impact its heating 
    and cooling requirements, thereby affecting its energy consumption. The results will highlight the areas that 
    receive high or low sun 
    radiation, enabling a more informed decision-making process in urban development projects.""",
    "docs": "/docs/morning_afternoon_sun_radiation",
    "image": "static/images/energy_saving6.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

density = {
    "id": "card-image-4",
    "title": "Density",
    "simplified_title": "Density",
    "card_introduction": """The density of buildings in an area can significantly impact the thermal comfort and 
    energy efficiency of 
    buildings.""",
    "description": """The density of buildings in an area can significantly impact the heating and cooling 
    requirements of a building, 
    thereby affecting its energy consumption. The results will highlight the areas that have high or low density, 
    enabling a more 
    informed decision-making process in urban development projects.""",
    "docs": "/docs/density",
    "image": "static/images/energy_saving5.png",
    "badge": "New",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

views_availability = {
    "id": "card-image-5",
    "title": "Views Availability",
    "simplified_title": "Views",
    "card_introduction": """The availability of views can significantly impact the quality of life for building 
    occupants.""",
    "description": """The availability of views from a building can significantly impact the quality of life for its 
    occupants. The 
    results will highlight the areas that have good or poor views, enabling a more informed decision-making process 
    in urban development 
    projects.""",
    "docs": "/docs/views_availability",
    "image": "static/images/city_density4.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

age_of_building = {
    "id": "card-image-6",
    "title": "Age of the Building",
    "simplified_title": "Age",
    "card_introduction": """The age of a building can significantly impact its energy efficiency and maintenance 
    requirements.""",
    "description": """The age of a building can significantly impact its energy efficiency and maintenance 
    requirements. Older buildings 
    may require more energy for heating and cooling, and may also require more frequent maintenance. The results will 
    highlight the areas 
    with older or newer buildings, enabling a more informed decision-making process in urban development projects.""",
    "docs": "/docs/age_of_building",
    "image": "static/images/city_density3.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

urban_noise = {
    "id": "card-image-7",
    "title": "Urban Noise",
    "simplified_title": "Noise",
    "card_introduction": """Urban noise can significantly impact the quality of life for building occupants.""",
    "description": """Urban noise can significantly impact the quality of life for building occupants. High levels of 
    noise can lead to 
    stress and other health issues. The results will highlight the areas with high or low levels of noise, 
    enabling a more informed 
    decision-making process in urban development projects.""",
    "docs": "/docs/urban_noise",
    "image": "static/images/city_density2.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

close_distance_to_green_areas = {
    "id": "card-image-8",
    "title": "Close Distance to Green/Walking Areas",
    "simplified_title": "Closinness",
    "card_introduction": """The proximity of buildings to green or walking areas can significantly impact the quality 
    of life for 
    building occupants.""",
    "description": """The proximity of buildings to green or walking areas can significantly impact the quality of 
    life for building 
    occupants. Access to green spaces and walking areas can promote physical activity and improve mental health. The 
    results will 
    highlight the areas that are close or far from green/walking areas, enabling a more informed decision-making 
    process in urban 
    development projects.""",
    "docs": "/docs/close_distance_to_green_areas",
    "image": "static/images/energy_saving.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

potential_cost_reduction_solar_energy = {
    "id": "card-image-9",
    "title": "Potential Cost Reduction Using Solar Energy",
    "simplified_title": "Energy",
    "card_introduction": """The use of solar energy can significantly reduce the energy costs for buildings.""",
    "description": """The use of solar energy can significantly reduce the energy costs for buildings. Solar panels 
    can generate 
    electricity, reducing the amount of electricity that needs to be purchased from the grid. The results will 
    highlight the areas that 
    have high potential for cost reduction using solar energy, enabling a more informed decision-making process in 
    urban development 
    projects.""",
    "docs": "/docs/potential_cost_reduction_solar_energy",
    "image": "static/images/energy_saving2.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

social_life = {
    "id": "card-image-10",
    "title": "Social Life",
    "simplified_title": "Social",
    "card_introduction": """The quality of social life can significantly impact the quality of life for building 
    occupants.""",
    "description": """The quality of social life in a building can significantly impact the quality of life for its 
    occupants. Buildings 
    with good social life can promote community interaction and improve mental health. The results will highlight the 
    areas that have 
    good or poor social life, enabling a more informed decision-making process in urban development projects.""",
    "docs": "/docs/social_life",
    "image": "static/images/city_territorial.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

territorial_connection = {
    "id": "card-image-11",
    "title": "Territorial Connection",
    "simplified_title": "Connectivity",
    "card_introduction": """The territorial connection of a building can significantly impact the accessibility and 
    convenience for 
    building occupants.""",
    "description": """The territorial connection of a building can significantly impact the accessibility and 
    convenience for its 
    occupants. Buildings with good territorial connection are easily accessible and convenient for its occupants. The 
    results will 
    highlight the areas that have good or poor territorial connection, enabling a more informed decision-making 
    process in urban 
    development projects.""",
    "docs": "/docs/territorial_connection",
    "image": "static/images/energy_saving3.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

air_pollution = {
    "id": "card-image-12",
    "title": "Air Pollution",
    "simplified_title": "Pollution",
    "card_introduction": """The level of air pollution can significantly impact the health and well-being of building 
    occupants.""",
    "description": """The level of air pollution in an area can significantly impact the health and well-being of 
    building occupants. 
    High levels of air pollution can lead to respiratory issues and other health problems. The results will highlight 
    the areas with high 
    or low levels of air pollution, enabling a more informed decision-making process in urban development projects.""",
    "docs": "/docs/air_pollution",
    "image": "static/images/city_density.png",
    "badge": "In Progress",
    "src": (
        "https://speckle.xyz/embed?stream=b1603d1350&commit=a2a5e006ea&c=%5B-14.3149%2C56.02732%2C17.54074%2C0%2C43"
        ".27%2C17.23%2C0"
        "%2C1%5D&transparent=true&autoload=true&hidecontrols=true&hidesidebar=true&hideselectioninfo=true"),
    "updated": random_date()
}

congrats_intro = """
        **Congratulations** on the performance of your current assets according to this analysis! Your strategic 
        decisions 
        and careful management have led to impressive results. This analysis shows that your assets are performing 
        well, 
        which is a testament to your effective strategies and diligent management. Keep up the good work!
        
        There is more to be done, however. **The analysis shows that there is still room for improvement.** The 
        following 
        sections will provide you with some suggestions on how to improve your assets' performance.
        """

congrats_conclusion = """
        **Congratulations** on the performance of your current assets according to this analysis! Your strategic 
        decisions and careful 
        management have led to impressive results. This analysis shows that your assets are performing well, 
        which is a testament to your 
        effective strategies and diligent management. Keep up the good work!
        
        There is more to be done, however. **The analysis shows that there is still room for improvement.** The 
        following 
        sections will provide you with some suggestions on how to improve your assets' performance.
        """

description_df = pd.DataFrame({
    "facade_sun_radiation": facade_sun_radiation,
    "shadow_overcast_time": shadow_overcast_time,
    "morning_afternoon_sun_radiation": morning_afternoon_sun_radiation,
    "density": density,
    "views_availability": views_availability,
    "age_of_building": age_of_building,
    "urban_noise": urban_noise,
    "close_distance_to_green_areas": close_distance_to_green_areas,
    "potential_cost_reduction_solar_energy": potential_cost_reduction_solar_energy,
    "social_life": social_life,
    "territorial_connection": territorial_connection,
    "air_pollution": air_pollution,
}).T
