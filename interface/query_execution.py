import logging
from connection.postgre_con import create_connection
import sqlparse


def sql_query_type(query_string):
    '''Get Query Type'''
    query_type = str(sqlparse.parse(query_string)[0].get_type()).upper()
    return query_type


def execute_query(query, query_params=None):
    logging.basicConfig(level=logging.INFO)
    try:
        query_type = sql_query_type(query_string=query)
        with create_connection() as conn:
            if query_params == None:
                cursor = conn.execute(query)
            else:
                cursor = conn.execute(query, query_params)
            logging.info('Query Executed')
            if query_type == 'SELECT':
                columns = list(map(lambda x: x[0], cursor.cursor.description))
                row_vaules = cursor.fetchall()
                result_set = [dict(zip(columns, row)) for row in row_vaules]
            elif query_type == 'INSERT' or query_type == 'UPDATE'  or query_type == 'DELETE':
                result_set = cursor.rowcount
            elif query_type == 'ALTER':
                return 'Altered'
            return result_set
    except Exception as exp_msg:
        logging.error("Error in Query Execution: " + str(exp_msg))

