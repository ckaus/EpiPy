# -*- coding: utf-8 -*-

import scipy.integrate as spi
import numpy as np
import pylab as pl

def simple(sis_values, time):
    """
    sis_values [S,I], where
    S = initial number of suspectable
    I = initial number of infected

    time = observe time
    https://me.ucsb.edu/~moehlis/APC514/tutorials/tutorial_seasonal/node2.html
    gamma = alpha
    """
    s = sis_values[0] 
    i = sis_values[1]

    beta = 1.4247 # transmission rate between S and I + probability of transmission
    gamma = 0.14286 # recovery rate
    sis=np.zeros((2))    
    sis[0] = - beta * s * i + gamma * i
    sis[1] = beta * s * i - gamma * i
    return sis

def build(sis_values, model, time):
    # initial values
    S0 = sis_values[0]
    I0 = sis_values[1]
    return spi.odeint(model, (S0, I0), time)

if __name__ == '__main__':
	I0 = 1e-6
	S0 = 1.0 - I0
	time = np.arange(0.0,71.0,1.0)
	result = build((S0,I0), simple,time)
	pl.subplot(211)
	pl.plot(result[:,0], '-g', label='Susceptibles')
	pl.xlabel('Time')
	pl.ylabel('Susceptibles')
	pl.subplot(212)
	pl.plot(result[:,1], '-r', label='Infectious')
	pl.xlabel('Time')
	pl.ylabel('Infectious')
	pl.show()