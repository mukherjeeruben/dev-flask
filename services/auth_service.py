from flask_restx import Resource
from flask import request, jsonify
from bl.jwt_auth import create_token
import config
from models.auth_model import api, token_info


@api.route('/key_gen')
class GenerateJwtKey(Resource):
    @api.expect(token_info)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def post(self):
        """ GENERATE JWT KEY FOR AUTHORIZATION """
        if (not request.headers['Registered_Email_id']
                and not request.headers['Secret_key']):
            return 'You are not authorized'

        incoming_key = request.headers['Secret_key']
        if incoming_key != config.Secret_key:
            return 'You are not authorized'

        user_details = [user_data for user_data in config.user_details if user_data['email'] == request.headers['Registered_Email_id']]
        if len(user_details) == 0:
            return 'User not registered. Contact Administrator.'

        token = create_token(user_details, 100, incoming_key)

        return jsonify(token)