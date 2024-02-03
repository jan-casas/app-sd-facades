from callbacks_core import *
from callbacks import (callback_modal, callback_response, callback_login, callback_chat)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
