from copy import deepcopy
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS


import find_parent

app = Flask(__name__)
CORS(app)
api = Api(app)

# List all available Strategies

# List all assets

# Deploy strategy
# insert config row into db

# host='0.0.0.0'
# app.run(host='localhost',port=5001,debug=True)
