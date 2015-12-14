# -*- coding: utf-8 -*-

"""This file contains the least sqaure method for fitting a model."""

from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np

class Leastsquare(object):
	"""
		This class fit a given model by using least square method.
		
		:param model: a epidemic model
		:type model: model file
		:param data: the data set for fitting, contains Time and an epidemic data set
		:type data: *Dictionary*
		:param n: ??? count of train data set ???
		:type n: int 
		:returns: a *Leastsquare* instance
		:raises: *ValueError* if Time or epidemic data set values not matching
		
		Example:
		::

			import pylab as pl
			from utils import csvmanager
			from algorithm import Leastsquare
			from model import sir
		
			cfo = csvmanager.CSV_File_Object(
					file_name="/data1.csv",
					seperator=";",
					model=sir)

			cm = csvmanager.CSV_Manager(cfo).read(
					origin_fields=["Time","I"],
					result_fields=["Time", "Infected"])

			ls_data = cm.content
			# least square use record instead of infected, recovered, ...
			ls_data["Record"] = ls_data.pop("Infected")
			lsq = Leastsquare(sir, ls_data, 60)
			result = lsq.run()

			# Plot data and fit
			pl.clf()
			pl.plot(lsq.time_total, lsq.data_record, "o")
			pl.plot(lsq.time_total, result)
			pl.show()
		"""
	def __init__(self, model, data, n):
		if "Time" not in data:
			raise ValueError("'Time' not found")
		if "Record" not in data:
			raise ValueError("'Data not found")
		if len(data["Time"]) != len(data["Record"]):
			raise ValueError("'Time' not matching 'Record'")
		
		self.model = model
		self.data = data
		self.ode = model.simple
		self.time_total = self.data["Time"]
		self.time_train = self.data["Time"][:n]
		# original record data
		self.data_record = self.data["Record"]
		# train data
		self.data_record_train = []
		if isinstance(self.data_record[0],str):
			# cast to float, because csv data are normaly strings
			for i in range(0, len(self.data_record)):
				self.data_record[i] = float(self.data_record[i])
		self.data_record_train = self.data_record[:n]
		# normalize train data
		self.k = 1.0/sum(self.data_record_train)
		# normalized classes for t = 0
		self.N0 = self.model.pop(self.data_record_train[0], self.k)
		self.errors = []
		
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
		self.fit = Nt[:,1]
	
	def sse(self, model):
		"""
		This function calculate the squared errors of prediction.

		:param model: a epidemic model
		:type model: model file
		:returns: a measure of the discrepancy between the data and an estimation model
		"""
		
		def result(x):
			Nt = integrate.odeint(self.ode, self.N0, self.time_train, args=tuple(x))
			INt = [row[1] for row in Nt]
			INt = np.divide(INt, self.k)
			difference = self.data_record_train - INt
			# square the difference
			diff = np.dot(difference, difference)
			self.errors.append(diff)
			return diff
		return result