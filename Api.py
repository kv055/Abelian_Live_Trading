from copy import deepcopy
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

import find_parent

# from Frontend.select_exchange_connection import 
# from Frontend.select_strategy import
# from Frontend.select_strategy import 

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/Exchanges', methods=['GET'])
def get_Echanges():
    """Return an ex-parrot."""
    return{'Metadata':'DataSources()'}

@app.route('/AssetStreams', methods=['GET'])
def get_AssetStreams():
    """Return an ex-parrot."""
    return{'Metadata':'DataSources()'}

@app.route('/Strategies', methods=['GET'])
def get_Strategies():
    """Return an ex-parrot."""
    return{'Metadata':'DataSources()'}

# host='0.0.0.0'
app.run(host='localhost',port=5200,debug=True)