from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np
import csv
import sir

class LeastSquaresFit:

    # Set initial population conditions
    def setInitPop(self):
        I0 = self.dataI[0]*self.k
        S0 = 1 - I0
        N = [S0, I0, 0]
        return N
        
    def getInitParam(self):
        if self.model=="sir":
            param = sir.param()
        return param

    def __init__(self, model, data):
    # number of training data = n
        self.n = 15
        self.timetotal = data['Time']
        self.timetrain = self.timetotal[:self.n]
        self.originaldataI = data['I']
        self.dataI = self.originaldataI[:self.n]
        self.k = 1.0/sum(self.dataI)
        self.N0 = self.setInitPop()
        self.model = model
    
        # Set initial parameter values
        self.paramInit = self.getInitParam()
        self.paramInit.append(self.k)


    # Scale out to original scale
    def scale_out(self, Nt):
        # Get the second column of data corresponding to I
        # INt = [row[1] for row in Nt]
        Nt = np.divide(Nt, self.k)
        return Nt


    # Get the sum of squared errors of I (for least squares method)
    def SSE(self, model):

        # select the right model
        if model=="sir":
            ode = sir.ode

        def result(x):

            Nt = integrate.odeint(ode, self.N0, self.timetrain, args=tuple(x))

            INt = [row[1] for row in Nt]
            INt = np.divide(INt, self.k)

            difference = self.dataI - INt

            # square the difference
            LL = np.dot(difference, difference)

            return LL
        
        return result


    # Get the fitted parameters
    def fit(self, x0):
    
        # Do the fitting
        results = minimize(self.SSE(self.model), x0, method='nelder-mead')

        # return parameters
        return results.x


    # main
    def run(self):
        param = self.fit(self.paramInit)

        # Get the fitted model
        Nt = integrate.odeint(sir.ode, self.N0, self.timetotal, args=tuple(param))
        Nt = self.scale_out(Nt)

        # Get the second column of data corresponding to I
        INt = [row[1] for row in Nt]

        # Plot data and fit
        py.clf()
        py.plot(self.timetotal, self.originaldataI, 'o')
        py.plot(self.timetotal, INt)
        py.show()


if __name__ == "__main__":
    
    model = "sir"
    data = {"Time": [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],
            "I": [ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]}
    
    LeastSquaresFit(model, data).run()
