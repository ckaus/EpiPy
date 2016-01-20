# -*- coding: utf-8 -*-

""" This file contains the function for converting a date array to
    the number of days relative to the first date. """

import numpy as np
from datetime import datetime

from epipy.utils import logger


def convert(array=[]):
    """
    :param array:
    :return:
    This function converts an array of dates to an array of relative days.

    :param array:
    :type array: list
    :returns: a numpy array of days relative to the first date
    """
    res = []
    try:
        # work with numpy array
        array = np.array(array)
        if array.size < 1:
            return array

        # the first date for the reference
        date1 = datetime.strptime(array[0], "%Y-%m-%d")

        for datestr in array:
            date2 = datetime.strptime(datestr, "%Y-%m-%d")
            d = date2 - date1
            res.append(d.days)

    except (TypeError, ValueError) as error:
        logger.error("Dates should have the following format: YYYY-MM-DD, %s"
                     % error)
    return np.array(res)
