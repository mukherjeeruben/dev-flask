from interface.query_execution import execute_query


def get_user_details_from_db():
    query = '''SELECT * FROM "DEV".user_details'''
    result = execute_query(query=query)
    return result
