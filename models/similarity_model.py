from flask_restx import Namespace, fields


api = Namespace('SimilarityService', description='get data from master database')


search_fields = api.model('Search Key word',
                                 {'SearchKey': fields.String(attribute='name')})