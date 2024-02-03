import pandas as pd
import geopandas as gpd

# load pickle file
gdf_monoparte = pd.read_pickle(r'Database/monoparte.pkl')
gdf_buildingparts = pd.read_pickle(r'Database/buildingParts.pkl')

# extract centroid from geojson file
gdf_monoparte['centroid'] = gdf_monoparte['geometry'].centroid
gdf_buildingparts['centroid'] = gdf_buildingparts['geometry'].centroid

# extract coordinates x and y from centroid
gdf_monoparte['x'] = gdf_monoparte['centroid'].x
gdf_monoparte['y'] = gdf_monoparte['centroid'].y
gdf_buildingparts['x'] = gdf_buildingparts['centroid'].x
gdf_buildingparts['y'] = gdf_buildingparts['centroid'].y
gdf_monoparte.head()

# save geojson file with pickle
gdf_monoparte.to_pickle(r'monoparte.pkl')
gdf_buildingparts.to_pickle(r'buildingParts.pkl')
