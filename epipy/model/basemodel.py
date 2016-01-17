# -*- coding: utf-8 -*-

import inspect
from abc import abstractmethod, ABCMeta
from scipy import optimize, stats


class BaseModel(object):
    def __init__(self):
        __metaclass__ = ABCMeta
        self.N = None
        self.N0 = None

    def calculate_regression_line(self, x, y):
        # Calculates regression line. Mostly for Quality of fit(a float between 0 and 1).
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return (slope, intercept, r_value ** 2, p_value, std_err)

    def fit(self, xdata, ydata, N=None, **param):
        self.N = N
        self.N0 = self.init_param(ydata[0])
        if not param:
            param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
            clasz = inspect.stack()[1][1]
            print "Best param for %s: %s" % (self.__class__.__name__, param)
            fit = self.fit_model(xdata, *param)
            reg_line_values = self.calculate_regression_line(ydata, fit)
            print "Quality of Fit:", reg_line_values[2]
            print "p=value: ", reg_line_values[3]
            return fit
        return self.fit_model(xdata, **param)

    @abstractmethod
    def init_param(self, y0): pass
