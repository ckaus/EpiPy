# -*- coding: utf-8 -*-

from basemodel import BaseModel
from scipy import integrate


class SEIR(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)

    def init_param(self, y0):
        E0 = y0
        S0 = self.N - E0
        I0 = 0.0
        R0 = 0.0
        return S0, E0, I0, R0


class Simple(SEIR):
    def __init__(self):
        SEIR.__init__(self)
        
    @staticmethod
    def param():
        return ["beta", "gamma", "sigma", "mu"]
    

    def model(self, y, x, beta, gamma, sigma, mu):
        S = mu * (self.N - y[0]) - ( beta * y[0] * y[2] / self.N)
        E = beta * y[0] * y[2] / self.N - (mu + sigma) * y[1]
        I = sigma * y[1] - (mu + gamma) * y[2]
        R = gamma * y[2] - mu * y[3]
        return S, E, I, R

    def fit_model(self, x, beta, gamma, sigma, mu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, sigma, mu))[:, 2]
