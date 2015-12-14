# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from utils import logger, csvmanager
from algorithm import Leastsquare

class BaseSimulator():
	def __init__(self):
		__metaclass__ = ABCMeta
		
	@abstractmethod
	def run(self):
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

	def _run_lsq(self, model, data, train_data_range):
		lsq_obj = Leastsquare(model, data, train_data_range)
		lsq_obj.run()
		return lsq_obj

	def plot(self):
		logger.error("Not implemented error")
		raise NotImplementedError