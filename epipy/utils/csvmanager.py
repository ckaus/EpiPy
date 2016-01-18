# -*- coding: utf-8 -*-

"""This file contains functionality for reading a CSV file."""

import csv
import logger
import os.path


def read(file_name="", seperator=";", column=[]):
    """
    :param self:
    :return:
    This function read a csv file by given header.

    :param file_name: the file name
    :param seperator: the CSV delimiter
    :param column: the columns of csv file
    :type column: list
    :raises: *csv.Error* if CSV file is not readable
    :returns: a content of csv file as *Dict*
    """

    current_dir = os.path.abspath(os.path.dirname(__file__))
    #path = os.path.abspath(current_dir + "/../resources/data") + "/" + file_name
    path = file_name
    result = {}
    try:
        # read input file
        _file = open(path, "rb")
        reader = csv.reader(_file, delimiter=seperator)
        header = reader.next()
        # header
        if not column:
            column = header
        for h in column:
            result[h] = []
        # content
        for row in reader:
            # match content with origin header
            [result[h].append(row[header.index(h)]) for h in column]
    except (csv.Error, ValueError) as e:
        logger.error("Can not read file %s, %s" % (file_name, e))
    return result
