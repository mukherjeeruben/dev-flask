from flask_restx import Resource
from models.storage_model import api, FILE_UPLOAD, file_download_fields
from bl.jwt_auth import token_required
from bl.drop_box_bucket import upload_file, download_file, get_file_list
from interface.cache import cache


@api.route('/uplaodfile')
class UplaodFileClass(Resource):
    @token_required
    @api.doc(response={200: 'Success', 400: 'Validation Error'}, security='apikey')
    @api.expect(FILE_UPLOAD)
    @api.response('default', 'Error')
    def post(self):
        '''Upload File service to dropbox'''
        args = FILE_UPLOAD.parse_args()
        uploaded_file = args['file']
        response = upload_file(uploaded_file)
        return response


@api.route('/downloadfile')
class DownloadFileClass(Resource):
    @token_required
    @api.doc(response={200: 'Success', 400: 'Validation Error'}, security='apikey')
    @api.expect(file_download_fields)
    @api.response('default', 'Error')
    def post(self):
        '''Download File service from dropbox'''
        payload = api.payload
        response = download_file(filename=payload['FileName'])
        return response


@api.route('/getfilelist')
class FetchFileListClass(Resource):
    @cache.memoize(timeout=300)
    @token_required
    @api.doc(response={200: 'Success', 400: 'Validation Error'}, security='apikey')
    @api.response('default', 'Error')
    def get(self):
        '''Get File List from dropbox'''
        response = get_file_list()
        return response

