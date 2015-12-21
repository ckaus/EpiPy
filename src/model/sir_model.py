# -*- coding: utf-8 -*-

"""This file contains the SIR-Model."""

import numpy as np
import scipy.integrate as spi
import pylab as pl

def simple(sir_values, time, beta, gamma, k):
    """
    This function represents the SIR Model.

    :param sir_values: the input sir values, where 
        S = initial number of suspectable,
        I = initial number of infected,
        R = initial number of recovered
    :type sir_values: list
    :param time: the observe time
    :type time: int
    :param beta: the transmission rate between S and I = probability of transmission
    :type beta: float
    :param gamma: the recovery rate between I and R = probability of transmission
    :type gamma: float
    :param k: minimization of scalar function by using the initial parameter (SIR) and  Nelder-Mead algorithm
    :type k: float
    :returns: sir values based on time
    """

    s = sir_values[0]
    i = sir_values[1]
    r = sir_values[2]

    res = np.zeros((3))
    res[0] = - beta * s * i
    res[1] = beta * s * i - gamma * i
    res[2] = gamma * i
    return res

def pop(I, k):
    """
    This function returns the initial parameter for SIR Model.

    :param I: initial number of infected
    :type I: int
    :param k: normalize train data
    :type k: float
    """
    I0 = I*k
    S0 = 1 - I0
    N = [S0, I0, 0]
    return N

def param_init():
    """
    This function returns the initial parameter (beta/gamma) for SIR Model.
    """
    return [0.9, 0.1] 

def with_births_deaths(sir_values, time):
    """
    This function represents the SIR Model with birth and death.

    :param sir_values: the input sir values, where 
        S = initial number of suspectable,
        I = initial number of infected,
        R = initial number of recovered
    :type sir_values: list
    :param time: the observe time
    :type time: int
    """
    s = sir_values[0]
    i = sir_values[1]
    r = sir_values[2]

    mu=1/(70*365.0) # death rate, birth rate
    beta=520/365.0 # the transmission rate between S and I
    gamma=1/7.0 # recovery rate
    
    res = np.zeros((3))
    res[0] = mu - beta * s * i - mu * s
    res[1] = beta * s * i - gamma * i - mu * i
    res[2] = gamma * i - mu * r
    return res

def disease_induced_mortality(sir_values, time):
    """
    This function represents the SIR Model with disease_induced_mortality.

    :param sir_values: the input sir values, where 
        S = initial number of suspectable,
        I = initial number of infected,
        R = initial number of recovered
    :type sir_values: list
    :param time: the observe time
    :type time: int
    """
    s = sir_values[0]
    i = sir_values[1]
    r = sir_values[2]

    rho=0.5 # mortality probability before recovering.
    mu=1/(70*365.0) # death rate from natural causes
    beta=520/365.0 # transmission rate between S and I
    gamma=1/7.0 # recovery rate
    
    res=np.zeros((3))
    res[0] = mu - beta * s * i - mu * s
    res[1] = beta * s * i - (gamma + mu) * i/(1-rho)
    res[2] = gamma * i - mu * r
    return res

# def build(sir_values, model, time):
#     # initial values
#     S0 = sir_values[0]
#     I0 = sir_values[1]
#     R0 = sir_values[2]
#     return spi.odeint(model, (S0, I0, R0), time)

# if __name__ == '__main__':
#     # =====================
#     # simple sir with t = 71 days
#     # =====================
#     S0=1-1e-6 # 0.999999
#     I0=1e-6 # -3.28171817154
#     R0=0
#     time = np.arange(0.0,71,1)
#     sir_model = build((S0,I0,R0), simple, time)
#     pl.plot(time,sir_model[:,1])
#     pl.xlabel('Time')
#     pl.show()

#     # =====================
#     # with_births_deaths with t = 60 years
#     # =====================
#     S0=0.1
#     I0=1e-4
#     R0=1-S0-I0
#     time = np.arange(0.0,60*365,1) 
#     sir_model = build((S0,I0,R0), with_births_deaths, time)
#     # note: y axis is for 60 years!
#     pl.plot(time,sir_model[:,1])
#     pl.xlabel('Time')
#     pl.show()
    
    # =====================
    # disease_induced_mortality
    # =====================
    # S0=0.2
    # I0=1e-4
    # R0=1-S0-I0
    # INP = (S0,I0,R0)
    # time = np.arange(0.0, 1e5, 1.0)
    # sir_model = build((S0,I0,R0), disease_induced_mortality, time)

    # pl.plot(sir_model[:,2], '-k', label='Recovereds')
    # pl.plot(sum((sir_model[:,0],sir_model[:,1],sir_model[:,2])), '--k', label='Total Population')
    # pl.xlabel('Time')
    # pl.legend(loc=0)
    # pl.ylabel('Recovereds\nTotal Population')
    # pl.show()