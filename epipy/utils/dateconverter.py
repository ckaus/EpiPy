# -*- coding: utf-8 -*-

<<<<<<< HEAD
"""
This file contains the function for converting a date array to the number of days relative to the first date.
"""
=======
""" This file contains the function for converting a date array to 
    the number of days relative to the first date. """
>>>>>>> origin/yena

import numpy as np
from datetime import datetime

<<<<<<< HEAD
from epipy.utils import logging


def convert(array=[]):
    """
    This function converts an array of dates to an array of relative days.
    :param array:
    :type array: list

    :returns: a numpy array of days relative to the first date
    """

    res = []
    try:
        # work with numpy array
        array = np.array(array)
=======
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

>>>>>>> origin/yena
        if array.size < 1:
            return array

        # the first date for the reference
        date1 = datetime.strptime(array[0], "%Y-%m-%d")

<<<<<<< HEAD
        for date in array:
            date2 = datetime.strptime(date, "%Y-%m-%d")
            d = date2 - date1
            res.append(d.days)

    except (TypeError, ValueError) as error:
        logging.error("Dates should have the following format: YYYY-MM-DD, %s"
                      % error)
    return np.array(res)
=======
        for datestr in array:
            date2 = datetime.strptime(datestr, "%Y-%m-%d")
            d = date2 - date1
            res.append(d.days)
            
    except (TypeError, ValueError) as e:
        logger.error("Dates should have the following format: YYYY-MM-DD, %s" % (e))

    return np.array(res)
>>>>>>> origin/yena
