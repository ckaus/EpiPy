# -*- coding: utf-8 -*-

"""This file contains the least sqaure method for fitting a model."""

from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np

class Leastsquare(object):
	def __init__(self, model, data):
		self.model = model
		self.data = data
		self.ode = model.simple
		self.time_total = self.data["Time"]
		# original record data
		self.data_record = self.data["Record"]
		# train data
		self.data_record_train = []
		if isinstance(self.data_record[0],str):
			# cast to float, because csv data are normaly strings
			for i in range(0, len(self.data_record)):
				self.data_record[i] = float(self.data_record[i])
		self.data_record_train = self.data_record
		# normalize train data
		self.k = 1.0/sum(self.data_record_train)
		# normalized classes for t = 0
		self.N0 = self.model.pop(self.data_record_train[0], self.k)
		self.errors = []
		
	def run(self):
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
		self.fit = Nt[:,1]
		return self.fit
	
	def sse(self, model):
		def result(x):
			Nt = integrate.odeint(self.ode, self.N0, self.time_total, args=tuple(x))
			INt = [row[1] for row in Nt]
			INt = np.divide(INt, self.k)
			difference = self.data_record_train - INt
			# square the difference
			diff = np.dot(difference, difference)
			self.errors.append(diff)
			return diff
		return result