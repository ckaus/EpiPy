# -*- coding: utf-8 -*-

from basesimulator import BaseSimulator
from utils import logger
from model import sir

class SSESimulator(BaseSimulator):
	def __init__(self):
		BaseSimulator.__init__(self)
		self.name = "SSE Simulator"
		self.mode = sir
		self.data = None

	def simulation(self):
		logger.info("Start Simulation")
		return self.simulation_1()
		

	def simulation_1(self):
		logger.info("Simulation 1")
		
		# data set
		self.data = self.read_csv(
					"data1.csv",
					";",
					["Time","I"], 
					["Time", "Record"]).content

		# calculation
		def calculation(self, lsq):
			# some more calculations ...
			return sum(lsq.errors)
			
		# execute simulation
		result = self.run(1,30,5,calculation)
		logger.success("Simulation 1")
		return result