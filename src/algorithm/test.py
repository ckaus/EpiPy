# -*- coding: utf-8 -*-

"""
This file contains fitting methods.
"""
import pylab as pl
from pymc import *
# load the model
import si_model as mod
reload(mod)  # this reload streamlines interactive debugging

def plot_si_model_fit():
	# fit the model with mcmc    
	mc = MCMC(mod)
	mc.use_step_method(AdaptiveMetropolis, [mod.beta, mod.gamma, mod.SI_0])
	mc.sample(iter=100000, burn=50000, thin=20, verbose=1)
	pl.title('SI model with uncertainty')
	pl.plot(mod.infected_data, 's', mec='black', color='black', alpha=.9)
	pl.plot(mod.I.stats()['mean'], color='blue', linewidth=2)
	pl.plot(mod.I.stats()['95% HPD interval'], color='blue', linewidth=1, linestyle='dotted')
	pl.xticks(range(1,10,2))
	pl.xlabel('Time (days)')
	pl.yticks([0,15,30])
	pl.ylabel('I (people)')
	pl.axis([-1,10,-1,35])
	pl.show()

if __name__ == '__main__':
	plot_si_model_fit()
    