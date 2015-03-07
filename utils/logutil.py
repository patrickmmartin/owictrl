""" simple util to set up and export a default logger """

import logging


def apply_console_handler(logger):
    """ set a console handler on the logger """
    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


LOGGER_DEFAULT = logging.getLogger('default')
LOGGER_DEFAULT.setLevel(logging.DEBUG)
apply_console_handler(LOGGER_DEFAULT)
