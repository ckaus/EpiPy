# -*- coding: utf-8 -*-

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
		self.ode = model.ode
		self.time_total = self.data['Time']
		self.time_train = self.data['Time'][:n]
		self.data_infected = self.data['Infected']
		# train data
		self.data_infected_train = self.data_infected[:n]
		# normalize train data
		self.k = 1.0/sum(self.data_infected_train)
		# normalized classes for t = 0
		self.N0 = self.model.pop(self.data_infected_train[0], self.k)
		
	def run(self):
		# Set initial parameter values
		param_init = self.model.param_init()
		param_init.append(self.k)
		# fitting
		param = minimize(self.sse(self.model), param_init, method='nelder-mead').x
		# get the fitted model
		Nt = integrate.odeint(self.ode, self.N0, self.time_total, args=tuple(param))
		# scale out
		Nt = np.divide(Nt, self.k)
		# Get the second column of data corresponding to I
		return [row[1] for row in Nt]
	
	def sse(self, model):
		''' (S) of (S)quare (E)rror'''
		def result(x):
			Nt = integrate.odeint(self.ode, self.N0, self.time_train, args=tuple(x))
			INt = [row[1] for row in Nt]
			INt = np.divide(INt, self.k)
			difference = self.data_infected_train - INt
			# square the difference
			return np.dot(difference, difference)
		return result

# example
import sir_model
data = {'Time': [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],
		'Infected': [ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]}    

lsq = Leastsquare(sir_model, data, 15)
result = lsq.run()

# Plot data and fit
py.clf()
py.plot(lsq.time_total, lsq.data_infected, 'o')
py.plot(lsq.time_total, result)
py.show()
