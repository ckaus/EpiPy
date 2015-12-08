# -*- coding: utf-8 -*-

"""This file contains functionality for reading a CSV file."""

import os.path
import csv
import logger

class CSV_File_Object(object):
	"""
	This class represents a CSV Object.

	:param file_name: the file name
	:type file_name: str
	:param seperator: the CSV delimiter
	:type seperator: str
	:model: the using *Model*
	:type model: str
	:returns: a *CSV_File_Object* instance
	"""

	def __init__(self, file_name, seperator, model):
		current_dir =  os.path.abspath(os.path.dirname(__file__))
		self.path = os.path.abspath(current_dir + "/../../resources/data")+"/"+file_name
		self.name = file_name
		self.seperator = seperator
		self.content = {}
		self.model = model

	def __repr__(self):
		return '<object=%s - file=%s%s seperator=%s content=%s model=%s>'\
		% (self.__class__.__name__, self.path, self.name, self.seperator, self.content, self.model)

	def content_to_float(self, header):
		"""
		This function convert the data of a *CSV_File_Object* into the data type float by given header.
		The corresponding content of the header list must be convertable. This function is not proofing the
		possibilty of converting.

		:param header: the header list
		:type header: list
		:returns: the converted content
		
		Example:
		::

			from utils import csvmanager

			cfo = csvmanager.CSV_File_Object(
					file_name="/liberia_data/2014-06-16.csv",
					seperator=",",
					model="SIR")

			csv_manager = csvmanager.CSV_Manager(cfo).read(
					origin_fields=["Date", "National"],
					result_fields=["Time", "Infected"])

			print csv_manager.content_to_float(["Infected"])
		"""

		_content = self.content
		for key, value in self.content.iteritems():
			if key in header:
				_content[key] = []
				for iv in value:
					if iv is '' or None:
						_content[key].append(0)
					else:
						_content[key].append(float(iv))
		return _content
					

class CSV_Manager(object):
	"""
	This class represents a manager for reading CSV files.

	:param csv_file_object: a *CSV_File_Object* which contains main information
	:type csv_file_object: *CSV_File_Object*
	:returns: a *CSV_Manager* instance
	"""

	def __init__(self, csv_file_object):
		self.cfo = csv_file_object

	def _convert_header(self, data, from_header, to_header):
		"""
		This function convert a given header of a data set to another header.

		:param data: the data set which represents the CSV
		:type data: *Dict*
		:param from_header: the origin header of the data set
		:type from_header: *Dict*
		:param to_header: the result header of the data set
		:type to_header: *Dict*
		:returns: the converted data set
		"""

		# change origin header to template header
		for i in range(0, len(to_header)):
			data[to_header[i]] = data.pop(from_header[i])
		return data

	def _check_fields(self, origin_fields, result_fields):
		"""
		This function check whether the origin header is equals the result header.

		:param origin_fields: the origin header
		:type origin: *Dict*
		:param result_fields: the result header
		:type result: *Dict*
		:raises: Error if headers not match
		:returns: bool if headers match
		"""

		if len(origin_fields) == 0 or len(result_fields) == 0 or len(origin_fields) != len(result_fields):
			logger.error("Origin header %s does not matching result fields %s" % (origin_fields, result_fields))
			return False
		return True

	def read(self, origin_fields=[], result_fields=[]):
		"""
		This function read a csv file by given header.

		:param origin_fields: the origin header fields
		:type origin_fields: list
		:param result_fields: the result header fields
		:type result_fields: list
		:raises: *csv.Error* if CSV file is not readable
		:returns: a *CSV_File_Object* instance

		Example:
		::

			from utils import csvmanager
			
			cfo = csvmanager.CSV_File_Object(
					file_name="/liberia_data/2014-06-16.csv",
					seperator=",",
					model="SIR")

			csv_manager = csvmanager.CSV_Manager(cfo).read(
					origin_fields=["Date", "National"],
					result_fields=["Time", "Infected"])

			print csv_manager.content
		"""

		result = {}

		if not self._check_fields(origin_fields, result_fields):
			return self.cfo

		try:
			# read input file
			file = open(self.cfo.path, "rb")
			reader = csv.reader(file, delimiter=self.cfo.seperator)
			header = reader.next()
			# header
			for h in origin_fields:
				result[h] = []
				# content 
			for row in reader:
				for h in origin_fields:
					# match content with origin header
					result[h].append(row[header.index(h)])
			self.cfo.content = self._convert_header(result, origin_fields, result_fields)
			return self.cfo
		except csv.Error as e:
			logger.error("Can not read file %s, %s" % (file_name,  e))
		return csvresult

	def __repr__(self):
		return '<object=%s - file=%s result=%s>' % (self.__class__.__name__, self.file_name, self.result)