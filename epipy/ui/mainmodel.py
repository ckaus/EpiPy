# -*- coding: utf-8 -*-

import numpy as np

class MainModel(object):
	def __init__(self):
		self.x_data = None
		self.y_data = None
		self.fit_data = None
		self.poputlation = None
		self.epidemic_model = None

	def set_data_set(self, x_data, y_data, population):
		self.x_data = x_data
		self.y_data = y_data
		self.population = population
	
	def get_x_data():
		return self.x_data

	def get_y_data():
		return self.y_data

	def get_fit_data(self):
		return self.fit_data
		
	def set_epidemic_model(self, epidemic_model):
		self.epidemic_model = epidemic_model

	def set_fit_data(self, y_fit_data):
		self.y_fit_data = y_fit_data