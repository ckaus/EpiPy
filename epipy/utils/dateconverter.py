# -*- coding: utf-8 -*-

""" This file contains the function for converting a date array to 
    the number of days relative to the first date. """

import numpy as np
from datetime import datetime

def convert(array=[]):
    """
    :param array:
    :return:
    This function converts an array of dates to an array of relative days.

    :param array: 
    :type array: list
    :returns: a numpy array of days relative to the first date
    """

    # work with numpy array
    array = np.array(array)

    if array.size < 1:
        return array

    # the first date for the reference
    date1 = datetime.strptime(array[0], "%Y-%m-%d")
    res = []

    for datestr in array:
        date2 = datetime.strptime(datestr, "%Y-%m-%d")
        d = date2 - date1
        res.append(d.days)

    return np.array(res)