import dropbox
import logging
import config


def create_bucket_connection():
    '''Create bucket connection object for dropbox'''
    logging.basicConfig(level=logging.INFO)
    try:
        dbx = dropbox.Dropbox(config.DROPBOX_ACCESSTOKEN)
        logging.info('Bucket Connection Object Created')
        return dbx
    except Exception as exp_msg:
        logging.error("Bucket Connection error: " + str(exp_msg))