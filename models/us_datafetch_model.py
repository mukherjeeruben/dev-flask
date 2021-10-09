from flask_restx import Namespace, reqparse, fields, inputs
from werkzeug.datastructures import FileStorage


api = Namespace('USDataFetch', description='Open data from data.ny.gov')


#For File Upload

# FILE_UPLOAD = reqparse.RequestParser(bundle_errors=True)
# FILE_UPLOAD.add_argument('file', location='files', type=FileStorage, required=True)
# FILE_UPLOAD.add_argument('overwrite', type=inputs.boolean, help="to overwrite the file", required=False)


# dummy_fields = api.model('Dummy extracted', {
#     'Year': fields.Integer(attribute='Id'),
#     'Name': fields.String(attribute='name')
#     })