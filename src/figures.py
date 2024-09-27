import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

from utils.utils_database import fetch_data_from_db


def update_layout(fig, num_rows, title_text, background_color='rgba(0,0,0,0)', show_xaxis=True,
                  show_yaxis=True, legend_orientation='h', legend_y=-0.1, axis_color='lightgray',
                  **kwargs):
    layout_params = {
        'height': 250 * num_rows,
        'title_text': title_text,
        'showlegend': True,
        'legend': {'orientation': legend_orientation, 'y': legend_y, 'x': 0.5, 'xanchor': 'center'},
        'paper_bgcolor': background_color,
        'plot_bgcolor': background_color,
        'xaxis': {'visible': show_xaxis, 'showline': True, 'zeroline': True,
                  'linecolor': axis_color, 'zerolinecolor': axis_color},
        'yaxis': {'visible': show_yaxis, 'showline': True, 'zeroline': True,
                  'linecolor': axis_color, 'zerolinecolor': axis_color},
        'margin': {'l': 0, 'r': 0, 't': 20, 'b': 0},
    }
    layout_params.update(kwargs)
    fig.update_layout(**layout_params)

    # Apply the same layout settings to all subplots if the figure has subplots
    if hasattr(fig, '_grid_ref'):
        for i in range(1, num_rows + 1):
            fig.update_xaxes(linecolor=axis_color, zerolinecolor=axis_color, row=i)
            fig.update_yaxes(linecolor=axis_color, zerolinecolor=axis_color, row=i)
    else:
        fig.update_xaxes(linecolor=axis_color, zerolinecolor=axis_color)
        fig.update_yaxes(linecolor=axis_color, zerolinecolor=axis_color)


def create_subplots(df, plot_func, title_text, **kwargs):
    df = df.round(2)
    subplot_titles = [col.replace('_', ' ').title() for col in df.columns]

    df_numeric = df.select_dtypes(include=[np.number])
    num_cols = 4
    num_rows = (len(df_numeric.columns) + num_cols - 1) // num_cols
    fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=subplot_titles,
                        shared_yaxes=False, shared_xaxes=False, vertical_spacing=0.1,
                        )

    for i, col in enumerate(df_numeric.columns):
        row = i // num_cols + 1
        col_pos = i % num_cols + 1
        show_legend = (i == 0)  # Only show legend for the first subplot
        plot_func(fig, df_numeric[col], row, col_pos, show_legend)

    update_layout(fig, num_rows, title_text, **kwargs)
    return fig


def get_blue_palette(n_colors=3):
    cmap = plt.get_cmap('Blues')
    colors = [mcolors.to_hex(cmap(i / (n_colors + 1))) for i in range(1, n_colors + 1)]
    return colors


def add_vertical_lines(fig, row, col, mean, median, q1, q3, show_legend):
    colors = get_blue_palette()
    mean_color, median_color, quartile_color = colors

    fig.add_vline(x=mean, line_width=2, line_dash='dash', line_color=mean_color,
                  annotation_text=f"Mean: {mean:.2f}", annotation_position="top left",
                  row=row, col=col, legendgroup='vertical_lines', name='Mean',
                  showlegend=show_legend)
    fig.add_vline(x=median, line_width=2, line_dash='dot', line_color=median_color,
                  annotation_text=f"Median: {median:.2f}", annotation_position="top right",
                  row=row, col=col, legendgroup='vertical_lines', name='Median',
                  showlegend=show_legend)
    fig.add_vline(x=q1, line_width=1, line_dash='dashdot', line_color=quartile_color,
                  annotation_text=f"Q1: {q1:.2f}", annotation_position="bottom left",
                  row=row, col=col, legendgroup='vertical_lines', name='Q1',
                  showlegend=show_legend)
    fig.add_vline(x=q3, line_width=1, line_dash='dashdot', line_color=quartile_color,
                  annotation_text=f"Q3: {q3:.2f}", annotation_position="bottom right",
                  row=row, col=col, legendgroup='vertical_lines', name='Q3',
                  showlegend=show_legend)


def plot_combined(fig, data, row, col, show_legend):
    data = data.round(2)

    # Distribution plot
    hist_data = [data.dropna().values]
    group_labels = ['KDE']
    colors = ['#333F44']
    distplot = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

    # Add KDE traces, but only show legend for the first trace
    for i, trace in enumerate(distplot.data):
        trace.update(legendgroup='kde', name='KDE', showlegend=(i == 0 and show_legend))
        fig.add_trace(trace, row=row, col=col)

    mean = data.mean()
    median = data.median()
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)

    add_vertical_lines(fig, row, col, mean, median, q1, q3, show_legend)

    # KDE and CDF plot
    kde_fig = ff.create_distplot([data.dropna()], ['KDE'], show_hist=False)
    for i, trace in enumerate(kde_fig.data):
        trace.update(legendgroup='kde', name='KDE', showlegend=False)
        fig.add_trace(trace, row=row, col=col)
    cdf_fig = px.ecdf(data_frame=data.to_frame(), x=data.name)
    for i, trace in enumerate(cdf_fig.data):
        trace.update(legendgroup='cdf', name='CDF', showlegend=(i == 0 and show_legend))
        fig.add_trace(trace, row=row, col=col)


# Initialise figures
df = fetch_data_from_db(query="SELECT * FROM city_simulations.simulation_results").round(2)
kde_cdf_fig = create_subplots(df, plot_combined,
                              "")
