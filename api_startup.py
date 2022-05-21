from flask import Flask
from flask_restx import Api
import config
from flask_cors import CORS
from interface.cache import cache

##############Import service###############
from services.auth_service import api as auth
from services.storage_service import api as app_storage
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

###########Caching##################
CACHE_CONFIG = {'CACHE_TYPE': 'SimpleCache',
                'CACHE_DEFAULT_TIMEOUT': 600}
cache.init_app(flask_app, CACHE_CONFIG)
####################################

############Append Namespace##############
API.add_namespace(auth)
API.add_namespace(app_storage)
###########################################

if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)