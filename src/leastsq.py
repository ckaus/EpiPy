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
S0 = 0.99999
I0 = 0.00001
R0 = 0.0
population = (S0, I0, R0)
beta = 0.9
gamma = 0.5
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

# SIR = spi.odeint(eq_system, population, t_interval)

i = 0

# error function y - y^

def sumerror_sir(b, g):
    y = spi.odeint(eq_system, population, t_interval, (b, g))  # returns np ndarray
    # convert to pandas dataframe = y2
    y2 = pd.DataFrame(np.float_(y[0:,0:]), index=np.arange(t_start, t_end), columns=['S','I','R'])
    sqd_error = (y2 - dataframe)**2
    print sqd_error
    return sqd_error['I'].sum()

# print type(error_model(eq_system))
print sumerror_sir(2, 0.3)

# first 3 records
temp = dataframe[i:i+3]


#result = spo.minimize(sumerror_sir, np.array([0.5, 1]), args=(0.5))
#print result

i = i+3

"""
#Splitting out the curves for S, I and R from each other, in case they need
#to be used seperately
S=(SIR[:,0])
I=(SIR[:,1])
R=(SIR[:,2])

#Create a new array of the same length to be used as the x-axis for a plot
x=arange(len(SIR),dtype=float)

#Scale x-axis array by the step size
for i in x:
    x[i]=(x[i]*t_step)

#Stack S, I and R with the x-axis
SIR_plot= vstack([S,I,R,x])

#Graph!
fig= figure()
ax = fig.add_subplot(111)
plot(SIR_plot[3],SIR_plot[0],'g--',SIR_plot[3],SIR_plot[1],'r-',SIR_plot[3],SIR_plot[2],'-.b',linewidth=3)
xlabel("Time (days)")
ylabel("Percent of Population")
title("Zombie SIR Epidemic")
grid(True)
legend(("Survivors", "Zombies", "Dead"), shadow=True, fancybox=True)
show()
"""
