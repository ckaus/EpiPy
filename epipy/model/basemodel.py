# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize
from epipy.utils import logger
from numpy import ndarray

class BaseModel():
	"""
	This class defines an abstract epidemic model.
	"""
	def __init__(self, xdata, ydata):
		__metaclass__ = ABCMeta
		self.N = 1 # normalized population
		self.xdata = xdata # time
		self.ydata = ydata # samples

	@abstractmethod
	def init_param(self, ydata, N): pass

	@abstractmethod
	def model(self, y, x, *params): pass

	@abstractmethod
	def fit_odeint(x, *param): pass

	def fit(self, model_class=0, debug=0):
		self.model_class = model_class
		if type(self.ydata[0]) is not ndarray:
			# calculate init param for modelling
			self.N0 = self.init_param()
			# use for fitting given samples
			self._ydata = self.ydata
		else:
			# use init param of given samples for modelling
			self.N0 = self.ydata[:,0]
			# use for fitting only specific sample based on model class
			self._ydata = self.ydata[self.model_class,:]
		popt, pcov = optimize.curve_fit(self.fit_odeint, self.xdata, self._ydata)
		result = self.fit_odeint(self.xdata, *popt)
		if debug:
			logger.info("Fitting SIR Model by using func=curve_fit.")
			logger.info("popt: %s" % popt)
			logger.info("Description: Optimal values for the parameters so that the sum of the squared error of f(xdata, *popt) - ydata is minimized")
			logger.info("pcov: %s" % pcov)
			logger.info("Description: The estimated covariance of popt. The diagonals provide the variance of the parameter estimate.")
			logger.info("result: %s" % result)
		return result