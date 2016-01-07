# -*- coding: utf-8 -*-

"""This file contains the SIR-Model."""
# http://stackoverflow.com/questions/34422410/fitting-sir-model-based-on-least-squares/34425290#34425290

from basemodel import BaseModel
from scipy import integrate

class SIR(BaseModel):

    def __init__(self, xdata, ydata):
        BaseModel.__init__(self)
        self.xdata = xdata
        self.ydata = ydata
        self.N = 1
        self.N0 = self.init_param(ydata, self.N)

    def init_param(self, ydata, N):
        I0 = ydata[0]
        S0 = N - I0
        R0 = 0.0
        return S0, I0, R0

    def model(self, y, x, beta, gamma):
        S = -beta * y[0] * y[1] / self.N
        R = gamma * y[1]
        I = -(S + R)
        return S, I, R

    def fit_odeint(self, x, beta, gamma):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma))[:,1]