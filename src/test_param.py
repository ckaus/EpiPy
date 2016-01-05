# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
from utils import csvmanager, logger
from algorithm import Leastsquare
from model import sir, seir, si
from simulator import SSESimulator

"""This file contains test functionalites."""

def leastsquare_example(model, file_name, n=60):
	"""
	Example for using leastsquare method
	"""
	data = np.loadtxt(file_name, delimiter=';', skiprows=1)
	ls_data = {"Time": data[:,0], "S": data[:,1], "I": data[:,2], "R": data[:,3]}
	
	# least square use record instead of infected, recovered, ...
	#ls_data["Record"] = ls_data.pop("I")
	lsq = Leastsquare(model, ls_data, n)
	result = lsq.run()

	# Plot data and fit
	pl.clf()
	pl.plot(lsq.time_total, lsq.data_record, "o")
	pl.plot(lsq.time_total, result)
	pl.show()

def sse_simulator():
	ssesim = SSESimulator()
	ssesim.simulation()

if __name__ == '__main__':
	# sse_simulator()
	#for i in range(1000):
	leastsquare_example(sir, "../resources/data/data4.csv", 100)
	