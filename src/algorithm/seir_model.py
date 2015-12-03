# -*- coding: utf-8 -*-

import scipy.integrate as spi
import numpy as np
import pylab as pl

def simple(seir_values,time):
	"""
    seir_values [S,E,I], where
    S = initial number of suspectable
    E = initial proportion of the population that are exposed
    (infected but not infectious)
    I = initial number of infected
    
    time = observe time
    https://me.ucsb.edu/~moehlis/APC514/tutorials/tutorial_seasonal/node4.html
    sigma=alpha
    """
	s = seir_values[0]
	e = seir_values[1]
	i = seir_values[2]
	mu=1/(70*365.0) #  death rate, birth rate
	beta=520/365.0 # transmission rate between S and I + probability of transmission
	# sigma = rate at which individuals move from the exposed to the infectious classes. 
	# Its reciprocal (1/sigma) is the average latent (exposed) period.
	sigma=1/14.0
	gamma=1/7.0 # recovery rate

	seir=np.zeros((3))    
	seir[0] = mu - beta * s * i - mu * s
	seir[1] = beta * s * i - ( mu + sigma ) *  e
	seir[2] = sigma * e - ( mu + gamma ) * i
	return seir

def build(seir_values, model, time):
    # initial values
    S0 = seir_values[0]
    E0 = seir_values[1]
    I0 = seir_values[2]
    return spi.odeint(model, (S0, E0, I0), time)

if __name__ == '__main__':
	S0=0.1
	E0=1e-4
	I0=1e-4
	time = np.arange(0.0, 60*365.0, 1.0)

	result = build((S0,E0,I0), simple, time)
	rec=1. - (result[:,0]+result[:,1]+result[:,2])
	pl.subplot(311)
	pl.plot(result[:,0], '-g', label='Susceptibles')
	pl.xlabel('Time')
	pl.ylabel('Susceptibles')
	pl.subplot(312)
	pl.plot(result[:,1], '-m', label='Exposed')
	pl.plot(result[:,2], '-r', label='Infectious')
	pl.legend(loc=0)
	pl.xlabel('Time')
	pl.ylabel('Infected')
	pl.subplot(313)
	pl.plot(rec, '-k', label='Recovereds')
	pl.xlabel('Time')
	pl.ylabel
	pl.show()