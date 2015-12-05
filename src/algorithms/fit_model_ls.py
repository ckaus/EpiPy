from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np
import csv
from model import *

class LeastSquaresFit:

    # Set initial population conditions
    def getInitPop(self):
        I = self.dataI[0]
        # select the right model
        if self.model=="sir":
            N = sir.pop(I,self.k)
        elif self.model=="seir":
            N = seir.pop(I,self.k)
        else:
            #raise NameError(self.model, 'is not a supported model')
            print ('ERROR: "' + self.model + '" is not a supported model')
            exit(-1)
        return N
        
    def getInitParam(self):
        if self.model=="sir":
            param = sir.param()
        if self.model=="seir":
            param = seir.param()
        return param

    def setODE(self):
        if self.model=="sir":
            self.ode = sir.ode
        if self.model=="seir":
            self.ode = seir.ode

    def __init__(self, model, data):
    # number of training data = n
        self.n = int(len(data['Time'])*(0.9))
        self.model = model
        self.timetotal = data['Time']
        self.timetrain = self.timetotal[:self.n]
        self.originaldataI = data['I']
        self.dataI = self.originaldataI[:self.n]
        self.k = 1.0/sum(self.dataI)
        self.N0 = self.getInitPop()
    
        # Set initial parameter values
        self.paramInit = self.getInitParam()
        self.paramInit.append(self.k)
        self.setODE()


    # Scale out to original scale
    def scale_out(self, Nt):
        # Get the second column of data corresponding to I
        # INt = [row[1] for row in Nt]
        Nt = np.divide(Nt, self.k)
        return Nt


    # Get the sum of squared errors of I (for least squares method)
    def SSE(self, model):

        def result(x):

            Nt = integrate.odeint(self.ode, self.N0, self.timetrain, args=tuple(x))

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
        print param

        # Get the fitted model
        Nt = integrate.odeint(self.ode, self.N0, self.timetotal, args=tuple(param))
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
    data = {"Time": np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161]),
            "I": np.array([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ])}
    
    LeastSquaresFit(model, data).run()
