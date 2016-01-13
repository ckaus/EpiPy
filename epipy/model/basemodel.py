# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize

class BaseModel():
	"""
	This class defines an abstract epidemic model class.
	An epidemic model is a simplified means of describing
	the transmission of communicable disease through individuals.
	"""
	def __init__(self, xdata, ydata):
		__metaclass__ = ABCMeta
		self.N = 1 # normalized population
		self.xdata = xdata # time
		self.ydata = ydata # samples

	@abstractmethod
	def init_param(self, ydata, N): pass

	@abstractmethod
	def model(self, y, x, *args): pass

	@abstractmethod
	def fit_odeint(x, *args): pass

	def fit(self, **kwargs):
		if len(kwargs) is 0:
			popt, pcov = optimize.curve_fit(self.fit_odeint, self.xdata, self.ydata)
			return self.fit_odeint(self.xdata, *popt)
		else:
			return self.fit_odeint(self.xdata, **kwargs)
		