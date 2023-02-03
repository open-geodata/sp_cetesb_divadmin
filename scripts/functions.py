"""
Summary
"""

from open_geodata import geo


# List Datasets (dataframes and geodataframes)
list_data = geo.get_dataset_names()
print(list_data)

# Load Dataset
df_mun = geo.load_dataset('tab.sp.tab_municipio_nome')

# Load Data
gdf_sp = geo.load_dataset('geo.sp.sp_250k_wgs84')

# Adjust
gdf_sp.drop(['municipio_nome'], axis=1, inplace=True)
gdf_sp['id_municipio'] = gdf_sp['id_municipio'].astype(int)
gdf_sp['geometry'] = gdf_sp.simplify(0.0015)

# Results
print(gdf_sp.head())
