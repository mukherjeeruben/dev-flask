from flask import Flask
from flask_restx import Api, Resource
import config
from dal.data_fetch import data_fetch_from_api

flask_app = Flask(__name__)

api = Api(flask_app)

name_space = api.namespace('main', description='Main APIs')


@name_space.route("/jobsbyindustry")
class DatafetchClass(Resource):
    def get(self):
        '''This data shows jobs by industry, beginning in 2012, created from a dataset of economic profiles of the 10 Empire State Development (ESD) economic development regions. Refer to the About section for the data dictionary and other information.'''

        '''NY Open Data'''

        dataset_list = list()
        json_data = data_fetch_from_api(config.jobs_by_industry_api_url)
        for raw_rowdata in json_data:
            rowdata = dict()
            rowdata['Year'] = raw_rowdata[8]
            rowdata['Region'] = raw_rowdata[9]
            rowdata['NAICS Code'] = raw_rowdata[10]
            rowdata['Industry'] = raw_rowdata[11]
            rowdata['Jobs'] = raw_rowdata[12]
            dataset_list.append(rowdata)
        return dataset_list


if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)