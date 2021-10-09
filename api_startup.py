from flask import Flask
from flask_restx import Api
import config
from flask_cors import CORS

##############Import service###############
from services.us_datafetch_service import api as us_data


flask_app = Flask(__name__)
CORS(flask_app)
API = Api(flask_app)

############Append Namespace##############
API.add_namespace(us_data)

if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)