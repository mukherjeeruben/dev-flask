from flask import Flask
from flask_restx import Api
import config
from flask_cors import CORS

##############Import service###############
from services.us_datafetch_service import api as us_data
from services.auth_service import api as auth
###########################################
############Authentication Model############
AUTH = {
    'apikey' :{
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization'
    }
}
#############################################

flask_app = Flask(__name__)
CORS(flask_app)
API = Api(flask_app, authorizations=AUTH)

############Append Namespace##############
API.add_namespace(auth)
API.add_namespace(us_data)
###########################################

if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)