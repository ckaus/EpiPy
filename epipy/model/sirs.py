# -*- coding: utf-8 -*-

from basemodel import BaseModel
from scipy import integrate

class SIRS(BaseModel):
	def __init__(self, xdata, ydata):
		BaseModel.__init__(self, xdata, ydata)
		self.N0 = self.init_param()

	def init_param(self):
		I0 = self.ydata[0]
		S0 = self.N - I0
		R0 = 0.0
		return S0, I0, R0

	def model(self, y, x, beta, gamma, f):
		"""
		f = Average loss of immunity rate of recovered individuals
		"""
		S = -beta * y[0] * y[1] / self.N
		I = beta * y[0] * y[1] / self.N - gamma * y[1]
		R = gamma * y[1]
		return S, I, R

	def fit_odeint(self, x, beta, gamma):
		return integrate.odeint(self.model, self.N0, x, args=(beta, gamma))[:,1]