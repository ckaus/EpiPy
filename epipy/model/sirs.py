# -*- coding: utf-8 -*-

from basemodel import BaseModel
from scipy import integrate


class SIRS(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)

    def init_param(self, y0):
        I0 = y0
        S0 = self.N - I0
        R0 = 0.0
        return S0, I0, R0


class Simple(SIRS):
    def __init__(self):
        SIRS.__init__(self)

    def model(self, y, x, beta, gamma, mu):
        S = -beta * y[0] * y[1] / self.N + mu * y[2]
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1] - mu * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, mu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:, 1]


class WithBirthsAndDeaths(SIRS):
    def __init__(self):
        SIRS.__init__(self)

    def model(self, y, x, beta, gamma, mu, f):
        S = -beta * y[0] * y[1] / self.N + mu * y[2] + f * self.N
        I = beta * y[0] * y[1] / self.N - gamma * y[1] - f * y[1]
        R = gamma * y[1] - mu * y[2] - f * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, mu, f):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu, f))[:, 1]