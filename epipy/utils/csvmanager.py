# -*- coding: utf-8 -*-

"""
This file contains functionality for reading a CSV file.
"""

import csv

from epipy.utils import logging


def read(file_name="", column=[]):
    """
    This function read a csv file by given header.

    :param file_name: the file name
    :type file_name: str
    :param column: the columns of csv file
    :type column: list
    :raises: *csv.Error* if csv file is not readable

    :returns: a content of csv file as *Dict*
    """

    result = {}
    try:
        # read input file
        with open(file_name, 'rb') as _csvfile:
            dialect = csv.Sniffer().sniff(_csvfile.read(), delimiters=';,')
            _csvfile.seek(0)
            reader = csv.reader(_csvfile, dialect)
            header = reader.next()
            # header
            if len(column) == 0:
                column = header
            for h in column:
                result[h] = []
                # content
            for row in reader:
                # match content with origin header
                [result[h].append(row[header.index(h)]) for h in column]
    except (csv.Error, ValueError) as e:
        logging.error("Can not read file %s, %s" % (file_name, e))
    return result
