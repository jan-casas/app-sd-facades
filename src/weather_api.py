import logging
from datetime import datetime, timedelta

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import requests


def fetch_weather_data(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # for Celsius
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data


def plot_weather_figure(location, api_key):
    # Fetch the weather data
    weather_data = fetch_weather_data(location, api_key)

    # Extract relevant information
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    weather_description = weather_data['weather'][0]['description'].capitalize()
    wind_speed = weather_data['wind']['speed']
    city_name = weather_data['name']
    country = weather_data['sys']['country']
    datetime_str = datetime.fromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')

    # Create the figure
    fig = go.Figure()

    # Add temperature as a bar
    fig.add_trace(go.Bar(
        x=['Temperature'],
        y=[temperature],
        text=f"{temperature}°C",
        textposition='auto',
        name='Temperature',
        marker_color='orange'
    ))

    # Add feels like temperature
    fig.add_trace(go.Bar(
        x=['Feels Like'],
        y=[feels_like],
        text=f"{feels_like}°C",
        textposition='auto',
        name='Feels Like',
        marker_color='lightblue'
    ))

    # Add wind speed as a bar
    fig.add_trace(go.Bar(
        x=['Wind Speed'],
        y=[wind_speed],
        text=f"{wind_speed} m/s",
        textposition='auto',
        name='Wind Speed',
        marker_color='lightgreen'
    ))

    # Add humidity and pressure as separate bars
    fig.add_trace(go.Bar(
        x=['Humidity'],
        y=[humidity],
        text=f"{humidity}%",
        textposition='auto',
        name='Humidity',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=['Pressure'],
        y=[pressure],
        text=f"{pressure} hPa",
        textposition='auto',
        name='Pressure',
        marker_color='purple'
    ))

    # Update the layout
    fig.update_layout(
        title=f"Weather in {city_name}, {country} ({datetime_str})",
        xaxis_title="Weather Metrics",
        yaxis_title="Value",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True
    )

    # Add a text box with weather description
    fig.add_annotation(
        text=f"Condition: {weather_description}",
        xref="paper", yref="paper",
        x=1, y=1, showarrow=False,
        font=dict(size=14, color="black")
    )

    return fig


def fetch_historical_weather_data(location, api_key):
    try:
        # Set up the API URL (example using Visual Crossing API)
        base_url = ("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services"
                    "/timeline/")
        end_date = datetime.today()
        start_date = end_date - timedelta(days=7)  # 1 year ago

        # Request parameters
        params = {
            'unitGroup': 'metric',
            'include': 'obs',
            'key': api_key,
            'contentType': 'json'
        }

        # Make API call to get historical weather data
        url = (f"{base_url}{location}/{start_date.strftime('%Y-%m-%d')}/"
               f"{end_date.strftime('%Y-%m-%d')}")
        response = requests.get(url, params=params)
        data = response.json()

        # Extract relevant data points
        dates = []
        temperatures = []

        for day in data['days']:
            dates.append(day['datetime'])
            temperatures.append(day['temp'])

        df = pd.DataFrame({
            'Date': pd.to_datetime(dates),
            'Temperature': temperatures
        })
        logging.info(f"Fetched historical weather data for {location} with {len(df)} data points.")

        return df

    except Exception as e:
        logging.error(f"Error fetching historical weather data: {e}")
        return pd.DataFrame()


def plot_weather_histogram(df):
    # Create KDE plot
    fig = ff.create_distplot([df['Temperature']], group_labels=['Temperature'], show_hist=False)

    # Update layout
    fig.update_layout(
        title="Temperature Distribution with KDE Curve",
        xaxis_title="Temperature (°C)",
        yaxis_title="Density",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True
    )

    return fig


# Usage Example:
# Replace 'your_api_key_here' with your actual OpenWeatherMap API key.
api_key = 'b9be22730bca116ebd1c57136aa21000'
location = 'Madrid, ES'
weather_fig = plot_weather_figure(location, api_key)

"""df_weather = fetch_historical_weather_data(location, api_key)
historical_weather_fig = plot_weather_histogram(df_weather)"""
