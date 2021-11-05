import logging
from connection.postgre_con import create_connection


def execute_query(query, query_params=None):
    logging.basicConfig(level=logging.INFO)
    try:
        with create_connection() as conn:
            cursor = conn.execute(query)
            logging.info('Query Executed')
            # for get query
            result_set = cursor.fetchall()
            ## columns = cursor.description # TODO Check
            return result_set
    except Exception as exp_msg:
        logging.error("Error in Query Execution: " + str(exp_msg))



# fields = map(lambda x:x[0], cursor.description)
# result = [dict(zip(fields,row))   for row in cursor.fetchall()]