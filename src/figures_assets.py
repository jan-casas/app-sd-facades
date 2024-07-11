import plotly.graph_objects as go
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import sys
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import dash

from core_callbacks import app, dash_app

sys.path.insert(0, '../core_callbacks.py')


def random_normal_distribution(loc: list, scale: list, size: int, n: int) -> tuple:
    '''
    Generate random normal distribution
    '''
    random_distribution = []
    for i in range(n):
        random_distribution.append(np.random.normal(
            loc=loc[i], scale=scale[i], size=size))

    # create a cumulative sum of the random distribution
    cum_sum_nd = []
    for i in range(len(random_distribution)):
        cum_sum_nd.append(np.histogram(random_distribution[i], bins=100)[1])
    return random_distribution, cum_sum_nd


def random_color(n):
    '''
    Generate random colors
    '''
    import random
    colors = []
    for i in range(n):
        colors.append('#%06X' % random.randint(0, 0xFFFFFF))

    return colors


# Instate values
hist_data, cumsum_data = random_normal_distribution(
    [5, 10, 15], [1, 2, 1], 1000, 3)
group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = random_color(3)


def create_random_df():
    # create a empty df with the fields 'day', 'people', 'hour', 'temp'
    df = pd.DataFrame(columns=['day', 'people', 'hour', 'temp', 'noise'])
    # add normal distirbution values to the df in the field people and temp
    # the field people cannot be negative has to be integer with minimum 1 and maximum 100
    # random integer values between 1 and 100
    # select random values from the list
    df['month'] = np.random.choice(['January', 'February', 'March', 'April', 'May',
                                    'June', 'July', 'August', 'September', 'October', 'November', 'December'], 1000)
    df['people'] = np.random.randint(1, 100, 1000)
    df['temp'] = np.random.normal(loc=1, scale=1, size=1000)
    # df['temp'] = np.random.randint(17, 34, 1000)
    # remap the values of the field temp to the min and max values of the field people
    df['temp'] = df['temp'].apply(lambda x: (x - df['temp'].min()) / (df['temp'].max(
    ) - df['temp'].min()) * (df['people'].max() - df['people'].min()) + df['people'].min())

    x1 = np.random.gamma(1, 1, 500)
    x2 = np.random.gamma(6, 4, 500)
    df['noise'] = np.concatenate([x1, x2])

    # remap the values of the field noise to the min and max values of the field people
    df[''] = df['noise'].apply(lambda x: (x - df['noise'].min()) / (df['noise'].max() -
                                                                    df['noise'].min()) * (
                                                 df['people'].max() - df['people'].min()) + df['people'].min())

    # add random values to the fields day and hour
    df['day'] = np.random.choice(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 1000)
    df['hour'] = np.random.choice(range(8, 20, 2), 1000)

    return df


def distribution(df):
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                             bin_size=.2, show_rug=False)
    fig.update_layout(template="ggplot2")  # add theme to plot
    fig.update_layout(legend=dict(
        yanchor="top", y=0.99,
        xanchor="left", x=0.01
    ))  # move legend
    # remove background color
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    # remove margin
    fig.update_layout(margin=dict(l=0, r=0, t=20, b=20))

    return fig


def update_subplot(hist_data, group_labels, colors, cumsum_data):
    # Create distplot with curve_type set to 'normal'

    # create a plot with the cumsum_data values
    fig = go.Figure()
    for i in range(len(cumsum_data)):
        fig.add_trace(go.Scatter(x=np.arange(0, len(
            cumsum_data[i])), y=cumsum_data[i], name=group_labels[i], line=dict(color=colors[i], width=2)))
    fig.update_layout(template="ggplot2")
    fig.update_layout(legend=dict(
        yanchor="top", y=0.99,
        xanchor="left", x=0.01
    ))
    # remove background color
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=20))

    return fig


# update_subplot(hist_data, group_labels, colors, cumsum_data)


def weekly_time(df):
    fig = make_subplots(rows=1, cols=2, shared_yaxes=False,
                        subplot_titles=("Semana", "Horas"))

    # fig = go.Figure()
    # create a violin plot with the fields day and people
    fig.add_trace(go.Violin(x=df['people'], y=df['day'],
                            name='people', side='negative'), row=1, col=1)
    # create a violin plot with the fields day and temp
    fig.add_trace(go.Violin(
        x=df['temp'], y=df['day'], name='temp', side='positive', opacity=0.5), row=1, col=1)
    fig.add_trace(go.Violin(x=df['noise'], y=df['day'],
                            name='noise', side='positive', opacity=0.5), row=1, col=1)

    # add theme to plot
    fig.update_traces(meanline_visible=True, orientation='h')
    # remove background color
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=20))

    # create a violin plot with the fields day and people
    fig.add_trace(go.Violin(x=df['people'], y=df['hour'],
                            name='people', side='negative'), row=1, col=2)
    # create a violin plot with the fields day and temp
    fig.add_trace(go.Violin(x=df['temp'], y=df['hour'],
                            name='temp', side='positive', opacity=0.5), row=1, col=2)
    fig.add_trace(go.Violin(x=df['noise'], y=df['hour'],
                            name='noise', side='positive', opacity=0.5), row=1, col=2)

    # add theme to plot
    fig.update_traces(meanline_visible=True, orientation='h')
    # change vertical size
    # fig.update_layout(height=800, width=400)
    # change vertical axis labels

    # move legend
    fig.update_layout(template="ggplot2")
    # remove background color
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(l=0, r=0, t=20, b=20))
    # add title
    # fig.update_layout(title_text="Distribuição de pessoas por dia e hora")

    # modify the layout width and height
    # fig.update_layout(height=800, width=600)

    return fig


weekly_time = weekly_time(create_random_df())


def monthly_heatmap(df):
    '''
    Create a montly density heatmap
    '''

    fig = go.Figure(data=go.Heatmap(
        z=round(df['temp'], 1),
        x=df['day'],
        y=df['hour'],
        colorscale='RdBu_r',
        zmin=0,
        zmax=100,
        texttemplate="%{z}"
    ))
    fig.update_layout(template="ggplot2")
    # fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    fig.update_layout(showlegend=False)
    fig.update_layout(
        xaxis=dict(autorange=True),  # Enable autoscale for x-axis
        yaxis=dict(autorange=True)  # Enable autoscale for y-axis
    )
    return fig


# monthly_heatmap = monthly_heatmap(create_random_df(), 'January')


@dash_app.callback(
    dash.dependencies.Output('monthly_heatmap', 'figure'),
    [dash.dependencies.Input('dropdown_fachadas', 'value')]
)
def update_montly_heatmap(dropdown_fachadas):
    montly = monthly_heatmap(create_random_df())
    return montly


def daily_distribution(df):
    '''
    Create a violin plot with the fields hour,temp and noise
    '''

    fig = go.Figure()
    # filter the df for the field hour and the value 8
    df = df[df['hour'] == 8]
    fig.add_trace(go.Violin(x=df['temp'], y=df['hour'],
                            name='temp', side='positive', opacity=0.5))
    fig.add_trace(go.Violin(x=df['noise'], y=df['hour'],
                            name='noise', side='positive', opacity=0.5))
    fig.add_trace(go.Violin(x=df['people'], y=df['hour'],
                            name='people', side='negative', opacity=0.5))
    # add theme to plot
    fig.update_traces(meanline_visible=True, orientation='h')
    # change vertical size
    # fig.update_layout(height=300, width=600)
    # change vertical axis labels
    # fig.update_yaxes(tickvals=[0, 1, 2], ticktext=['temp', 'noise', 'people'])
    # move legend
    fig.update_layout(template="ggplot2")
    # remove background color
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(margin=dict(l=0, r=0, t=20, b=20))

    return fig

# daily_distribution = daily_distribution(df)
