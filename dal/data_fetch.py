from interface.query_execution import execute_query


def get_all_image_data():
    query = '''SELECT embeddings_vector, image_url FROM "DEV".table_image_master WHERE embeddings_vector IS NOT NULL '''
    result = execute_query(query=query)
    return result