# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize, stats


class BaseModel(object):
    def __init__(self):
        __metaclass__ = ABCMeta
        self.N = None
        self.N0 = None
        self.best_fit = None
        self.quality_of_fit = None

    def calculate_regression_line(self, x, y):
        # Calculates regression line. Mostly for Quality of fit(a float between 0 and 1).
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return slope, intercept, r_value ** 2, p_value, std_err

    def fit(self, xdata, ydata, N=None, **param):
        self.N = N
        self.N0 = self.init_param(ydata[0])
        if not param:
            param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
            self.best_fit = param
            fit = self.fit_model(xdata, *param)
            reg_line_values = self.calculate_regression_line(ydata, fit)
            self.quality_of_fit = reg_line_values[2]
            return fit
        self.best_fit = self.fit_model(xdata, **param)
        return self.best_fit

    @abstractmethod
    def init_param(self, y0): pass

    def __repr__(self):
        return '<object=%s - Population=%s - Initial Parameter=%s - >' % (
            self.__class__.__name__, self.N, self.N0)

    def __str__(self):
        return '%s - %s\nBest Fit: %s\nQuality Of Fit: %s' \
               % (self.__name__, self.__class__.__name__, self.best_fit, self.quality_of_fit)
