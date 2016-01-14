# -*- coding: utf-8 -*-

"""This file contains functionality for reading a CSV file."""

import csv
import logger
import os.path


class CSVManager:
    """
	This class represents a csv manager for reading csv files.
	"""

    def read(self, file_name="", seperator=";", column=[]):
        """
		This function read a csv file by given header.

		:param file_name: the file name
		:param seperator: the CSV delimiter
		:param column: the columns of csv file
		:type column: list
		:raises: *csv.Error* if CSV file is not readable
		:returns: a content of csv file as *Dict*

		Example:
			::
				from utils import csvmanager

				content = csvmanager.CSVManager().read(
					file_name="data1.csv",
					seperator=";", column=["Time", "I"])

				print content
		"""

        current_dir = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(current_dir + "/../resources/data") + "/" + file_name
        result = {}
        try:
            # read input file
            file = open(path, "rb")
            reader = csv.reader(file, delimiter=seperator)
            header = reader.next()
            # header
            for h in column:
                result[h] = []
            # content
            for row in reader:
                # match content with origin header
                [result[h].append(row[header.index(h)]) for h in column]
        except (csv.Error, ValueError) as e:
            logger.error("Can not read file %s, %s" % (file_name, e))
        return result
