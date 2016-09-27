# -*- coding: utf-8 -*-

"""This file contains the function for converting a date array to the number of
days relative to the first date.
"""

import numpy as np
from datetime import datetime
from epipy.utils import logging


def convert(dates):
    """Converts dates to relative days.

    :param dates:
    :type array: list
    :raises: *csv.Error* or *ValueError* if CSV file is not readable

    :returns: days relative to the first date
    :rtype: array_like
    """
    res = []
    try:
        # Work with numpy array
        dates = np.array(dates)
        if dates.size < 1:
            return dates
        # the first date for the reference
        date1 = datetime.strptime(dates[0], "%Y-%m-%d")
        for date in dates:
            date2 = datetime.strptime(date, "%Y-%m-%d")
            d = date2 - date1
            res.append(d.days)
    except (TypeError, ValueError) as error:
        logging.error('Dates should have the following format: YYYY-MM-DD, %s'
                      % error)
    return np.array(res)
