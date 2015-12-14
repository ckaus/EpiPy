# -*- coding: utf-8 -*-

import pylab as pl
from utils import csvmanager, logger
from algorithm import Leastsquare
from model import sir, seir, si
from simulator import SSESimulator

"""This file contains test functionalites."""

def leastquare_example(model, file_name, n=60):
	"""
	Example for using leastsquare method
	"""
	cfo = csvmanager.CSV_File_Object(file_name=file_name, seperator=";", model=model)
	cm = csvmanager.CSV_Manager(cfo).read(origin_fields=["Time","I"], result_fields=["Time", "Infected"])
	ls_data = cm.content
	# least square use record instead of infected, recovered, ...
	ls_data["Record"] = ls_data.pop("Infected")
	lsq = Leastsquare(model, ls_data, n)
	result = lsq.run()

	# Plot data and fit
	pl.clf()
	pl.plot(lsq.time_total, lsq.data_record, "o")
	pl.plot(lsq.time_total, result)
	pl.show()


def sse_simulator():
	ssesim = SSESimulator()
	result = ssesim.simulation()
	print result
	
if __name__ == '__main__':
	sse_simulator()
	# leastquare_example(sir,"data1.csv", 60) # bug, file name need backslash, otherwise it doesnt work.


# from pymc import MCMC, AdaptiveMetropolis
# def mcmc_example():
# 	"""Example of using MCMC method"""
	
# 	reload(model)  # this reload streamlines interactive debugging

# 	# fit the model with mcmc    
# 	mc = MCMC(model)
# 	mc.use_step_method(AdaptiveMetropolis, [model.beta, model.gamma, model.SI_0])
# 	mc.sample(iter=100000, burn=50000, thin=20, verbose=1)
# 	pl.title('SI model with uncertainty')
# 	pl.plot(model.infected_data, 's', mec='black', color='black', alpha=.9)
# 	pl.plot(model.I.stats()['mean'], color='blue', linewidth=2)
# 	pl.plot(model.I.stats()['95% HPD interval'], color='blue', linewidth=1, linestyle='dotted')
# 	pl.xticks(range(1,10,2))
# 	pl.xlabel('Time (days)')
# 	pl.yticks([0,15,30])
# 	pl.ylabel('I (people)')
# 	pl.axis([-1,10,-1,35])
# 	pl.show()
