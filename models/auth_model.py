from flask_restx import Namespace

api = Namespace('Service Authentication', description= 'Service Key for Authentication')

token_info = api.parser()
token_info.add_argument('Registered_Email_id', location='headers')
token_info.add_argument('Secret_key', location='headers')
