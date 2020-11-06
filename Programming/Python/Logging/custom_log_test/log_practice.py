import logging

# setup logging
logger = logging.getLogger(__name__)
# tell which file to use
file_handler = logging.FileHandler('logfile.log')
# set format
formatter = logging.Formatter('%(asctime)s:%(levelname)s: Filename: %(filename)s: Line: %(lineno)d; %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p ')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# set level of logging to catpure
logger.setLevel(logging.CRITICAL)

# test logging
logger.debug('log debug test')
logger.info('log info test')
logger.warning('log warning test')
logger.error('log error test')
logger.critical('log critical test')