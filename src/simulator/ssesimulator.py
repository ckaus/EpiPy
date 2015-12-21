# -*- coding: utf-8 -*-

from basesimulator import BaseSimulator
from utils import logger
from model import sir
import numpy

class SSESimulator(BaseSimulator):
	def __init__(self):
		BaseSimulator.__init__(self)
		self.name = "SSE Simulator"
		self.model = sir
		self.data = None

	def simulation(self, with_plot=True):
		logger.info("Start Simulation")
		return self.simulation_1(with_plot)
		

	def simulation_1(self, with_plot):
		logger.info("Simulation 1")
		
		# data set
		self.data = self.read_csv(
					"data1.csv",
					";",
					["Time","I"], 
					["Time", "Record"]).content

		# calculate the sum of all sse
		def calculation(self, lsq):
			return mean(lsq.errors)
			
		# execute simulation
		result = self.run(30,80,2,calculation)
		
		if with_plot:
			# build graph for plotting result
			graph = [[],[]]
			for k,v in result.iteritems():
				graph[0].append(k)
				graph[1].append(v)
			self.plot_graph(graph)
		else:
			# print '--'
			print result
		
		logger.success("Simulation 1")
		# plot graph
		return result