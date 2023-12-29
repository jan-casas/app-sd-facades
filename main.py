'''
When you run this code and navigate to http://localhost:5000/, you’ll see the “Hello Flask” message rendered by the Flask app. If you navigate to http://localhost:5000/_dash, you’ll see the “Hello Dash” message rendered by the Dash app.
- DEFAULT ENDPOINT: Define Flask app. Define Flask API routes. Make API request and return response.
- LANDING ENDPOINT: Define Dash app. Define Dash API routes. Make API request and return response.
- RESPONSE ENDPOINT: Callbacks for Dash app. Make local API request and return response for interaction with the dashboard.
'''
from callbacks_core import *
from callbacks import (callback_modal, callback_response)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
