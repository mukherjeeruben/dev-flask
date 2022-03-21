from flask import Flask
from flask_restx import Api
import config
from flask_cors import CORS
from bl.similarity_bl import set_cache

##############Import service###############
from services.image_similarity_service import api as similarity_service
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

############Append Namespace##############
API.add_namespace(auth)
API.add_namespace(app_storage)
API.add_namespace(similarity_service)
###########################################

set_cache()

if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)