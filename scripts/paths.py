"""
Pastas do Projeto
mar.2023
"""


from pathlib import Path

# Project Path
project_path = Path(__file__).parents[1]

# Package Path
package_path = project_path / 'sp_cetesb_divadmin'

# Data
data_path = package_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

output_path_tab = output_path / 'tab'
output_path_tab.mkdir(exist_ok=True)

output_path_geojson = output_path / 'geojson'
output_path_geojson.mkdir(exist_ok=True)

output_path_gpkg = output_path / 'gpkg'
output_path_gpkg.mkdir(exist_ok=True)

output_path_map = output_path / 'map'
output_path_map.mkdir(exist_ok=True)

output_path_zip = output_path / 'zips'
output_path_zip.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
