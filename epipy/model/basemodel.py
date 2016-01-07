# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize
from epipy.utils import logger

class BaseModel():
	"""
	This class defines an abstract epidemic model.
	"""
	def __init__(self):
		__metaclass__ = ABCMeta

	@abstractmethod
	def init_param(self, ydata, N): pass

	@abstractmethod
	def model(self, y, x, *params): pass

	@abstractmethod
	def fit_odeint(x, *param): pass

	def fit(self, debug=0):
		popt, pcov = optimize.curve_fit(self.fit_odeint, self.xdata, self.ydata)
		result = self.fit_odeint(self.xdata, *popt)
		if debug:
			logger.info("Fitting SIR Model by using func=curve_fit.")
			logger.info("popt: %s" % popt)
			logger.info("Description: Optimal values for the parameters so that the sum of the squared error of f(xdata, *popt) - ydata is minimized")
			logger.info("pcov: %s" % pcov)
			logger.info("Description: The estimated covariance of popt. The diagonals provide the variance of the parameter estimate.")
			logger.info("result: %s" % result)
		return result