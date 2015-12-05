# -*- coding: utf-8 -*-

import scipy.integrate as spi
import numpy as np
import pylab as pl

def simple(sir_values, time, beta, gamma, sigma, mu, k):
	"""
    seir_values [S,E,I], where
    S = initial number of suspectable
    E = initial proportion of the population that are exposed
    (infected but not infectious)
    I = initial number of infected
    
    time = observe time
    https://me.ucsb.edu/~moehlis/APC514/tutorials/tutorial_seasonal/node4.html
    http://www.stat.colostate.edu/~rdavis/ey680/sir.pdf
    http://www.public.asu.edu/~hnesse/classes/seir.html?Beta=0.9&Gamma=0.2&Sigma=0.5&Mu=0&Nu=0&initialS=10&initialE=1&initialI=0&initialR=0&iters=15
    
    sigma=alpha
    mu = is the immunity loss rate transmission rate between 
    	S and I + probability of transmission
	gamma = recovery rate
	sigma = rate at which individuals move from the exposed to the infectious classes. 
		Its reciprocal (1/sigma) is the average latent (exposed) period.
	mu = death rate, birth rate
    """
	s = seir_values[0]
	e = seir_values[1]
	i = seir_values[2]
	r = seir_values[3]

	seir=np.zeros((3))    
	seir[0] = mu - beta * s * i - mu * s
	seir[1] = beta * s * i - ( mu + sigma ) *  e
	seir[2] = sigma * e - ( mu + gamma ) * i
	seir[3] = gamma * i - mu * r 
	return seir

def pop(E, k):
    E0 = I*k
    S0 = 1 - E0
    N = [S0, E0, 0, 0]
    return N

def param_init():
	# 		beta	   gamma sigma	  mu
	return [520/365.0, 1/7.0, 1/14.0, 1/(70*365.0)]

# def build(seir_values, model, time):
#     # initial values
#     S0 = seir_values[0]
#     E0 = seir_values[1]
#     I0 = seir_values[2]
#     return spi.odeint(model, (S0, E0, I0), time)

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