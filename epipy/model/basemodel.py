# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize, stats
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

    @staticmethod
    def fit_info(x, y):
        """ Return R^2 and p-value of linear regression between x and y
            where x and y are array-like."""
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return (r_value*r_value, p_value)

    def fit(self, xdata, ydata, N=None, **param):
        self.N = N
        self.N0 = self.init_param(ydata[0])
        if not param:
            param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
            clasz = inspect.stack()[1][1]
            print "Best param for %s: %s" % (self.__class__.__name__, param)
            fitted = self.fit_model(xdata, *param)
            return (fitted, param) + self.fit_info(ydata, fitted)
        fitted = self.fit_model(xdata, *param)
        return (fitted, param) + self.fit_info(ydata, fitted)

    @abstractmethod
    def init_param(self, y0): pass
