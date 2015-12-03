# -*- coding: utf-8 -*-

from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np

class Leastsquare(object):
	def __init__(self, model, data, n):
		"""
		This class fit a given model by using least square method.
		
		:param model: a epidemic model
		:param data: the data set for fitting
		:type data: the *Dictionary* contains, Time and an epidemic data set
		:param n: ??? count of train data set ???
		:type n: int 
		:returns: a *Leastsquare* instance
		:raises: *ValueError* if Time or epidemic data set values not matching
		"""

		if "Time" not in data:
			raise ValueError("'Time' data not found")
		if "Infected" not in data:
			raise ValueError("'Infected' data not found")
		if len(data["Time"]) != len(data["Infected"]):
			raise ValueError("'Time' data not matching 'Infected' data")
		
		self.model = model
		self.data = data
		self.ode = model.simple
		self.time_total = self.data["Time"]
		self.time_train = self.data["Time"][:n]
		self.data_infected = self.data["Infected"]
		# train data
		self.data_infected_train = self.data_infected[:n]
		# normalize train data
		self.k = 1.0/sum(self.data_infected_train)
		# normalized classes for t = 0
		self.N0 = self.model.pop(self.data_infected_train[0], self.k)
		
	def run(self):
		"""
		This function fits a epidemic data set with a model.
		"""
		# Set initial parameter values
		param_init = self.model.param_init()
		param_init.append(self.k)
		# fitting
		param = minimize(self.sse(self.model), param_init, method="nelder-mead").x
		# get the fitted model
		Nt = integrate.odeint(self.ode, self.N0, self.time_total, args=tuple(param))
		# scale out
		Nt = np.divide(Nt, self.k)
		# Get the second column of data corresponding to I
		return [row[1] for row in Nt]
	
	def sse(self, model):
		"""
		This function calculate the squared errors of prediction.

		:param model: a epidemic model
		:returns: a measure of the discrepancy between the data and an estimation model
		"""
		def result(x):
			Nt = integrate.odeint(self.ode, self.N0, self.time_train, args=tuple(x))
			INt = [row[1] for row in Nt]
			INt = np.divide(INt, self.k)
			difference = self.data_infected_train - INt
			# square the difference
			return np.dot(difference, difference)
		return result