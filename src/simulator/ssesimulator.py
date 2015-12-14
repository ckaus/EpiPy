# -*- coding: utf-8 -*-

from basesimulator import BaseSimulator
from utils import logger
from model import sir

class SSESimulator(BaseSimulator):
	def __init__(self):
		BaseSimulator.__init__(self)
		self.name = "SSE Simulator"
		self.mode = sir

	def run(self):
		logger.info("Start Simulation 1")
		error_list = {}
		csv_obj = self.read_csv(
					"data1.csv",
					";",
					["Time","I"], 
					["Time", "Record"])
		
		for i in range(1,30,2):
			lsq = self._run_lsq(sir, csv_obj.content, i)
			error_list[i] = lsq.errors
		logger.success("End Simulation 1")
		return error_list		