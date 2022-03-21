from flask_restx import Namespace, reqparse, fields
from werkzeug.datastructures import FileStorage

api = Namespace('BucketService', description='Upload and Download Files to Bucket - Dropbox Service')

# For File Upload
FILE_UPLOAD = reqparse.RequestParser(bundle_errors=True)
FILE_UPLOAD.add_argument('file', location='files', type=FileStorage, required=True)
# FILE_UPLOAD.add_argument('overwrite', type=inputs.boolean, help="to overwrite the file", required=False)

file_download_fields = api.model('File Name', {
    'FileName': fields.String(attribute='name')
    })
