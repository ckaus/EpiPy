# -*- coding: utf-8 -*-

import os.path
import csv
import logger

current_dir =  os.path.abspath(os.path.dirname(__file__))
resources_dir = os.path.abspath(current_dir + "/../../resources/data")

def read(file_name, seperator=";", col=[]):
	"""
	This function reads a csv file.
	
	:param file_name: a file name
	:param type: str
	:param: col: readable coloumn(s)
	:param type: list

	:returns: the content as *Dictionary*
	:raises: *Error* if csv file cannot read
	"""
	
	file = open(resources_dir+"/"+file_name, "rb")
	reader = csv.reader(file, delimiter=seperator)
	result = {}
	header = reader.next()
	
	try:
		if len(col) > 0: # read only given coloumns
			# header
			for c in col:
				if c in header:
					result[c] = []
			# content
			for row in reader:
				for c in col:
					result[c].append(row[header.index(c)])
		else: # read all coloumns
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