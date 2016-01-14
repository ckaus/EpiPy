# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize


class BaseModel(object):
    """
    This class defines an abstract epidemic model class.
    An epidemic model is a simplified means of describing
    the transmission of communicable disease through individuals.
    """

    def __init__(self):
        __metaclass__ = ABCMeta

    @abstractmethod
    def model(self, y, x, **param): pass

    def base_model(self, I0, N, time, **param):
        self.N = N
        self.N0 = self.init_param(I0)
        return self.fit_odeint(time, **param)

    @abstractmethod
    def init_param(self, y0): pass

    @abstractmethod
    def fit_odeint(self, x, **param): pass

    def fit(self, xdata, ydata, **param):
        self.N = 1
        self.N0 = self.init_param(ydata[0])
        if not param:
            # estimate best param (rates) values
            param, pcov = optimize.curve_fit(self.fit_odeint, xdata, ydata)
            return self.fit_odeint(xdata, *param)
        return self.fit_odeint(xdata, **param)
