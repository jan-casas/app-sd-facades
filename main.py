from core_callbacks import *
from callbacks import (callback_modal, callback_response, callback_login, callback_chat)

# TODO:
"""
Load section:
- Bake urban data in postgres and read geojson from server not in local (query done)

- Display real data in tables
Home section:
- Bake the analytic example models in Speckle and link them to the app

Assets section:
- Create the functionality to compare your current assets at scale

Explore preferences:
- Add graphs to filter the data
- Add a kind of "search copilot" functionality to filter the data by natural language
"""

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
