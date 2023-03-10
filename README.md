# CETESB

[GitHub](https://github.com/open-geodata/sp_cetesb_divadmin)

> Atualizado em 10.03.2023

<br>

_Script_ para obter a divisão administrativa da CETESB, em formato tabular.

Fiz através da iteração da consulta dos municípios por meio do formulário disponível em:

> https://licenciamento.cetesb.sp.gov.br/municipioss.asp?muni=SANTOS

<br>

Os _scripts_ também transformam o dado tabular em arquivos espaciais (_geojson_ e _gpkg_). E cria mapa _folium_...

<br>

---

### DataGeo

Após algum tempo encontrei também a delimitação das Agências Ambientais no [DataGeo](https://datageo.ambiente.sp.gov.br/). Particularmente eu prefiro consumir a fonte primária de dados, mesmo que seja mais trabalhosa para obtenção, motivo pelo qual deixo os _links_ apenas para registro.

- http://datageo.ambiente.sp.gov.br/serviceTranslator/rest/getXml/Geoserver_Publico/VWM_AGENCIA_CETESB_50_CETESB_20160201_POL/1454333714664/wms
- http://datageo.ambiente.sp.gov.br/geoserver/datageo/VWM_AGENCIA_CETESB_50_CETESB_20160201_POL/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=VWM_AGENCIA_CETESB_50_CETESB_20160201_POL

<br>

---

### _TODO_

1. Rotina para atualizar periodicamente.
