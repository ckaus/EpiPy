# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from utils import csvmanager
from algorithm import Leastsquare
import sys

class BaseSimulator():
	def __init__(self):
		__metaclass__ = ABCMeta
		
	@abstractmethod
	def simulation(self):
		pass
		
	def read_csv(self, file_name, seperator, origin_fields, result_fields):
		"""
		This function read a csv file.
		:param file_name: the file name
		:type file_name: str
		:param seperator: the delimiter
		:type seperator: str
		:param origin_fields: the origin header fields
		:type origin_fields: list
		:param result_fields: the result header fields
		:type result_fields: list
		:returns: a *CSV_File_Object*
		"""

		cfo = csvmanager.CSV_File_Object(
				file_name=file_name,
				seperator=seperator,
				model="SIR")
		csv_data = csvmanager.CSV_Manager(cfo).read(
					origin_fields=origin_fields,
					result_fields=result_fields)
		return csv_data

	def run(self, start_t, end_t, steps, calc_func):
		"""
		This function start the simulation based on given calculation function.
		:param start_t: iteration start time
		:type start_t: int
		:param end_t: iteration end time
		:type end_t: int
		:param steps: iteration steps
		:type steps: int
		:param calc_func: a function who is execute by each iteration step
		:tpye calc_func: function
		:returns: dict, where key = time stamp and value = calculation result
		"""
		counter = 0
		result_list = {}
		for i in range(start_t, end_t, steps):
			counter+=1
			lsq = Leastsquare(self.mode, self.data, i)
			lsq.run()
			result_list[i] = calc_func(self, lsq)
			print '%\r',counter*(100*steps)/end_t,
			sys.stdout.flush()		
		return result_list

	def plot(self):
		logger.error("Not implemented error")
		raise NotImplementedError