import logging
from sqlalchemy import create_engine
import config


def create_connection():
    '''Create sqlalchemy connection object for postgresql'''
    logging.basicConfig(level=logging.INFO)

    user = config.POSTGRESQL_USER
    password = config.POSTGRESQL_PASSWORD
    host = config.POSTGRESQL_HOST
    port = config.POSTGRESQL_PORT
    database = config.POSTGRESQL_DATABASE
    db_string = "postgres://" + user + ":" + password + "@" + host + ":" + port + "/" + database
    # Fix for Heroku database service connection
    if db_string.startswith("postgres://"):
        db_string = db_string.replace("postgres://", "postgresql://", 1)
    try:
        db = create_engine(db_string)
        logging.info('Database Engine Created')
        conn_obj = db.connect()
        logging.info('Database Connection Object Created')
        return conn_obj
    except Exception as exp_msg:
        logging.error("Database Connection error: " + str(exp_msg))











