# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize, stats

from epipy.utils import logging


class BaseModel(object):
    def __init__(self):
        __metaclass__ = ABCMeta
        self.N = None
        self.N0 = None

    def fit_info(self, ydata_1, ydata_2):
        """ Return R^2 and p-value of linear regression between x and y
            where x and y are array-like."""
        slope, intercept, r_value, p_value, std_err = stats.linregress(
                ydata_1, ydata_2)
        return slope, intercept, r_value ** 2, p_value, std_err

    def fit(self, xdata, ydata, N=None, **param):
        try:
            self.N = N
            self.N0 = self.init_param(ydata[0])

            if not param:
                param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
                fitted = self.fit_model(xdata, *param)
                return (fitted, param) + self.fit_info(ydata, fitted)

            fitted = self.fit_model(xdata, **param)
            return (fitted, param)

        except RuntimeError as error:
            logging.error('Runtime Error %s' % error)
            return

    @abstractmethod
    def init_param(self, y0):
        pass

    def __repr__(self):
        return '<object=%s - Population=%s - Initial Parameter=%s - >' % (
            self.__class__.__name__, self.N, self.N0)

    def __str__(self):
        return '%s - %s\nPopulation: %s\nInitial Parameter %s' \
               % (self.__name__, self.__class__.__name__, self.N, self.N0)
