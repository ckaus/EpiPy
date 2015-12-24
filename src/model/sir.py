# -*- coding: utf-8 -*-

"""This file contains the SIR-Model."""
# http://stackoverflow.com/questions/34422410/fitting-sir-model-based-on-least-squares/34425290#34425290

from scipy import integrate, optimize
from utils import logger

class SIR(object):

    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        self.N = 1
        self.N0 = self.init_param(ydata, self.N)

    def init_param(self, ydata, N):
        I0 = ydata[0]
        S0 = N - I0
        R0 = 0.0
        return S0, I0, R0

    def sir_model(self, y, x, beta, gamma):
        S = -beta * y[0] * y[1] / self.N
        R = gamma * y[1]
        I = -(S + R)
        return S, I, R

    def fit(self, debug=0):
        def fit_odeint(x, beta, gamma):
            return integrate.odeint(self.sir_model, self.N0, x, args=(beta, gamma))[:,1]

        popt, pcov = optimize.curve_fit(fit_odeint, self.xdata, self.ydata)
        result = fit_odeint(self.xdata, *popt)
        if debug:
            logger.info("Fitting SIR Model by using func=curve_fit.")
            logger.info("popt: %s" % popt)
            logger.info("Description: Optimal values for the parameters so that the sum of the squared error of f(xdata, *popt) - ydata is minimized")
            logger.info("pcov: %s" % pcov)
            logger.info("Description: The estimated covariance of popt. The diagonals provide the variance of the parameter estimate.")
            logger.info("result: %s" % result)
        return result