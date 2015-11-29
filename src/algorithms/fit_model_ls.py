from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np
import csv
import sir

## load data
"""
#originaldata = np.array(readCSV())
originaldata = np.loadtxt('googleflugermany.csv', delimiter=',', skiprows=1)[50:100]
print originaldata
timetotal = np.array(range(len(originaldata)))
"""
# number of training data = n
n = 23

timetotal = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161])
timetrain = timetotal[:n]

originaldata = np.array([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ])
data = originaldata[:n]

# Set initial parameter values
beta = 0.75
gamma = 0.75
k = 1.0/sum(data)


# Set initial population conditions
def setInitPop():
    I0 = data[0]*k
    S0 = 1 - I0
    N = [S0, I0, 0]
    return N

N0 = setInitPop()


# Scale out to original scale
def scale_out(Nt):
    # Get the second column of data corresponding to I
    # INt = [row[1] for row in Nt]
    Nt = np.divide(Nt, k)
    return Nt


# Get the sum of squared errors of I (for least squares method)
def SSE(model):

	# select the right model
    if model=="sir":
        ode = sir.ode

    def result(x):

        Nt = integrate.odeint(ode, N0, timetrain, args=tuple(x))

        INt = [row[1] for row in Nt]
        INt = np.divide(INt, k)

        difference = data - INt

        LL = np.dot(difference, difference)

        return LL
        
    return result


# Get the fitted parameters
def fit(model, x0):
    
    # Do the fitting
    results = minimize(SSE(model), x0, method='nelder-mead')

	# return parameters
    return results.x


# main
def main():
    param = fit("sir", [beta,gamma,k])

    # Get the fitted model
    Nt = integrate.odeint(sir.ode, N0, timetotal, args=tuple(param))
    Nt = scale_out(Nt)

    # Get the second column of data corresponding to I
    INt = [row[1] for row in Nt]

    # Plot data and fit
    py.clf()
    py.plot(timetotal, originaldata, 'o')
    py.plot(timetotal, INt)
    py.show()


if __name__ == "__main__":
    main()

