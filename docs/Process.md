# Process

## Table of Contents

- [Recopilación de información](#recopilación-de-información)
- [Tratamiento de información GIS](#tratamiento-de-información-gis)
- [Scripting en Grasshopper](#scripting-en-grasshopper)
- [Análisis de información](#análisis-de-información)

## Recopilación de información

El proceso de trabajo se divide en dos partes, la primera parte es la obtención de la información y la segunda parte es
el análisis de la información.

### Tratamiento de información GIS

- Importación de información GIS de la ciudad de Logroño. Del portal Catastro se obtiene la información de la ciudad.
    - Edificación: Se importa la información de la edificación de la ciudad de Logroño, se clasifica la información
      teniendo en cuenta el `id_building_part` y la altura `height`.
    - Manzanas: Se procesan la capa building part para formar la capa de manzanas, a continuación se clasifica la
      información
      teniendo en cuenta el `id_manzana`.
- Segmentación de la información teniendo en cuenta una retícula (batch de ejecución), se clasifica utilizando la
  intersección entre la retícula y las manzanas, a su vez se interseccionan las manzanas con la edificación. De esta
  forma obtenemos la pertenencia del edificio `id_building_part` a la manzana `id_manzana` y la pertenencia de la
  manzana
  `id_manzana` a la
  retícula `id_batch`.
    - Retícula: Se crea una retícula de 100x100 metros, se clasifica la información teniendo en cuenta el `id_batch`.

### Scripting en Grasshopper

- Utilización del plugin Ladybug para la simulación de soleamiento, sombras y vistas.
    - Epw map locator: https://www.ladybug.tools/epwmap/
- Creación del modelo a partir de información GIS. Building parts de Logroño, crear modelo tridimensional con la
  planta y
  las alturas.
- Simulación utilizando ladybug del sun exposure, teniendo en cuenta las sombras arrojas por los edificios.
- Organización de la información obtenida en la simulación: la información debe contener el `id_building_part` del
  building part,
  la altura `height`, la orientación de la fachada `orientation` (de acuerdo a 24 vectores en el plano XY), la
  radiación recibida en la fachada `radiation`.
  La matriz de puntos (centroid mesh faces) es almacenada en un archivo `json` para su posterior uso.
- Exportación del modelo utilizando Speckle systems y exportación de la información mediante postgresql a la base de
  datos.

## Análisis de información

El análisis se divide en dos partes, la primera parte es el análisis de la información obtenida para viviendas y la
segunda parte es el análisis de la información obtenida para bajos comerciales.
Por optimización de tiempo, el volumen completo del modelo se utiliza para obstaculizar el análisis de, únicamente,
las fachadas de los edificios. No se calcula la radiación en las cubiertas, lo que sería objeto de un estudio posterior.

- Sun Exposure: Cálculo entre periodos de radiación en verano e invierno, teniendo en cuenta la posición del sol
  (radiación mínima,
  máxima y promedio). Los resultados se almacenan en `radiation_winter`, `radiation_summer` y `radiation_average`.
- Shadow Exposure: Cálculo de sombras arrojadas por los edificios en los periodos de radiación mínima, máxima y
  promedio. Los resultados se almacenan en `shadow_winter`, `shadow_summer` y `shadow_average`.
- View Exposure: Cálculo de vistas en los periodos de radiación mínima, máxima y promedio. Los resultados se
  almacenan en `percent_view`, `percent_type_view`.

## Productos resultantes

Los productos se dividen en dos partes, la primera parte es la información obtenida para viviendas y la segunda parte es
la información obtenida para bajos comerciales.

### Productos con la información obtenida para viviendas

- Los cálculos obtenidos se clasifican en dos tipos, los cálculos de radiación y los cálculos de sombras. Y se
  promocionan para el estudio informado del valor de los assets residenciales.
- Junto con la información de antigüedad de la edificación, soleamiento, sombras, vistas, centralidad y ruido podemos
  obtener un
  valor teórico de los assets residenciales.

### Productos con la información obtenida para bajos comerciales

- Los cálculos obtenidos se clasifican en dos tipos, los cálculos de radiación y los cálculos de sombras. Y se
  promocionan para el estudio informado del valor de los assets comerciales.
- Junto con la información de antigüedad de la edificación, soleamiento, sombras, vistas, ruido, y accesibilidad
  podemos
  obtener un
  valor teórico de los assets comerciales.

La información para su interacción se monta sobre una webapp desarrollado en Dash y Django utilizando Speckle para
la visualización tridimensional de la ciudad (o dash-deck) y Dash para la comparación y explicación de los resultados.

## Despliegue de la aplicación

- Contenedores de Docker: `docker-compose up`
- Contenedor de Postgres: `docker run --name postgres -e POSTGRES_PASSWORD=postgres -d postgres`
- Contenedor de Speckle: `docker run --name speckle -p 3000:3000 -d speckle/speckle-server:latest`
- Webapp de Azure: https://dash-deck.azurewebsites.net/