# -*- coding: utf-8 -*-

from basemodel import BaseModel
from scipy import integrate

class SIR(BaseModel):
	def __init__(self):
		BaseModel.__init__(self)
		
	def init_param(self, y0):
		I0 = y0
		S0 = self.N - I0
		R0 = self.N - S0 - I0
		return S0, I0, R0

	def model(self, y, x, beta, gamma):
		S = -beta * y[0] * y[1] / self.N
		I = beta * y[0] * y[1] / self.N - gamma * y[1]
		R = gamma * y[1]
		return S, I, R

	def fit_odeint(self, x, beta, gamma):
		return integrate.odeint(self.model, self.N0, x, args=(beta, gamma))[:,1]

class SIRwbad(SIR):
	def __init__(self):
		SIR.__init__(self)
		
	def model(self, y, x, beta, gamma, mu):
		S, I, R = SIR.model(self, y,x,beta,gamma)
		S = S + mu * (self.N - y[0])
		I = I - mu * y[1]
		R = R - mu * y[2] 
		return S, I, R

	def fit_odeint(self, x, beta, gamma, mu):
		return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:,1]