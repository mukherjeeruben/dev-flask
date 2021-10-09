from flask_restx import Resource
from models.us_datafetch_model import api
from bl.us_datafetch_bl import api_datafetch_factoring


@api.route('/jobsbyindustry')
class dummy(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    # @api.marshal_with(dummy_fields)
    @api.response('default', 'Error')
    def get(self):
        '''This data shows jobs by industry, beginning in 2012, created from a dataset of economic profiles of the 10 Empire State Development (ESD) economic development regions. Refer to the About section for the data dictionary and other information.'''

        '''NY Open Data'''
        response = api_datafetch_factoring()
        return response


