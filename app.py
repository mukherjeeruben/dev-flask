from flask import Flask
from flask_restx import Api, Resource
import config
from dal.data_fetch import data_fetch_from_api

app = Flask(__name__)

api = Api(app)

name_space = api.namespace('main', description='Main APIs')


@name_space.route("/apidatafetch")
class DatafetchClass(Resource):
    def get(self):
        json_data = data_fetch_from_api()
        return json_data


if __name__ == '__main__':
    app.run(debug=config.DEBUG)