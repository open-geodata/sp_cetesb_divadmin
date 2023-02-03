"""
Pastas do Projeto
nov.22
"""


from pathlib import Path

project_path = Path(__file__).parents[1]

# Data
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

output_path_tab = output_path / 'tab'
output_path_tab.mkdir(exist_ok=True)

output_path_geo = output_path / 'geo'
output_path_geo.mkdir(exist_ok=True)

output_path_map = output_path / 'map'
output_path_map.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
