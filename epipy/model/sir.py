# -*- coding: utf-8 -*-

"""This file contains the SIR-Model."""
# http://stackoverflow.com/questions/34422410/fitting-sir-model-based-on-least-squares/34425290#34425290

from basemodel import BaseModel
from scipy import integrate

class SIR(BaseModel):

    def __init__(self, xdata, ydata):
        BaseModel.__init__(self, xdata, ydata)
        
    def init_param(self):
        S0 = 0.0
        I0 = 0.0
        R0 = 0.0
        # Susceptible
        if self.model_class is 0:
            S0 = self.ydata[0]
            I0 = self.N - S0
            R0 = 0.0
        # Infected
        elif self.model_class is 1:
            I0 = self.ydata[0]
            S0 = self.N - I0
            R0 = 0.0
        # Recovered
        elif self.model_class is 2:
            R0 = ydata[0]
            # We can not know the amount of S0 and I0 if we have
            # only knownledge of R0. 
            I0 = (self.N - R0) / 2
            S0 = self.N - I0
        return S0, I0, R0

    def model(self, y, x, beta, gamma):
        S = -beta * y[0] * y[1] / self.N
        R = gamma * y[1]
        I = -(S + R)
        return S, I, R

    def fit_odeint(self, x, beta, gamma):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma))[:,self.model_class]