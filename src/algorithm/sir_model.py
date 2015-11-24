# -*- coding: utf-8 -*-

import numpy as np
import scipy.integrate as spi
import math

# only infected values
dataset = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5,
            6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 
            13, 14, 13, 10, 10, 10, 11, 10, 10, 10, 11, 
            10, 10, 10, 8, 8, 7, 8, 10, 9, 11, 11, 12, 12, 
            14, 14, 12, 13, 17, 19, 17, 16, 17, 18, 20, 19, 16, 
            16, 15, 14, 15, 15, 16, 17, 17, 17, 18, 17, 17, 18, 
            19, 21, 21, 23, 26, 26, 25, 26, 31, 31, 30, 36, 39, 
            48, 48, 51, 57, 56, 61, 67, 68, 66, 67, 67, 66, 64, 60, 
            57, 55, 56, 57, 53, 52, 50, 49, 49, 48, 45, 44, 43, 44, 
            43, 40, 37, 39, 40, 41, 41, 38, 34, 35, 33, 32, 32, 29, 28, 
            11, 12, 12, 12, 12, 12, 12, 13, 13, 12, 12, 10, 10, 11, 9, 10, 
            9, 8, 6, 6, 6, 6, 4, 3, 3, 4, 4, 4, 1, 1, 0]

beta=1.4247
gamma=0.14286

def sir(parameters, time):
    """"
    
    This function generates the sir model.
    
    :param parameters: a array where [0] = S, [1] = I, [2] = default 
    :param time: a sequence of time points for which to solve for parameters.
    :returns: array of points for S, I, R
    """
    sir_v = np.zeros((3))
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

if __name__ == '__main__':
    sir_model = compute(sir,np.arange(0.0,len(dataset),1))
    print sir_model