# -*- coding: utf-8 -*-

import os.path
import csv
import logger

current_dir =  os.path.abspath(os.path.dirname(__file__))
resources_dir = os.path.abspath(current_dir + "/../../resources/data")
	
class Template:
	"""Valid CSV templates"""
	from collections import OrderedDict
	# python sort dictionary keys, thats why I use OrderedDict
	# http://stackoverflow.com/questions/1867861/python-dictionary-keep-keys-values-in-same-order-as-declared
	SIR = OrderedDict([("Time", []), ("Suspectable", []), ("Infected", []), ("Recovered", [])])
	
def _check_header_fields(header, template):
	"""
	This function checks if the header match the template.
	
	:param header: a CSV header
	:param type: list of str
	:param template: a CSV template
	:param type: *Template*

	:returns True if the header match the template header: 
	"""

	for h in header:
		if h not in template.keys():
			logger.error('Given header field %s not exist in template: %s'
				% (h, template))
			return False
	return True
	
def read(file_name, template, header_fields, seperator=';'):
	"""
	This function reads a CSV file.
	
	:param file_name: a file name
	:param type: str
	:param template: a CSV template
	:param type: *Template*
	:param: header_fields: header fields must match *Template*
	:param type: list of str
	:param seperator: a delimiter
	:param type: str
	:returns: the content of CSV as *Dictionary*
	:raises: *Error* if csv file cannot read
			or header fields not match template
	Example:

	data = csvmanager.read(file_name='data1.csv', 
			template=csvmanager.Template.SIR, 
			seperator=';', 
			header_fields=["Time","Recovered"])
	"""

	result = {}
	try:
		# read input file
		file = open(resources_dir+"/"+file_name, "rb")
		reader = csv.reader(file, delimiter=seperator)
		result = {}
		header = reader.next()
		
		if len(header_fields) > 0:
			# use given header fields as header
			header = header_fields

		if _check_header_fields(header,template):
			# header
			for h in header:
				result[h] = []
			# content 
			reader.next() # jump to content of csv
			for row in reader:
				for h in header:
					# match content with header
					result[h].append(row[template.keys().index(h)])
		return result
	except csv.Error as e:
		logger.error("Can not read file %s, %s" % (filename,  e))