# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from utils import logger, csvmanager
from algorithm import Leastsquare
import sys

class BaseSimulator():
	def __init__(self):
		__metaclass__ = ABCMeta
		
	@abstractmethod
	def simulation(self):
		pass
		
	def read_csv(self, file_name, seperator, origin_fields, result_fields):
		cfo = csvmanager.CSV_File_Object(
				file_name=file_name,
				seperator=seperator,
				model="SIR")
		csv_data = csvmanager.CSV_Manager(cfo).read(
					origin_fields=origin_fields,
					result_fields=result_fields)
		return csv_data

	def run(self, start_t, end_t, steps, calc_func):
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