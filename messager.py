# ----- intro -----

"""
This is the new and improved system for creating debug/output logs and terminal messages, using the logging library: 
https://docs.python.org/3/howto/logging.html
"""


def messager_setup():  # bundling into a function for easy import

    # ----- import necessary libraries -----

    import logging  # for messaging and automatic debug logging
    from logging.handlers import RotatingFileHandler
    import sys  # for console outputs

    # ----- maximum log file size -----

    max_log_size_mb = 500  # making 0.5 gb the maximum log file size
    max_log_size_bytes = max_log_size_mb * (10 ^ 6)  # auto-conversion to bytes

    # ----- create and configure an instance of the logger class -----
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)  # ensure that all message types are handled

    # ----- configure logging formats -----
    debug_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {filename}::{funcName}() (line {lineno}): {message}', datefmt='%m.%d %H:%M:%S', style='{')

    info_formatter = logging.Formatter(
        fmt='[{levelname}] {asctime}: {message}', datefmt='%H:%M:%S', style='{')

    warning_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {funcName}(): {message}', datefmt='%Y.%m.%d %H:%M:%S', style='{')

    critical_error_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {filename}::{funcName}() (line {lineno}): {message}', datefmt='%Y.%m.%d %H:%M:%S', style='{')

    # ----- setup level filter -----

    class singleFilter(object):
        """

        class for filtering logs to singular levels. inspired by https://stackoverflow.com/questions/8162419/python-logging-specific-level-only.

        Parameters:
        -----------

        level: logging level attribute
            logging level attribute representing the level of log to filter to (e.g. logging.DEBUG).

        """

        def __init__(self, level):
            self.level = level

        def filter(self, record):
            return record.levelno == self.level

    # ----- setup console logger handlers -----

    # for simplifying code to setup console log handlers
    console_debug_handler = logging.StreamHandler()
    console_info_handler = logging.StreamHandler()
    console_warning_handler = logging.StreamHandler()
    console_error_handler = logging.StreamHandler()
    console_critical_handler = logging.StreamHandler()

    handler_list = [
        [console_debug_handler, logging.DEBUG, debug_formatter],
        [console_info_handler, logging.INFO, info_formatter],
        [console_warning_handler, logging.WARNING, warning_formatter],
        [console_error_handler, logging.ERROR, critical_error_formatter],
        [console_critical_handler, logging.CRITICAL, critical_error_formatter]
    ]

    for entry in handler_list:
        entry[0].setLevel(entry[1])  # set the lower-bound level
        # restrict to lower-bound level
        entry[0].addFilter(singleFilter(entry[1]))
        entry[0].setFormatter(entry[2])  # set the format style
        entry[0].setStream(sys.stdout)  # set log to output to terminal

    # ----- setup file logger handlers -----

    file_all_handler = RotatingFileHandler(
        "./pytools/messenger_output/all/all.log", maxBytes=max_log_size_bytes, backupCount=10)
    file_all_handler.setLevel(logging.DEBUG)
    file_all_handler.setFormatter(critical_error_formatter)

    file_warning_up_handler = RotatingFileHandler(
        "./pytools/messenger_output/warn_up/warn_up.log", maxBytes=max_log_size_bytes, backupCount=10)
    file_warning_up_handler.setLevel(logging.WARNING)
    file_warning_up_handler.setFormatter(critical_error_formatter)

    # ----- add handlers to the logger -----

    logger.addHandler(console_debug_handler)
    logger.addHandler(console_info_handler)
    logger.addHandler(console_warning_handler)
    logger.addHandler(console_error_handler)
    logger.addHandler(console_critical_handler)
    logger.addHandler(file_all_handler)
    logger.addHandler(file_warning_up_handler)

    return logger


def clear():
    """

    clears the terminal window.

    Parameters:
    -----------

    None

    Returns:
    --------

    None

    """

    import os
    os.system('cls||clear')
