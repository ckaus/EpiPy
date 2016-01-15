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

    def model(self, y, x, beta, gamma, mu):
        """
		Mistake on wiki: https://en.wikipedia.org/wiki/Epidemic_model#The_SIRS_model is a SIRSwbad Model!
        Take a look here http://www.mathe.tu-freiberg.de/~wegert/Lehre/Seminar3/moehler.pdf page 3 (SIRS/SIRSwbad) or
        http://msemac.redwoods.edu/~darnold/math55/DEProj/sp08/bgill/presentation2.pdf slide 14 (SIRS)
		:param y:
		:param x:
		:param beta:
		:param gamma:
		:param mu:
		:param f:
		:param beta:
		:param y:
		"""
        S = -beta * y[0] * y[1] / self.N + mu * y[2]
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1] - mu * y[2]
        return S, I, R

    def fit_odeint(self, x, beta, gamma, mu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:, 1]


class SIRSwbad(SIRS):
    def __init__(self):
        SIRS.__init__(self)

    def model(self, y, x, beta, gamma, mu, f):
        """
        Mistake on wiki: https://en.wikipedia.org/wiki/Epidemic_model#The_SIRS_model is a SIRSwbad Model!
        Take a look here http://www.mathe.tu-freiberg.de/~wegert/Lehre/Seminar3/moehler.pdf page 3 (SIRS/SIRSwbad) or
        http://msemac.redwoods.edu/~darnold/math55/DEProj/sp08/bgill/presentation2.pdf slide 14 (SIRS)
		f = Average loss of immunity rate of recovered individuals
		:param y:
		:param x:
		:param beta:
		:param gamma:
		:param mu:
		:param f:
		:param beta:
		:param y:
		"""
        S,I,R = SIRS.model(self, y, x, beta, gamma, mu)
        S = S - f * y[0] + f * self.N
        I = I - f * y[1]
        R = R - f * y[2]
        return S, I, R

    def fit_odeint(self, x, beta, gamma, mu, f):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu, f))[:, 1]