# -*- coding: utf-8 -*-

from basesimulator import BaseSimulator

class SSESimulator(BaseSimulator):
	def __init__(self):
		BaseSimulator.__init__(self)
		self.name = "SSE Simulator"

	def run(self, file_path):
		self.read_file(file_path)
		return None