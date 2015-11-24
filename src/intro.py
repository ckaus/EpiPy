#!/usr/bin/env python
#
# The above allows this script to be run directly from the shell
#

# This loads some pacakges that have arrays etc and the ODE integrators
import scipy, scipy.integrate, csv

realTime = list()
realS = list()
realI = list()
realR = list()

def readCSV():
	with open('resources/data1.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		next(csvfile, None) # skip the first line
		for row in reader:
			realTime.append(row[0])
			realS.append(row[1])
			realI.append(row[2])
			realR.append(row[3])
	return [realTime,realS,realI,realR]
	



	
"""

# Parameters
beta = 5
gamma = 0.1

# Initial condition

I0 = 0.01
S0 = 1-I0
R0 = 0.00

Y0 = [ S0, I0, R0 ]

tMax = 100

# Time vector for solution
T = scipy.linspace(0, tMax, 1001)


# This defines a function that is the right-hand side of the ODEs
# Warning!  Whitespace at the begining of a line is significant!
def rhs(Y, t, beta, gamma):
    '''
    SIR model.
   
    This function gives the right-hand sides of the ODEs.
    '''
   
    # Convert vector to meaningful component vectors
    # Note: Indices start with index 0, not 1!
    S = Y[0]
    I = Y[1]
    R = Y[2]
   
    N = S + I + R
   
    # The right-hand sides
    dS = - beta * I * S
    dI = beta * I * S  - (gamma ) * I
    dR = gamma * I
   
    # Convert meaningful component vectors into a single vector
    dY = [ dS, dI, dR ]

    return dY



def SSE(rhs, data, n):
    result = rhs
    sse = sum( (result[1]-data[1])^2)
    return sse








# Integrate the ODE
# Warning!  The ODE solver over-writes the initial value.
# This can be a pain in the ass if you run the ODE multiple times.
# Also, 'args' passes parameters to right-hand-side function.
solution = scipy.integrate.odeint(rhs,
                                  Y0,
                                  T,
                                  args = (beta, gamma))
       
S = solution[:, 0]
I = solution[:, 1]
R = solution[:, 2]

N = S + I + R


# Make plots

# Load a plotting package
# PyLab is motivated by Matlab...
import pylab

# I usually use PyLab for quick plots
# and the Python GnuPlot package for publication

pylab.figure()

pylab.plot(#T, S / N,
           T, I / N,
           #T, R / N
)

pylab.xlabel('Time')
pylab.ylabel('Proportion')

pylab.legend([ 'Susceptible', 'Infective', 'Recovered' ])

# Actually display the plot
pylab.show()
"""
