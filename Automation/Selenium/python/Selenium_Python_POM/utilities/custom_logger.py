# This module contains classes to help with framework
import  logging, inspect

def custom_logger(loglevel=logging.DEBUG):

    """
    Returns a logger to the calling function
    :param loglevel: default is DEBUG
    :return: logger object
    """

    # get name of method from where this is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # by default, log all messages
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s: %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p ')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger