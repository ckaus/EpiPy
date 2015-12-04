# -*- coding: utf-8 -*-

import os.path
import csv
import logger

current_dir =  os.path.abspath(os.path.dirname(__file__))
resources_dir = os.path.abspath(current_dir + "/../../resources")

def read(file_name, seperator=";"):
	"""
	This function reads a csv file.
	
	:param file_name: a file name
	:param type: str
	
	:returns: the content as *Dictionary*
	:raises: *Error* if csv file cannot read
	"""
	
	file = open(resources_dir+"/"+file_name, "rb")
	reader = csv.reader(file, delimiter=seperator)
	result = {}
	header = reader.next()
	# read header
	try:
		for h in header:
			result[h] = []
		# read content 
		for row in reader:
			# match with header field
			for h, v in zip(header, row):
				result[h].append(float(v))
	except csv.Error as e:
		logger.error("Can not read file %s, %s" % (filename,  e))
	return result