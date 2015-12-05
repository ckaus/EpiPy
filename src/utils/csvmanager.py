# -*- coding: utf-8 -*-

import os.path
import csv
import logger

current_dir =  os.path.abspath(os.path.dirname(__file__))
resources_dir = os.path.abspath(current_dir + "/../../resources/data")

def read(file_name='', seperator=";", column=[]):
	"""
	This function reads a csv file.
	
	:param file_name: a file name
	:param type: str
	:param seperator: a delimiter
	:param type: str
	:param: column: readable column(s)
	:param type: list

	:returns: the content as *Dictionary*
	:raises: *Error* if csv file cannot read

	Example:
	
	data = csvmanager.read(
			file_name='liberia_data/2014-06-16.csv',
			seperator=',',
			column=['National','Date'])
	"""
	result = {}
	try:
		file = open(resources_dir+"/"+file_name, "rb")
		reader = csv.reader(file, delimiter=seperator)
		header = reader.next()
	
		if len(column) > 0: # read only given column(s)
			# header
			for c in column:
				if c in header:
					result[c] = []
			# content
			for row in reader:
				for c in column:
					result[c].append(row[header.index(c)])
		else: # read all column(s)
			# header
			for h in header:
				result[h] = []
			# content 
			for row in reader:
				# match content with header
				for h, v in zip(header, row):
					result[h].append(v)
	except csv.Error as e:
		logger.error("Can not read file %s, %s" % (filename,  e))
	return result