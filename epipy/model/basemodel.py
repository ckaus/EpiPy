# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize

class BaseModel():
	"""
	This class defines an abstract epidemic model.
	"""
	def __init__(self, xdata, ydata):
		__metaclass__ = ABCMeta
		self.N = 1 # normalized population
		self.xdata = xdata # time
		self.ydata = ydata # samples
		self.N0 = self.init_param() # S,I,R on t=0

	@abstractmethod
	def init_param(self, ydata, N): pass

	@abstractmethod
	def model(self, y, x, *param): pass

	@abstractmethod
	def fit_odeint(x, *param): pass

	def fit(self, *param):
		if len(param) is 0:
			popt, pcov = optimize.curve_fit(self.fit_odeint, self.xdata, self.ydata)
			return self.fit_odeint(self.xdata, *popt)
		else:
			return self.fit_odeint(self.xdata, *param)
		