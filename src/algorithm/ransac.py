import numpy as np
from leastsquare import Leastsquare
from model import sir
import random 
from scipy.optimize import minimize
from scipy import integrate
import leastsquare
import collections
import pylab as pl
class Ransac(object):
	
	def __init__(self, model, data, n, iterations, treshold):
		self.model = model
		self.treshold = treshold
		self.cs_list = []
		
		# convert str to float
		data["Time"] = [float(v) for v in data["Time"]]
		data["Record"] = [float(v) for v in data["Record"]]

		for i in range(0, iterations):
			print "Iteration: %s" % i
			# get random data for leastsqaure
			rnd_lsq_data = self.get_random_data(data)
			# sort random  data
			sorted_keys = sorted(rnd_lsq_data.keys())
			lsq_data = {"Time": [], "Record": [], "LSQ": []}
			for key in sorted_keys:
				lsq_data["Time"].append(key)
				lsq_data["Record"].append(rnd_lsq_data.get(key))
			# fit random data to model by using leastsquare
			lsq = Leastsquare(self.model, lsq_data)
			possible_cs = lsq.run() # possible consensus set
			error_mean = np.mean(lsq.errors) # average of sse
			# add consensus set with less sse
			if error_mean < 1.0:
				self.cs_list.append([lsq_data["Time"], possible_cs])

		for cs in self.cs_list:
			# check if consensus set contains more than 20 points
			if len(cs[1]) > 20:
				# plot
				print "CS count:%s" % len(cs[1])
				print "CS Time: %s" % cs[0]
				pl.clf()
				pl.plot(data["Time"], data["Record"], "o")
				pl.plot(cs[0], cs[1])
				pl.show()
			
	def get_random_data(self, data):
		result = {}
		data_time = data["Time"]
		data_record = data["Record"]
		# merge time and data for better access
		_data = dict(zip(data_time,data_record))
		# mix (shuffle) data
		random.shuffle(_data.keys())
		# select random value for init model
		rnd_init_time = random.choice(_data.keys())
		rnd_init_data = _data[rnd_init_time]
		# delete rnd time and data from data set
		del _data[rnd_init_time]
		result[rnd_init_time] = rnd_init_data
		# select random values for fitting model
		rnd = random.randint(10,len(data_record)-1)
		for i in range(0, rnd):
			rnd_time = random.choice(_data.keys())
			rnd_data = _data[rnd_time]
			del _data[rnd_time]
			result[rnd_time] = rnd_data
		return result