# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize
from scipy import stats
import inspect


class BaseModel(object):
    def __init__(self):
        __metaclass__ = ABCMeta
        self.N = None
        self.N0 = None

    def get_model(self, xdata, y0, N=None, **param):
        self.N = N
        self.N0 = self.init_param(y0)
        return self.fit_model(xdata, **param)
    
    def calculateRegressionLine(self, x, y):
    #Calculates regression line. Mostly for Quality of fit(a float between 0 and 1).
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        regressionLineValues = (slope, intercept, r_value**2, p_value, std_err)
        return regressionLineValues


    def fit(self, xdata, ydata, N=None, **param):
        self.N = N
        self.N0 = self.init_param(ydata[0])
        if not param:
            param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
            clasz = inspect.stack()[1][1]
            print "Best param for %s: %s" % (self.__class__.__name__, param)
            fit = self.fit_model(xdata, *param)
            regressionLineValues = self.calculateRegressionLine(ydata, fit)
            print "Quality of Fit:", regressionLineValues[2]
            print "p=value: ", regressionLineValues[3]
            return fit
        return self.fit_model(xdata, **param)

    @abstractmethod
    def init_param(self, y0): pass
