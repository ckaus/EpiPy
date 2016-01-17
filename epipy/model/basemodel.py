# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize
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

    def fit(self, xdata, ydata, N=None, **param):
        self.N = N
        self.N0 = self.init_param(ydata[0])
        if not param:
            param, pcov = optimize.curve_fit(self.fit_model, xdata, ydata)
            clasz = inspect.stack()[1][1]
            print "Best param for %s: %s" % (self.__class__.__name__, param)
            return self.fit_model(xdata, *param)
        return self.fit_model(xdata, **param)

    @abstractmethod
    def init_param(self, y0): pass
