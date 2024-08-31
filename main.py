import logging
import sys

from core_callbacks import *
from callbacks import (callback_response, callback_chat)
# from callbacks import (callback_modal, callback_response, callback_chat)

# TODO:
# Añadir matriz con la distribución (curve) de cada variable y la posición de la variable
# seleccionada
"""
Load section:
- Bake urban data in postgres and read geojson from server not in local (query done)
- Display real data in tables

Home section:
- Bake the analytic example models in Speckle and link them to the app

Assets section:
- Create the functionality to compare your current assets at scale
[X]- Add graphs to show more valuable information -> Current graph must display the analysis 
types not the cities (it filter when the table value is selected). Add graph about building age, 
building type, etc.
- Filter table data with the parallel graph



---- OPTIONAL ----
Explore preferences:
- Add graphs to filter the data
- Add a kind of "search copilot" functionality to filter the data by natural language
"""

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
