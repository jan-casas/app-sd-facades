from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output, State
from pandas import DataFrame, read_pickle
from numpy import intersect1d
from random import choice
from constants import MAPBOX_TOKEN, MAPBOX_MAP_STYLE

monoparte_centroides = read_pickle(r'database/data_experiments/monoparte.pkl')
geojson_complete = read_pickle(r'database/data_experiments/data_barrios.pkl')  # geojson_complete
geojson = geojson_complete.sample(frac=0.1, random_state=0)
propiedades_entidad = read_pickle(r'database/data_experiments/df_propiedades_entidaddes.pkl')
val_size = 0.001
number_of_colors = len(propiedades_entidad.nombre.unique())
color_stacked = ["#" + ''.join([choice('0123456789ABCDEF')
                                for j in range(6)]) for i in range(number_of_colors)]
color_landuse = ["#" + ''.join([choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(len(propiedades_entidad.currentuse.unique()))]


def update_mapbox(df, selectedpoints, df_graph):
    fig_mapa = px.scatter_mapbox(
        monoparte_centroides,
        lat=monoparte_centroides.centroid.y,
        lon=monoparte_centroides.centroid.x,
        color_discrete_sequence=["fuchsia"],
        zoom=16,
        center={"lat": 39.468217, "lon": -0.377127},
        opacity=0,

    ),

    fig_mapa[0].update_layout(
        hovermode='closest',
        dragmode='lasso',
        # mapbox_bearing=0, mapbox_pitch=50,
        mapbox_style='light',
        # mapbox_style="mapbox://styles/jancasas/clefu8dxe000401qxfxy9nhc2",
        mapbox_accesstoken="pk.eyJ1IjoiamFuY2FzYXMiLCJhIjoiY2tlYTk4ZnBlMTBwZzJ5cHhzbzBjdTltaSJ9.nYGQnvw5kkC0m0EC5eHLbg",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
        # height=1000,
        uirevision='constant',
    ),

    fig_mapa[0].update_traces(
        selectedpoints=selectedpoints,
        customdata=geojson.index,
        mode='markers',
        marker={'color': '#fabd05', 'size': 5},
        selected={'marker': {'opacity': 0.5}},
        unselected={'marker': {'opacity': 0}},
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Rockwell"
        )
    ),

    fig_años = px.scatter(
        df_graph,
        x=df_graph.numberofdwellings.fillna(0),
        y=df_graph.calculofachadas_0320_sup_fachada.fillna(0),
        color=[color_stacked[int(clase)]
               for clase in df_graph.codbarrio.fillna(0)],

        size=[val_size * int(dw)
              for dw in df_graph['longitud_fachada'].fillna(0)],
        color_discrete_sequence=color_stacked,
        render_mode="webgl",
        labels={
            "x": "Cubiertas (m2)",
            "y": "Fachadas expuestas (m2)",
            "color": "Barrio"
        },

    ),

    fig_años[0].update_layout(
        # title='Relación entre fachada y cubierta expuesta por barrio',
        titlefont=dict(size=12),
        # margin={"r": 0, "t": 20, "l": 0, "b": 20},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='#fcfcfc',
        showlegend=False,
        font=dict(color='black', size=10),
        xaxis=dict(gridcolor='#e2e2e2'), yaxis=dict(gridcolor='#e2e2e2'),
        uirevision='constant',
        hovermode='closest',
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    ),

    byClass = df_graph.groupby(['nombre', 'Clase'], as_index=False)[
        'numberofdwellings'].count()

    fig_stacked = go.Figure([
        go.Bar(
            x=byClass[byClass.nombre == byClass.nombre.unique()[
                nombres]].Clase,
            y=byClass[byClass.nombre == byClass.nombre.unique()[nombres]
                      ].numberofdwellings,
            name=byClass.nombre.unique()[nombres],
            marker_color=color_stacked[nombres]
        ) for nombres in range(len(byClass.nombre.unique()))]).update(layout_barmode='stack')

    fig_stacked.update_layout(

        # title='Construcción de viviendas por año',
        titlefont=dict(size=12),
        # margin={"r": 0, "t": 20, "l": 0, "b": 20},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='#fcfcfc',
        showlegend=True,
        font=dict(color='black', size=10),
        legend=dict(
            x=0,
            y=1.0,
        ),
        uirevision='constant',

        xaxis=dict(
            tickvals=[0, 1, 2, 3, 4, 5, 6, 7],
            ticktext=['<1900', '1900>1940', '1940>1960', '1960>1979',
                      '1979>1990', '1990<2006', '2006>2013', '>2013'],
            gridcolor='#e2e2e2'
        ),
        yaxis=dict(gridcolor='#e2e2e2'),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    )

    return fig_mapa[0], fig_años[0], fig_stacked


def blank_map(df, selectedpoints, df_graph):
    fig_mapa = px.scatter_mapbox(
        monoparte_centroides,
        lat=monoparte_centroides.centroid.y,
        lon=monoparte_centroides.centroid.x,
        color_discrete_sequence=["fuchsia"],
        zoom=6,
        center={"lat": 39.468217, "lon": -0.377127},
        opacity=0,

    ),

    fig_mapa[0].update_layout(
        hovermode='closest',
        dragmode='lasso',
        # mapbox_bearing=0, mapbox_pitch=50,
        mapbox_style='light',
        # mapbox_style="mapbox://styles/jancasas/clefu8dxe000401qxfxy9nhc2",
        mapbox_accesstoken="pk.eyJ1IjoiamFuY2FzYXMiLCJhIjoiY2tlYTk4ZnBlMTBwZzJ5cHhzbzBjdTltaSJ9.nYGQnvw5kkC0m0EC5eHLbg",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
        # height=1000,
        uirevision='constant',
    ),

    fig_mapa[0].update_traces(
        selectedpoints=selectedpoints,
        customdata=geojson.index,
        mode='markers',
        marker={'color': '#fabd05', 'size': 5},
        selected={'marker': {'opacity': 0.5}},
        unselected={'marker': {'opacity': 0}},
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Rockwell"
        )
    ),

    return fig_mapa[0]
