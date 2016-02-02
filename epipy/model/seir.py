# -*- coding: utf-8 -*-

from scipy import integrate

from basemodel import BaseModel


class SEIR(BaseModel):
    """
    This class represents an abstract model for SEIR Models.
    """
    def __init__(self):
        BaseModel.__init__(self)
        self.__name__ = 'SEIR'

    def init_param(self, y0):
        """
        This function initialize the model parameters.

        :param y0: infected value in t0.
        :type y0: int or float

        :returns: tuple of S,E,I,R model values in t0
        """
        E0 = y0
        S0 = self.N - E0
        I0 = 0.0
        R0 = 0.0
        return S0, E0, I0, R0


class Simple(SEIR):
    """
    This class represents the SEIR Simple Model
    """
    def __init__(self):
        SEIR.__init__(self)

    def model(self, y, x, beta, gamma, sigma, mu):
        """
        This function defines the SEIR Simple Model.

        :param y: y values, which represents the individuals
        :type y: array
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param sigma: The rate at which an exposed person becomes infective.
        :type sigma: float
        :param mu: The parameter represents the average death rate
        :type mu: float

        :returns: a tuple of S,E,I,R in tn, where n=time step
        """
        S = mu * (self.N - y[0]) - (beta * y[0] * y[2] / self.N)
        E = beta * y[0] * y[2] / self.N - (mu + sigma) * y[1]
        I = sigma * y[1] - (mu + gamma) * y[2]
        R = gamma * y[2] - mu * y[3]
        return S, E, I, R

    def fit_model(self, x_data, beta, gamma, sigma, mu):
        """
        This function start the fitting process.
        It integrates a system of ordinary differential equations.

        :param x_data: data on x-axis
        :type x_data: array
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param sigma: The rate at which an exposed person becomes infective.
        :type sigma: float
        :param mu: The parameter represents the average death rate
        :type mu: float

        :returns: a fitted model for infected individuals
        """
        return integrate.odeint(self.model, self.N0, x_data, args=(beta, gamma, sigma, mu))[:, 2]
