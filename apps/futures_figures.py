import numpy as np
import plotly.graph_objects as go

WIDTH, HEIGHT = 200, 150

mu, sigma = 0, 1
s = np.random.normal(mu, sigma, 1000)

fig_normal = go.Figure(data=[go.Histogram(x=s, nbinsx=30, histnorm='probability density')])
fig_normal.update_layout(
    xaxis=dict(title='Normal Distribution'),
    autosize=False,
    margin=dict(l=0, r=0, b=0, t=0, pad=0),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=WIDTH,
    height=HEIGHT,
    font=dict(
        family="Colfax",
        size=11,
        color="grey"
    )
)

fig_cum = go.Figure(data=[go.Histogram(x=s, nbinsx=30, histnorm='probability density', cumulative_enabled=True)])
fig_cum.update_layout(
    xaxis=dict(title='Cumulative Distribution'),
    autosize=False,
    margin=dict(l=0, r=0, b=0, t=0, pad=0),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=WIDTH,
    height=HEIGHT,
    font=dict(
        family="Colfax",
        size=11,
        color="grey"
    )
)

fig_normal.add_shape(
    type="rect",
    x0=0.5, y0=0,
    x1=2, y1=1,
    yref='paper',
    fillcolor="rgba(128, 128, 128, 0.8)",
    line=dict(
        width=0,
    )
)

fig_cum.add_shape(
    type="rect",
    x0=-1, y0=0,
    x1=0, y1=1,
    yref='paper',
    fillcolor="rgba(128, 128, 128, 0.8)",
    line=dict(
        width=0,
    )
)
