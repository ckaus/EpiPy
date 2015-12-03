# -*- coding: utf-8 -*-

import sir_model
from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np

class Leastsquare:
	def __init__(self, model, data, n):
		if 'Time' not in data:
			print 'ERROR: data field Time not found.'
			return 0
		elif 'Infected' not in data:
			print 'ERROR: data field Infected not found.'
			return 0
		elif len(data['Time']) != len(data['Infected']):
			print 'ERROR: data field Time not matching data field Infected'
			return 0
		self.model = model
		self.data = data
		self.n = n
		self.ode = model.ode

	def run(self):
		self.timetotal = self.data['Time']
		self.timetrain = self.data['Time'][:self.n]
		self.originaldataI = self.data['Infected']
		# # till t = n
		self.dataI = self.originaldataI[:self.n]
		self.k = 1.0/sum(self.dataI)
		self.N0 = self.model.pop(self.dataI[0], self.k)
		# Set initial parameter values
		paramInit = self.model.param_init()
		paramInit.append(self.k)
		# fitting
		param = minimize(self.SSE(self.model), paramInit, method='nelder-mead').x
		# Get the fitted model
		Nt = integrate.odeint(sir_model.ode, self.N0, self.timetotal, args=tuple(param))
		# # scale out
		Nt = np.divide(Nt, self.k)
		# Get the second column of data corresponding to I
		return [row[1] for row in Nt]
	
	def SSE(self, model):
		def result(x):
			Nt = integrate.odeint(sir_model.ode, self.N0, self.timetrain, args=tuple(x))
			INt = [row[1] for row in Nt]
			INt = np.divide(INt, self.k)
			difference = self.dataI - INt
			# square the difference
			return np.dot(difference, difference)
		return result

data = {'Time': [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],
		'Infected': [ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]}    

lsq = Leastsquare(sir_model, data, 15)
result = lsq.run()

# Plot data and fit
py.clf()
py.plot(lsq.timetotal, lsq.originaldataI, 'o')
py.plot(lsq.timetotal, result)
py.show()
