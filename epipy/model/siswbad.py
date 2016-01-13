# -*- coding: utf-8 -*-

"""This file contains the SIR-Model."""

from basemodel import BaseModel
from scipy import integrate

class SISwbad(BaseModel):
	def __init__(self, xdata, ydata):
		BaseModel.__init__(self, xdata, ydata)
		self.N0 = self.init_param()

	def init_param(self):
		I0 = self.ydata[0]
		S0 = self.N - I0
		return S0, I0

	def model(self, y, x, beta, gamma, mu):
		S = -beta * y[0] * y[1] / self.N + mu * (self.N - y[0])
		I = beta * y[0] * y[1] / self.N - gamma * y[1] - mu * y[1]
		return S, I

	def fit_odeint(self, x, beta, gamma, mu):
		return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:,1]