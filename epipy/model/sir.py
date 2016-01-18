# -*- coding: utf-8 -*-

from scipy import integrate

from basemodel import BaseModel


class SIR(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.__name__ = 'SIR'

    def init_param(self, y0):
        I0 = y0
        S0 = self.N - I0
        R0 = 0.0
        return S0, I0, R0


class Simple(SIR):
    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma):
        S = -beta * y[0] * y[1] / self.N
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1]
        return S, I, R

    def fit_model(self, x, beta, gamma):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma))[:, 1]


class Vaccine(SIR):
    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma, nu):
        S = -beta * y[0] * y[1] / self.N - nu * y[0]
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1] + nu * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, nu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, nu))[:, 1]


class WithBirthsAndDeaths(SIR):
    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma, mu):
        S = -beta * y[0] * y[1] / self.N + mu * (self.N - y[0])
        I = beta * y[0] * y[1] / self.N - gamma * y[1] - mu * y[1]
        R = gamma * y[1] - mu * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, mu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:, 1]
