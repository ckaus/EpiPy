# -*- coding: utf-8 -*-

"""This file contains functionality for printing messages to terminal
with different colors.
"""

import inspect


class _Color:
    ERROR = '\033[91m'  # Red
    INFO = '\033[94m'  # Blue
    NORMAL = '\033[0m'  # Default
    SUCCESS = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow


def error(msg):
    """Print error message.

    :param msg: a messages
    :type msg: str
    """
    clasz = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    func = inspect.stack()[1][3]

    print '[%s%s%s] Class: %s in %s() on line %s\n\tMessage: %s' \
          % (_Color.ERROR, 'ERROR', _Color.NORMAL, clasz, func, line, msg)


def info(msg):
    """Print information message.

    :param msg: a messages
    :type msg: str
    """
    print '[%s%s%s] %s' % (_Color.INFO, 'INFO', _Color.NORMAL, msg)


def success(msg):
    """Print success message.

    :param msg: a messages
    :type msg: str
    """
    print '[%s%s%s] %s' % (_Color.SUCCESS, 'SUCCESS', _Color.NORMAL, msg)


def warning(msg):
    """Print a warning.

    :param msg: a messages
    :type msg: str
    """
    print '[%s%s%s] %s' % (_Color.WARNING, 'WARNING', _Color.NORMAL, msg)
