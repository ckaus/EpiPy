# -*- coding: utf-8 -*-

import os

cwd = os.path.dirname(os.path.realpath(__file__))


class Notification(object):
    INVALID_DATA = 'Data should be numbers like 1 or 1.0.'
    SAME_DATE_DATA = 'Date and Data columns are the same.'
    INVALID_DATE_DATA = 'Please make sure you have selected a \'Date\'\
        column.\nDates should have the following format: YYYY-MM-DD.'
    INVALID_DATA_RANGE = 'Data range and/or data range has not format: from:to'
    NO_POPULATION = 'Please define a population.'
    NO_POPULATION = 'Please define a population.'
    RESET_DATA = 'Reset all data?'
    NO_FILE = 'Please load a CSV file'
    NO_MODEL = 'Please choose a specific model.'
