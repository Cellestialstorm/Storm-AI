import logging
from flask import Flask, jsonify
from flask_cors import CORS
from desktop_ui.state import get_ui_state

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

CORS(app, resources={r"/state": {"origins": "*"}})

@app.route("/state")
def state():
    return jsonify(get_ui_state())

def start_ui_server():
    app.run(
        host="127.0.0.1",
        port=8765,
        debug=False,
        use_reloader=False
    )