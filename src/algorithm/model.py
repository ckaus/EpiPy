# -*- coding: utf-8 -*-

import numpy as np
import scipy.integrate as spi
import pylab as pl

beta=1.4247
gamma=0.14286

def sir(parameters, time):
    """"
    
    This function generates the sir model.
    
    :param parameters: a array where [0] = S, [1] = I, [2] = default 
    :param time: a sequence of time points for which to solve for parameters.
    :returns: array of points for S, I, R
    """
    sir_v=np.zeros((3))
    sir_v[0] = - beta * parameters[0] * parameters[1]
    sir_v[1] = beta * parameters[0] * parameters[1] - gamma * parameters[1]
    sir_v[2] = gamma * parameters[1]
    return sir_v

def compute(model, time=np.arange(0.0, 71.0, 1)):
    """
    :param model: the basic model
    :param time: time range of basic model
    :returns: (x,y) for S, I, R
    """
    # initial values
    S0=1-1e-6 # 0.999999
    I0=1e-6 # -3.28171817154
    return spi.odeint(model, (S0, I0, 0.0), time)


# RES = compute(sir)

# #Ploting
# pl.plot(RES[:,0], '-bs', label='Susceptibles')  # I change -g to g--  # RES[:,0], '-g',
# pl.plot(RES[:,2], '-g^', label='Recovereds')  # RES[:,2], '-k',
# pl.plot(RES[:,1], '-ro', label='Infectious')
# pl.legend(loc=0)
# pl.title('SIR epidemic without births or deaths')
# pl.xlabel('Time')
# pl.ylabel('Susceptibles, Recovereds, and Infectious')
# pl.show()