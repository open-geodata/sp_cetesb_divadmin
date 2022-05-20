from open_geodata import geo


df_mun = geo.load_dataset('tab_municipio_nome')



# Load Data
gdf_sp = geo.load_dataset('sp_250k_wgs84')

# Adjust
gdf_sp.drop(['municipio_nome'], axis=1, inplace=True)
gdf_sp['id_municipio'] = gdf_sp['id_municipio'].astype(int)
gdf_sp['geometry'] = gdf_sp.simplify(0.0015)

# Results
gdf_sp.head()