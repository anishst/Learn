# https://www.youtube.com/watch?v=jxmzY9soFXg&t=605s

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

import logging, inspect

def custom_logger(loglevel=logging.DEBUG):

    logger = logging.getLogger(__name__)
    logger.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s: Filename: %(filename)s: Line: %(lineno)d; %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p ')

    file_handler = logging.FileHandler('custom.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        log = custom_logger()

        log.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

