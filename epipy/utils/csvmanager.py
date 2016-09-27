# -*- coding: utf-8 -*-

"""This file contains functionality for reading a CSV file."""

import csv
from epipy.utils import logging


def read(file_name='', column=[]):
    """Read a CSV file by given header.

    :param file_name: the file name
    :type file_name: str
    :param column: the columns of CSV file
    :type column: list
    :raises: *IOError*, *csv.Error* or *ValueError* if CSV file is not readable

    :returns: a content of CSV file
    :rtype: dict
    """
    result = {}
    if not file_name:
        return result
    try:
        # Read input file
        with open(file_name, 'rb') as _csvfile:
            dialect = csv.Sniffer().sniff(_csvfile.read(), delimiters=';,')
            _csvfile.seek(0)
            reader = csv.reader(_csvfile, dialect)
            header = reader.next()
            # Header
            if len(column) == 0:
                column = header
            for h in column:
                result[h] = []
                # Content
            for row in reader:
                # Match content with origin header
                [result[h].append(row[header.index(h)]) for h in column]
    except (IOError, csv.Error, ValueError) as e:
        logging.error('%s' % e)
        return {}
    return result
