from flask_restx import Resource
from models.similarity_model import api, search_fields
from bl.similarity_bl import get_similarity


@api.route('/similarity')
class SimilarityScore(Resource):
    @api.expect(search_fields)
    def post(self):
        ''' get smilarity scores with respect to query'''
        payload = api.payload
        matchs = get_similarity(search_query=payload['SearchKey'])
        return matchs


