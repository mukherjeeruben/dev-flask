import logging
from connection.postgre_con import create_connection


def execute_query(query, query_params=None):
    logging.basicConfig(level=logging.INFO)
    try:
        with create_connection() as conn:
            cursor = conn.execute(query)
            logging.info('Query Executed')

            # for 'GET' query
            columns = list(map(lambda x: x[0], cursor.cursor.description))
            row_vaules = cursor.fetchall()
            result_set = [dict(zip(columns, row)) for row in row_vaules]
            # for 'POST/PUT/DELETE' query

            ##TODO CODE PENDING

            return result_set
    except Exception as exp_msg:
        logging.error("Error in Query Execution: " + str(exp_msg))

