#!/usr/bin/env python

"""
Pseudo code:
-----------
parameters <- (beta0,gamma0)
time <- total time in dataset

for next n points p_1, .. , p_n in dataset do
    sumOfSq <- SSE(parameters, data until p_n)
    if sumOfSq > sumTarget do
        parameter <- optimize(SIR)

return parameters
"""

import numpy as np
import pandas as pd
# from pylab import *
import scipy.integrate as spi
import scipy.optimize as spo
# import csv
import pylab


# Load data using csv
"""
with open('../resources/data1.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=';', quotechar='\"')
    for row in datareader:
       print ', '.join(row)
"""

# Load data using pandas
dataframe = pd.read_csv('../resources/data1.csv', sep=';', index_col='Time')
print dataframe.head()
print dataframe.tail()

# Parameter Values

S0 = 0.999999
I0 = 0.000001
R0 = 0.0
population = (S0, I0, R0)

beta = 0.5
gamma = 0.1
t_end = len(dataframe.index) + 1
t_start = 1
t_step = 1  # how to decide how much step????
t_interval = np.arange(t_start, t_end, t_step)
sumTarget = 0.5

# Solving the differential equation. Solves over t for initial conditions PopIn
def eq_system(population, beta, gamma, t):
    '''Defining SIR System of Equations'''
    # Creating an array of equations
    Eqs = np.zeros((3))
    Eqs[0] = -beta*population[0]*population[1]
    Eqs[1] = beta*population[0]*population[1] - gamma*population[1]
    Eqs[2] = gamma*population[1]
    return Eqs

#SIR = spi.odeint(eq_system, population, t_interval (0.5), (0,1))

"""
i = 0

# first 3 records
temp = dataframe[i:i+3]
"""


# error function y - y^
def sumerror_sir(x):
    beta = x[0]
    gamma = x[1]
    y = spi.odeint(eq_system, population, t_interval, (beta, gamma))  # returns np ndarray
    # convert to pandas dataframe = y2
    y2 = pd.DataFrame(np.float_(y[0:,0:]), index=np.arange(t_start, t_end), columns=['S','I','R'])
    sqd_error = (y2 - dataframe)**2
    return sqd_error['I'].sum()

# print type(error_model(eq_system))
# print sumerror_sir([2, 0.3])

"""
def con(x):
	return

cons = {'type':'ineq', 'fun': con}
"""


x0 = np.array([beta, gamma])

# impt for positive results
bnds = tuple((0,100) for x in x0)

# optimize function: minimizes the sum of squared errors
# result = the optimised [beta, gamma] values
result = spo.minimize(sumerror_sir, x0, method='slsqp', bounds=bnds).x
print result

# minimum error
print sumerror_sir(result)

# Plot the result
# data
pylab.plot(t_interval, dataframe['I'])
# fitted graph
fit = spi.odeint(eq_system, population, t_interval, (result[0], result[1]))
fitdf = pd.DataFrame(np.float_(fit[0:,0:]), index=np.arange(t_start, t_end), columns=['S','I','R'])
# print fitdf
pylab.plot(t_interval, fitdf['I'])

pylab.show()

