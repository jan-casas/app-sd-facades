import pandas as pd
import plotly.express as px
import math as math
from statistics import mean
import json
import geopandas as gpd
import numpy as np

data_barrios = gpd.read_file(
    r'D:\casas\Documents\Proyectos\AOS\FACHADAS\analysis_facade-street\01-geodata\geodata-inicial\BARRIOS.geojson')
data_barrios['geometry'] = data_barrios['geometry'].centroid

data_barrios.to_file(r"C:\Users\casas\Desktop\extract-windows\01-geodata\geodata-generada\data_barrios.geojson",
                     driver="GeoJSON")

csv = pd.read_csv(
    r'D:\casas\Documents\Proyectos\AOS\FACHADAS\analysis_facade-street\02-datasets\datasets-inicial\BARRIOS.csv',
    sep=',', decimal=',', dtype={'localId': str})
csv['calculoFachadas_0320_sup_fachada'] = csv['calculoFachadas_0320_sup_fachada'].replace(np.nan, 0)
csv['calculoFachadas_0320_sup_fachada'] = csv['calculoFachadas_0320_sup_fachada'].astype(int)

rang = list(range(0, 10, 1))
rang = [x / 10 for x in rang]
print(rang)
csv['quantile'] = pd.qcut(
    csv['calculoFachadas_0320_sup_fachada'],
    q=[0, .25, .5, .75, 1],
    labels=False, precision=0,
    duplicates='drop'
)

csv['gml_id_parts'] = csv['gml_id']
csv['gml_id'] = [part.split('_')[0] for part in csv['gml_id']]

# Edad edificación
edad_edificación = pd.read_excel(
    r'D:\casas\Documents\Proyectos\AOS\FACHADAS\analysis_facade-street\02-datasets\datasets-inicial\BB_EE_Barrios.xlsx')
edad_edificación.drop_duplicates(subset="gml_id", keep=False, inplace=True)

propiedades_entidad = pd.merge(csv, edad_edificación, on="gml_id", how="left")

DIR_TOTAL = r'D:\casas\Documents\Proyectos\AOS\FACHADAS\analysis_facade-street\02-datasets\datasets-generados\edificacion_coste_orientacion.csv'

df_propiedades_entidaddes = pd.read_csv(DIR_TOTAL)
df_propiedades_entidaddes = df_propiedades_entidaddes.drop(['Unnamed: 0', 'gml_id_y', 'id'], axis=1)
df_propiedades_entidaddes = df_propiedades_entidaddes.fillna(-1)

Classify = df_propiedades_entidaddes['edad'].astype(int)

num = []
for age in Classify:
    if age <= 1900:
        num.append("0")
    elif age > 1900 and age <= 1940:
        num.append("1")
    elif age > 1940 and age <= 1960:
        num.append("2")
    elif age > 1960 and age <= 1979:
        num.append("3")
    elif age > 1979 and age <= 1990:
        num.append("4")
    elif age > 1990 and age <= 2006:
        num.append("5")
    elif age > 2006 and age <= 2013:
        num.append("6")
    elif age > 2013:
        num.append("7")
    else:
        num.append("null")

df_propiedades_entidaddes.insert(len(df_propiedades_entidaddes.columns), 'Clase', pd.DataFrame(num))


def remap_dataframe(dataframe, field_name_to_sample, target_domain, new_field_name):
    low2, high2 = target_domain[0], target_domain[1]
    low1 = min(dataframe[field_name_to_sample].values)
    high1 = max(dataframe[field_name_to_sample].values)
    value = dataframe[field_name_to_sample].values

    dataframe[new_field_name] = low2 + (value - low1) * (high2 - low2) / (high1 - low1)

    return print('remap done!')


remap_dataframe(df_propiedades_entidaddes, 'orientacion_fachada', [0, 360], 'polar_coord')

df_propiedades_entidaddes.to_csv(
    r'D:\casas\Documents\Proyectos\AOS\FACHADAS\analysis_facade-street\02-datasets\datasets-generados\df_propiedades_entidaddes.csv')

sumClass = propiedades_entidad.groupby(['Clase'], as_index=False)['numberOfDw'].sum()
totalSumClass = int(sumClass.numberOfDw.sum())
acumulativeDw = sumClass.numberOfDw.cumsum()
percentage = (sumClass.numberOfDw / totalSumClass) * 100
acumulativeSum = percentage.cumsum()

sumClass.insert(2, 'Acumulative Dw', acumulativeDw)
sumClass.insert(3, 'Percentage', percentage)
sumClass.insert(4, 'Acumulative Sum', acumulativeSum)
