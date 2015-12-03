# -*- coding: utf-8 -*-

"""This file contains fitting methods."""

import pylab as pl

def leastquare_example():
	"""Example for using leastsquare method"""
	
	from leastsquare import Leastsquare
	import sir_model as model

	ls_data = {"Time": [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],
	"Infected": [ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]}    

	lsq = Leastsquare(model, ls_data, 15)
	result = lsq.run()

	# Plot data and fit
	pl.clf()
	pl.plot(lsq.time_total, lsq.data_infected, "o")
	pl.plot(lsq.time_total, result)
	pl.show()

def mcmc_example():
	"""Example of using MCMC method"""
	
	from pymc import MCMC, AdaptiveMetropolis
	# load the model
	import si_model as model
	reload(model)  # this reload streamlines interactive debugging

	# fit the model with mcmc    
	mc = MCMC(model)
	mc.use_step_method(AdaptiveMetropolis, [model.beta, model.gamma, model.SI_0])
	mc.sample(iter=100000, burn=50000, thin=20, verbose=1)
	pl.title('SI model with uncertainty')
	pl.plot(model.infected_data, 's', mec='black', color='black', alpha=.9)
	pl.plot(model.I.stats()['mean'], color='blue', linewidth=2)
	pl.plot(model.I.stats()['95% HPD interval'], color='blue', linewidth=1, linestyle='dotted')
	pl.xticks(range(1,10,2))
	pl.xlabel('Time (days)')
	pl.yticks([0,15,30])
	pl.ylabel('I (people)')
	pl.axis([-1,10,-1,35])
	pl.show()

if __name__ == '__main__':
	leastquare_example()
	# mcmc_example()
